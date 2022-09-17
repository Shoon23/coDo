"""empty message

Revision ID: b7d857f6d5ad
Revises: 
Create Date: 2022-09-16 22:13:31.602571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d857f6d5ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('completed_todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo_item', sa.Text(), nullable=False),
    sa.Column('createdAt', sa.String(length=30), nullable=False),
    sa.Column('completedAt', sa.String(length=30), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('progress_todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo_item', sa.Text(), nullable=False),
    sa.Column('createdAt', sa.String(length=30), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('progress_todo')
    op.drop_table('completed_todo')
    op.drop_table('user')
    # ### end Alembic commands ###