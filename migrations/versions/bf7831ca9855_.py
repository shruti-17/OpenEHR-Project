"""empty message

Revision ID: bf7831ca9855
Revises: 
Create Date: 2022-01-21 03:38:28.611626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf7831ca9855'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userdata',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('doctor',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('doctor_name', sa.String(length=100), nullable=False),
    sa.Column('year_exp', sa.Integer(), nullable=True),
    sa.Column('speciality', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('fee', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['userdata.user_id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('doctor_id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('patient',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('patient_name', sa.String(length=100), nullable=False),
    sa.Column('date_of_reg', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('symptoms', sa.String(length=250), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['userdata.user_id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('patient_id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('pharma',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('pharma_id', sa.Integer(), nullable=True),
    sa.Column('pharma_name', sa.String(length=100), nullable=False),
    sa.Column('year_exp', sa.Integer(), nullable=True),
    sa.Column('phone_no', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('registration_no', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['pharma_id'], ['userdata.user_id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('pharma_id'),
    sa.UniqueConstraint('phone_no'),
    sa.UniqueConstraint('registration_no')
    )
    op.create_table('allergyIntolerance',
    sa.Column('allergy_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('substance', sa.String(length=250), nullable=False),
    sa.Column('verification_status', sa.String(length=25), nullable=False),
    sa.Column('allergy_intol_type', sa.String(length=25), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=True),
    sa.Column('manifestation', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.patient_id'], ),
    sa.PrimaryKeyConstraint('allergy_id')
    )
    op.create_table('pastHistoryIllness',
    sa.Column('illness_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('problem_name', sa.String(length=100), nullable=False),
    sa.Column('body_site', sa.String(length=100), nullable=False),
    sa.Column('datetime_onset', sa.DateTime(), nullable=False),
    sa.Column('severity', sa.String(length=50), nullable=True),
    sa.Column('procedure_type', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.patient_id'], ),
    sa.PrimaryKeyConstraint('illness_id')
    )
    op.create_table('prescription',
    sa.Column('prescription_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('medication_item', sa.String(length=100), nullable=True),
    sa.Column('route', sa.String(length=50), nullable=True),
    sa.Column('dosage_instruction', sa.String(length=50), nullable=True),
    sa.Column('additional_instruction', sa.String(length=250), nullable=True),
    sa.Column('reason', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.doctor_id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.patient_id'], ),
    sa.PrimaryKeyConstraint('prescription_id')
    )
    op.create_table('problemList',
    sa.Column('problem_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('problem_diag_name', sa.String(length=100), nullable=False),
    sa.Column('body_site', sa.String(length=50), nullable=False),
    sa.Column('datetime_onset', sa.DateTime(), nullable=True),
    sa.Column('severity', sa.String(length=25), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.patient_id'], ),
    sa.PrimaryKeyConstraint('problem_id')
    )
    op.create_table('doseDirection',
    sa.Column('dose_id', sa.Integer(), nullable=False),
    sa.Column('prescription_id', sa.Integer(), nullable=False),
    sa.Column('dose', sa.Float(), nullable=False),
    sa.Column('dose_unit', sa.String(length=10), nullable=False),
    sa.Column('frequency_per_day', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['prescription_id'], ['prescription.prescription_id'], ),
    sa.PrimaryKeyConstraint('dose_id')
    )
    op.create_table('orderDetails',
    sa.Column('orderdetails_id', sa.Integer(), nullable=False),
    sa.Column('prescription_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('date_discontinued', sa.Date(), nullable=False),
    sa.Column('date_written', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['prescription_id'], ['prescription.prescription_id'], ),
    sa.PrimaryKeyConstraint('orderdetails_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderDetails')
    op.drop_table('doseDirection')
    op.drop_table('problemList')
    op.drop_table('prescription')
    op.drop_table('pastHistoryIllness')
    op.drop_table('allergyIntolerance')
    op.drop_table('pharma')
    op.drop_table('patient')
    op.drop_table('doctor')
    op.drop_table('userdata')
    # ### end Alembic commands ###
