"""Add posted_by column

Revision ID: 9df963dd3fed
Revises: 546b964dab90
Create Date: 2019-05-28 06:25:39.110948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df963dd3fed'
down_revision = '546b964dab90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch_table', sa.Column('posted_by', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch_table', 'posted_by')
    # ### end Alembic commands ###
