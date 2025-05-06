from marshmallow import Schema, fields, validate, EXCLUDE
from app.models.user import User

class UserSchema(Schema):
    class Meta:
        model = User
        load_instance = True
        unknown = EXCLUDE  
    id = fields.Int(dump_only=True) 
    email = fields.Email(required=True, validate=validate.Email())  
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))