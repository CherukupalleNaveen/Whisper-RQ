from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Transcription(Base):
    __tablename__ = 'transcriptions'

    id = Column(String, primary_key=True)
    text = Column(String)

# Connect to the database
engine = create_engine('sqlite:///transcriptions.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Function to save transcription to the database
def save_transcription(request_id, transcription_text):
    transcription = Transcription(id=request_id, text=transcription_text)
    session.add(transcription)
    session.commit()

# Function to retrieve transcription from the database
def get_transcription(request_id):
    transcription = session.query(Transcription).filter_by(id=request_id).first()
    return transcription.text if transcription else None
