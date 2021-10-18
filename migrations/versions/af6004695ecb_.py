"""empty message

Revision ID: af6004695ecb
Revises: 2e8d1f9e469c
Create Date: 2021-10-18 00:38:07.903650

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'af6004695ecb'
down_revision = '2e8d1f9e469c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'nombre_rol',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'role', ['nombre_rol'])
    op.drop_constraint('role_ibfk_1', 'role', type_='foreignkey')
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.drop_index('username', table_name='users')
    op.create_foreign_key(None, 'users', 'role', ['username'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_index('username', 'users', ['username'], unique=False)
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.create_foreign_key('role_ibfk_1', 'role', 'users', ['nombre_rol'], ['id'])
    op.drop_constraint(None, 'role', type_='unique')
    op.alter_column('role', 'nombre_rol',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
