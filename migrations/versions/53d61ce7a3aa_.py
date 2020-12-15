"""empty message

Revision ID: 53d61ce7a3aa
Revises: 4d7cd3ea3aa2
Create Date: 2020-12-15 14:58:17.651279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d61ce7a3aa'
down_revision = '4d7cd3ea3aa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('send_gift_date', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('giftee', schema=None) as batch_op:
        batch_op.drop_column('send_gift_date')

    # ### end Alembic commands ###