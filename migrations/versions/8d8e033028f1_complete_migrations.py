"""complete migrations

Revision ID: 8d8e033028f1
Revises: 38d244b2fbc2
Create Date: 2024-11-16 17:25:56.576192

"""
from alembic import op
import sqlalchemy as sa
from sqlmodel import SQLModel
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '8d8e033028f1'
down_revision = '38d244b2fbc2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extensions', schema=None) as batch_op:
        batch_op.alter_column('date_out',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.drop_column('sorti')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extensions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sorti', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.alter_column('date_out',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###