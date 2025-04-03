from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from ..database.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    pcap_files = relationship("PCAPFile", back_populates="user")

class PCAPFile(Base):
    __tablename__ = "pcap_files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255), nullable=False)
    file_size = Column(BigInteger, nullable=False)
    upload_date = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String(50), default="pending")
    file_metadata = Column(JSON)
    analysis_results = Column(JSON)

    user = relationship("User", back_populates="pcap_files")
    analysis = relationship("AnalysisResult", back_populates="pcap_file")
    alerts = relationship("Alert", back_populates="pcap_file")

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pcap_file_id = Column(UUID(as_uuid=True), ForeignKey("pcap_files.id"))
    analysis_type = Column(String(50), nullable=False)
    result_data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    pcap_file = relationship("PCAPFile", back_populates="analysis")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pcap_file_id = Column(UUID(as_uuid=True), ForeignKey("pcap_files.id"))
    alert_type = Column(String(50), nullable=False)
    severity = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    alert_metadata = Column(JSON)

    pcap_file = relationship("PCAPFile", back_populates="alerts") 