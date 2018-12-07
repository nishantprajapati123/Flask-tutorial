"""Added owners

Revision ID: adfbb0bb2d92
Revises: 6f3a47de56e9
Create Date: 2018-12-07 16:00:40.987831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adfbb0bb2d92'
down_revision = '6f3a47de56e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    # ### end Alembic commands ###
