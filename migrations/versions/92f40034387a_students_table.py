"""students table

Revision ID: 92f40034387a
Revises: 
Create Date: 2021-12-18 20:11:23.533314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f40034387a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_email'), 'student', ['email'], unique=True)
    op.create_index(op.f('ix_student_username'), 'student', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_username'), table_name='student')
    op.drop_index(op.f('ix_student_email'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###
