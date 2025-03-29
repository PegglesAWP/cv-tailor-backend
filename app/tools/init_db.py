from app.database import Base, engine
from app.models import User, Experience, Education, Achievement, Document, Employer
from app.auth import get_password_hash, generate_uuid
from datetime import datetime, timedelta

def init_db():
    """
    Initialize the database with tables and sample data for testing.
    """
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    print("Database tables created!")

def create_sample_data(db_session):
    """
    Create sample data for testing purposes.
    """
    # Create sample user
    user_id = generate_uuid()
    sample_user = User(
        id=user_id,
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        first_name="John",
        last_name="Doe",
        phone="+61412345678",
        subscription_status="free",
        is_active=True,
        is_verified=True
    )
    db_session.add(sample_user)
    
    # Create sample experiences
    exp1_id = generate_uuid()
    experience1 = Experience(
        id=exp1_id,
        user_id=user_id,
        company_name="Tech Solutions Pty Ltd",
        job_title="Software Developer",
        start_date=datetime.now() - timedelta(days=365),
        end_date=None,
        is_current=True,
        location="Melbourne, Australia",
        description="Developed web applications using React and Python."
    )
    db_session.add(experience1)
    
    exp2_id = generate_uuid()
    experience2 = Experience(
        id=exp2_id,
        user_id=user_id,
        company_name="Data Analytics Co",
        job_title="Junior Developer",
        start_date=datetime.now() - timedelta(days=730),
        end_date=datetime.now() - timedelta(days=366),
        is_current=False,
        location="Sydney, Australia",
        description="Created data visualizations and reports using SQL and Python."
    )
    db_session.add(experience2)
    
    # Create sample education
    edu_id = generate_uuid()
    education = Education(
        id=edu_id,
        user_id=user_id,
        institution="University of Melbourne",
        degree="Bachelor of Computer Science",
        field_of_study="Computer Science",
        start_date=datetime.now() - timedelta(days=1460),
        end_date=datetime.now() - timedelta(days=730),
        is_current=False,
        location="Melbourne, Australia",
        description="Studied algorithms, data structures, and software engineering."
    )
    db_session.add(education)
    
    # Create sample achievement
    achievement_id = generate_uuid()
    achievement = Achievement(
        id=achievement_id,
        user_id=user_id,
        title="Best Student Project Award",
        description="Won the best student project award for developing an innovative mobile application.",
        date=datetime.now() - timedelta(days=800)
    )
    db_session.add(achievement)
    
    # Create sample document
    document_id = generate_uuid()
    document = Document(
        id=document_id,
        user_id=user_id,
        title="My Software Developer CV",
        content="This is a sample CV content",
        document_type="cv",
        employer_name="Google Australia",
        job_title="Software Engineer"
    )
    db_session.add(document)
    
    # Create sample employers
    employer1_id = generate_uuid()
    employer1 = Employer(
        id=employer1_id,
        name="Google Australia",
        website="https://www.google.com.au",
        industry="Technology",
        description="Google is a multinational technology company.",
        values=["innovation", "diversity", "inclusion"],
        keywords=["technology", "search", "ads", "software"]
    )
    db_session.add(employer1)
    
    employer2_id = generate_uuid()
    employer2 = Employer(
        id=employer2_id,
        name="Commonwealth Bank",
        website="https://www.commbank.com.au",
        industry="Banking & Finance",
        description="Commonwealth Bank is one of Australia's leading financial institutions.",
        values=["integrity", "accountability", "service"],
        keywords=["banking", "finance", "technology", "customer service"]
    )
    db_session.add(employer2)
    
    # Commit all changes
    db_session.commit()
    
    print("Sample data created!")
    print(f"Sample user: email=test@example.com, password=password123")

if __name__ == "__main__":
    init_db()
    
    # Uncomment to create sample data
    # from app.database import SessionLocal
    # db = SessionLocal()
    # try:
    #     create_sample_data(db)
    # finally:
    #     db.close()