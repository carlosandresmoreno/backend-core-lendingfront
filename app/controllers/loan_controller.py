from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.schemas.loan_schema import LoanRequestSchema
from app.services.loan_service import evaluate_loan_amount

loan_blueprint = Blueprint("loans", __name__)

@loan_blueprint.route('/evaluate', methods=['POST'])
def evaluate_loan():
    """
    Evaluar solicitud de préstamo
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - requested_amount
          properties:
            requested_amount:
              type: number
              example: 40000
    responses:
      200:
        description: Decisión del préstamo
        schema:
          type: object
          properties:
            decision:
              type: string
              example: Approved
      400:
        description: Error de validación
        schema:
          type: object
          properties:
            error:
              type: string
              example: Invalid input
    """
    try:
        payload = LoanRequestSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

    response = evaluate_loan_amount(payload.requested_amount)
    return jsonify(response.model_dump()), 200
