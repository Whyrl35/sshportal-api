"""empty message

Revision ID: e8ca6557aa28
Revises:
Create Date: 2020-04-02 00:02:27.406489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8ca6557aa28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revoked_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_revoked_tokens'))
    )
    with op.batch_alter_table('host_groups', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uix_host_groups_name'), ['name'])
        batch_op.drop_index('uix_hostgroups_name')

    with op.batch_alter_table('hosts', schema=None) as batch_op:
        batch_op.drop_index('uix_hosts_name')
        batch_op.create_unique_constraint(batch_op.f('uix_hosts_name'), ['name'])

    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_index('uix_settings_name')
        batch_op.create_unique_constraint(batch_op.f('uix_settings_name'), ['name'])

    with op.batch_alter_table('ssh_keys', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uix_ssh_keys_name'), ['name'])
        batch_op.drop_index('uix_keys_name')

    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uix_user_groups_name'), ['name'])
        batch_op.drop_index('uix_usergroups_name')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=True))
        batch_op.create_index(batch_op.f('idx_users_name'), ['name'], unique=True)
        batch_op.drop_index('uix_users_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('uix_users_name', ['name'], unique=1)
        batch_op.drop_index(batch_op.f('idx_users_name'))
        batch_op.drop_column('password')

    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.create_index('uix_usergroups_name', ['name'], unique=1)
        batch_op.drop_constraint(batch_op.f('uix_user_groups_name'), type_='unique')

    with op.batch_alter_table('ssh_keys', schema=None) as batch_op:
        batch_op.create_index('uix_keys_name', ['name'], unique=1)
        batch_op.drop_constraint(batch_op.f('uix_ssh_keys_name'), type_='unique')

    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uix_settings_name'), type_='unique')
        batch_op.create_index('uix_settings_name', ['name'], unique=1)

    with op.batch_alter_table('hosts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uix_hosts_name'), type_='unique')
        batch_op.create_index('uix_hosts_name', ['name'], unique=1)

    with op.batch_alter_table('host_groups', schema=None) as batch_op:
        batch_op.create_index('uix_hostgroups_name', ['name'], unique=1)
        batch_op.drop_constraint(batch_op.f('uix_host_groups_name'), type_='unique')

    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.create_table('migrations',
    sa.Column('id', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('revoked_tokens')
    # ### end Alembic commands ###