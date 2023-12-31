"""empty message

Revision ID: 647b46199251
Revises: 
Create Date: 2023-07-25 09:56:54.926523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '647b46199251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cnpj', sa.String(length=25), nullable=True),
    sa.Column('reasonName', sa.String(length=100), nullable=True),
    sa.Column('fantasyName', sa.String(length=100), nullable=True),
    sa.Column('cnae', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    # ### end Alembic commands ###
