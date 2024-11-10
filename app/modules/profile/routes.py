from app.modules.auth.services import AuthenticationService
from app.modules.dataset.models import DataSet
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.modules.profile import profile_bp
from app.modules.profile.forms import UserProfileForm
from app.modules.profile.services import UserProfileService

@profile_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    auth_service = AuthenticationService()
    profile = auth_service.get_authenticated_user_profile()
    if not profile:
        return redirect(url_for("public.index"))

    form = UserProfileForm()
    if request.method == "POST":
        service = UserProfileService()
        result, errors = service.update_profile(profile.id, form)
        return service.handle_service_response(
            result, errors, "profile.edit_profile", "Profile updated successfully", "profile/edit.html", form
        )

    return render_template("profile/edit.html", form=form)

@profile_bp.route('/profile/summary')
@login_required
def my_profile():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    user_datasets_pagination = db.session.query(DataSet) \
        .filter(DataSet.user_id == current_user.id) \
        .order_by(DataSet.created_at.desc()) \
        .paginate(page=page, per_page=per_page, error_out=False)

    total_datasets_count = db.session.query(DataSet) \
        .filter(DataSet.user_id == current_user.id) \
        .count()

    return render_template(
        'profile/summary.html',
        user_profile=current_user.profile,
        user=current_user,
        datasets=user_datasets_pagination.items,
        pagination=user_datasets_pagination,
        total_datasets=total_datasets_count
    )

@profile_bp.route('/profile/view/<int:user_id>')
@login_required
def view_profile(user_id):
    service = UserProfileService()
    user_profile = service.get(user_id)  # Obtiene el perfil del usuario

    if not user_profile:
        return render_template("profile/not_found.html"), 404

    # Obtener los datasets paginados del usuario
    page = request.args.get('page', 1, type=int)
    per_page = 5
    user_datasets_pagination = db.session.query(DataSet) \
        .filter(DataSet.user_id == user_id) \
        .order_by(DataSet.created_at.desc()) \
        .paginate(page=page, per_page=per_page, error_out=False)

    # Contar el total de datasets
    total_datasets_count = db.session.query(DataSet) \
        .filter(DataSet.user_id == user_id) \
        .count()

    # Pasa el perfil del usuario, el usuario en sí, los datasets y el total de datasets a la plantilla
    return render_template(
        "profile/view.html",
        user_profile=user_profile,
        user=user_profile,  # Pasamos user_profile como user
        datasets=user_datasets_pagination.items,
        pagination=user_datasets_pagination,
        total_datasets=total_datasets_count
    )


@profile_bp.route('/profile/search', methods=['GET'])
@login_required
def search_user():
    query = request.args.get('query', '').strip()  # Toma el término de búsqueda del formulario

    service = UserProfileService()
    users = service.search_users(query)  # Realiza la búsqueda en el servicio

    return render_template('profile/search_results.html', users=users, query=query)
