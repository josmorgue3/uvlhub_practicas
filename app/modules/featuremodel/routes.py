from flask import jsonify, render_template, request
from flask_login import current_user, login_required
from app.modules.dataset.services import RatingService
from app.modules.featuremodel import featuremodel_bp


@featuremodel_bp.route('/featuremodel', methods=['GET'])
def index():
    return render_template('featuremodel/index.html')


@featuremodel_bp.route("/model/rate", methods=["POST"])
@login_required
def rate_model():
    user_id = current_user.id
    model_id = request.form.get("model_id")
    rating = int(request.form.get("rating"))

    if not model_id or not rating:
        return jsonify({"error": "Missing model ID or rating"}), 400

    # Guarda la valoración
    RatingService.add_model_rating(user_id, model_id, rating)

    # Obtiene el promedio actualizado
    average_rating = RatingService.get_average_model_rating(model_id)

    return jsonify({"model_id": model_id, "average_rating": average_rating})