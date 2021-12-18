"""teachers table

Revision ID: 07e7001b07bd
Revises: 92f40034387a
Create Date: 2021-12-18 20:19:30.581776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07e7001b07bd'
down_revision = '92f40034387a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teacher_email'), 'teacher', ['email'], unique=True)
    op.create_index(op.f('ix_teacher_username'), 'teacher', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teacher_username'), table_name='teacher')
    op.drop_index(op.f('ix_teacher_email'), table_name='teacher')
    op.drop_table('teacher')
    # ### end Alembic commands ###
