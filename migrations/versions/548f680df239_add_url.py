"""add_url

Revision ID: 548f680df239
Revises: 907a80dc8ab8
Create Date: 2019-06-07 07:50:19.307356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '548f680df239'
down_revision = '907a80dc8ab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issue', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issue', 'url')
    # ### end Alembic commands ###