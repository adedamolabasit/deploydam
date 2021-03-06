"""empty message

Revision ID: 0147f881ab41
Revises: b73182955c9d
Create Date: 2021-12-24 01:29:29.353158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0147f881ab41'
down_revision = 'b73182955c9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('image_file', sa.String(length=211), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'image_file')
    # ### end Alembic commands ###
