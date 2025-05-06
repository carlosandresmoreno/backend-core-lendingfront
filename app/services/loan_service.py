from app.schemas.loan_schema import LoanResponseSchema


def evaluate_loan_amount(amount: float) -> LoanResponseSchema:
    if amount > 50000:
        decision = 'Declined'
    elif amount == 50000:
        decision = 'Undecided'
    else:
        decision = 'Approved'

    return LoanResponseSchema(decision=decision)
