"""second

Revision ID: abbd658bec6c
Revises: 211899668d12
Create Date: 2022-06-21 03:00:42.663376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abbd658bec6c'
down_revision = '211899668d12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_encryption_encrypted_text', table_name='encryption')
    op.create_index(op.f('ix_encryption_encrypted_text'), 'encryption', ['encrypted_text'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_encryption_encrypted_text'), table_name='encryption')
    op.create_index('ix_encryption_encrypted_text', 'encryption', ['encrypted_text'], unique=False)
    # ### end Alembic commands ###