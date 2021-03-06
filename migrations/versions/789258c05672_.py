"""empty message

Revision ID: 789258c05672
Revises: a4d1992c4bb1
Create Date: 2021-12-31 02:04:49.559659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '789258c05672'
down_revision = 'a4d1992c4bb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
