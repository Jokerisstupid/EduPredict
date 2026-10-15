"""
EduPredict - Comprehensive Database Seeder
"""
import os
from pymongo import MongoClient
from datetime import datetime
import random
import bcrypt

client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017"))
db = client[os.environ.get("DB_NAME", "EduPredict")]

print("=" * 60)
print("  EduPredict - Full Database Seeder")
print("=" * 60)

print("\nClearing old data...")
for col in db.list_collection_names():
    if col == "counters":
        continue
    db[col].drop()
print("  All collections cleared.")

random.seed(42)

admin_pw = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt())
teacher_pw = bcrypt.hashpw("teacher123".encode("utf-8"), bcrypt.gensalt())
analyst_pw = bcrypt.hashpw("analyst123".encode("utf-8"), bcrypt.gensalt())
student_pw = bcrypt.hashpw("student123".encode("utf-8"), bcrypt.gensalt())

# ============================================================
# USERS
# ============================================================
print("\n[1/12] Seeding users...")
users_col = db["users"]

teachers_list = [
    {"email": "Teacher.ep9@gmail.com", "name": "Dr. Ayesha Khan", "created_at": "2025-11-10"},
    {"email": "Prof.Ali.ep9@gmail.com", "name": "Prof. Ali Raza", "created_at": "2025-11-12"},
    {"email": "Dr.Sara.ep9@gmail.com", "name": "Dr. Sara Malik", "created_at": "2025-12-01"},
    {"email": "Dr.Imran.ep9@gmail.com", "name": "Dr. Imran Shah", "created_at": "2026-01-05"},
]

analysts_list = [
    {"email": "Analyst.ep9@gmail.com", "name": "Hamza Tariq", "created_at": "2025-12-15"},
    {"email": "Lead.Analyst.ep9@gmail.com", "name": "Lead Data Analyst", "created_at": "2026-01-10"},
]

student_data = [
    ("Ahmed Khan", "Ahmed.Khan.ep9@gmail.com"),
    ("Fatima Ali", "Fatima.Ali.ep9@gmail.com"),
    ("Hassan Raza", "Hassan.Raza.ep9@gmail.com"),
    ("Zainab Malik", "Zainab.Malik.ep9@gmail.com"),
    ("Omar Farooq", "Omar.Farooq.ep9@gmail.com"),
    ("Amina Siddiqui", "Amina.Siddiqui.ep9@gmail.com"),
    ("Bilal Ahmed", "Bilal.Ahmed.ep9@gmail.com"),
    ("Noor Hassan", "Noor.Hassan.ep9@gmail.com"),
    ("Ali Hamza", "Ali.Hamza.ep9@gmail.com"),
    ("Sana Bibi", "Sana.Bibi.ep9@gmail.com"),
    ("Usman Ghani", "Usman.Ghani.ep9@gmail.com"),
    ("Maryam Noor", "Maryam.Noor.ep9@gmail.com"),
    ("Kamran Shah", "Kamran.Shah.ep9@gmail.com"),
    ("Hira Khan", "Hira.Khan.ep9@gmail.com"),
    ("Talha Mehmood", "Talha.Mehmood.ep9@gmail.com"),
    ("Rabia Aslam", "Rabia.Aslam.ep9@gmail.com"),
    ("Faisal Qureshi", "Faisal.Qureshi.ep9@gmail.com"),
    ("Mehwish Sheikh", "Mehwish.Sheikh.ep9@gmail.com"),
    ("Saad Ali", "Saad.Ali.ep9@gmail.com"),
    ("Iqra Javed", "Iqra.Javed.ep9@gmail.com"),
    ("Danish Rehman", "Danish.Rehman.ep9@gmail.com"),
    ("Ayesha Siddiqa", "Ayesha.Siddiqa.ep9@gmail.com"),
    ("Imran Khan", "Imran.Khan.ep9@gmail.com"),
    ("Nadia Parveen", "Nadia.Parveen.ep9@gmail.com"),
    ("Shahid Afridi", "Shahid.Afridi.ep9@gmail.com"),
    ("Rukhsana Bibi", "Rukhsana.Bibi.ep9@gmail.com"),
    ("Waqas Ahmed", "Waqas.Ahmed.ep9@gmail.com"),
    ("Sobia Malik", "Sobia.Malik.ep9@gmail.com"),
    ("Adnan Khan", "Adnan.Khan.ep9@gmail.com"),
    ("Bushra Bibi", "Bushra.Bibi.ep9@gmail.com"),
    ("Kashif Raza", "Kashif.Raza.ep9@gmail.com"),
    ("Saima Akhtar", "Saima.Akhtar.ep9@gmail.com"),
    ("Tariq Mahmood", "Tariq.Mahmood.ep9@gmail.com"),
    ("Zara Hussain", "Zara.Hussain.ep9@gmail.com"),
    ("Naeem Shah", "Naeem.Shah.ep9@gmail.com"),
    ("Farah Naz", "Farah.Naz.ep9@gmail.com"),
    ("Asif Javed", "Asif.Javed.ep9@gmail.com"),
    ("Samina Bibi", "Samina.Bibi.ep9@gmail.com"),
    ("Rashid Minhas", "Rashid.Minhas.ep9@gmail.com"),
    ("Nasreen Akhter", "Nasreen.Akhter.ep9@gmail.com"),
]

seen_emails = set()
unique_students = []
for name, email in student_data:
    if email not in seen_emails:
        seen_emails.add(email)
        unique_students.append((name, email))
student_data = unique_students

user_ids = {}

users_col.insert_one({
    "id": 1, "email": "admin@gmail.com", "password": admin_pw,
    "name": "Admin User", "role": "administrator",
    "created_at": "2025-10-01T00:00:00", "is_active": 1
})
user_ids["admin@gmail.com"] = 1

users_col.insert_one({
    "id": 2, "email": "Admin.ep9@gmail.com", "password": admin_pw,
    "name": "System Administrator", "role": "administrator",
    "created_at": "2025-10-05T00:00:00", "is_active": 1
})
user_ids["Admin.ep9@gmail.com"] = 2

for i, t in enumerate(teachers_list):
    uid = i + 3
    users_col.insert_one({
        "id": uid, "email": t["email"], "password": teacher_pw,
        "name": t["name"], "role": "teacher",
        "created_at": t["created_at"], "is_active": 1
    })
    user_ids[t["email"]] = uid

teacher_end_id = len(teachers_list) + 2

for i, a in enumerate(analysts_list):
    uid = teacher_end_id + i + 1
    users_col.insert_one({
        "id": uid, "email": a["email"], "password": analyst_pw,
        "name": a["name"], "role": "analyst",
        "created_at": a["created_at"], "is_active": 1
    })
    user_ids[a["email"]] = uid

analyst_end_id = teacher_end_id + len(analysts_list)

student_ids = []
for i, (name, email) in enumerate(student_data):
    uid = analyst_end_id + i + 1
    users_col.insert_one({
        "id": uid, "email": email, "password": student_pw,
        "name": name, "role": "student",
        "created_at": "2026-01-15", "is_active": 1
    })
    user_ids[email] = uid
    student_ids.append(uid)

print("  Inserted: 2 admins, %d teachers, %d analysts, %d students" % (len(teachers_list), len(analysts_list), len(student_ids)))

# ============================================================
# BATCHES
# ============================================================
print("\n[2/12] Seeding batches...")
batches_col = db["batches"]
batch_data = [
    {"id": 1, "name": "ADSE-2509-BigData", "teacher_id": user_ids["Teacher.ep9@gmail.com"], "created_at": "2025-11-20"},
    {"id": 2, "name": "ADSE-2510-CloudComputing", "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "created_at": "2025-12-01"},
    {"id": 3, "name": "ADSE-2601-MachineLearning", "teacher_id": user_ids["Dr.Sara.ep9@gmail.com"], "created_at": "2026-01-10"},
    {"id": 4, "name": "ADSE-2602-DataAnalytics", "teacher_id": user_ids["Dr.Imran.ep9@gmail.com"], "created_at": "2026-02-01"},
    {"id": 5, "name": "BSCS-2509-DataStructures", "teacher_id": user_ids["Teacher.ep9@gmail.com"], "created_at": "2025-11-25"},
    {"id": 6, "name": "BSCS-2601-AI-Fundamentals", "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "created_at": "2026-01-15"},
]
batches_col.insert_many(batch_data)
print("  Inserted %d batches" % len(batch_data))

# ============================================================
# STUDENT_BATCHES
# ============================================================
print("\n[3/12] Assigning students to batches...")
student_batches_col = db["student_batches"]
sb_data = []
for i, sid in enumerate(student_ids):
    batch_id = (i % 6) + 1
    sb_data.append({"student_id": sid, "batch_id": batch_id})
student_batches_col.insert_many(sb_data)
print("  Assigned %d student-batch mappings" % len(sb_data))

# ============================================================
# ASSIGNMENTS
# ============================================================
print("\n[4/12] Seeding assignments...")
assignments_col = db["assignments"]
assignment_data = [
    {"id": 1, "batch_id": 1, "teacher_id": user_ids["Teacher.ep9@gmail.com"], "title": "MapReduce Word Count Implementation", "subject": "Big Data Analytics", "total_marks": 100, "due_date": "2026-03-15", "created_at": "2026-03-01"},
    {"id": 2, "batch_id": 1, "teacher_id": user_ids["Teacher.ep9@gmail.com"], "title": "HDFS Cluster Configuration Lab", "subject": "Big Data Analytics", "total_marks": 50, "due_date": "2026-03-20", "created_at": "2026-03-05"},
    {"id": 3, "batch_id": 2, "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "title": "AWS EC2 Instance Deployment", "subject": "Cloud Computing", "total_marks": 80, "due_date": "2026-03-10", "created_at": "2026-03-02"},
    {"id": 4, "batch_id": 2, "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "title": "Docker Container Orchestration", "subject": "Cloud Computing", "total_marks": 120, "due_date": "2026-04-30", "created_at": "2026-03-10"},
    {"id": 5, "batch_id": 3, "teacher_id": user_ids["Dr.Sara.ep9@gmail.com"], "title": "Random Forest Model Evaluation", "subject": "Machine Learning", "total_marks": 100, "due_date": "2026-04-01", "created_at": "2026-03-15"},
    {"id": 6, "batch_id": 3, "teacher_id": user_ids["Dr.Sara.ep9@gmail.com"], "title": "Neural Network Backpropagation", "subject": "Machine Learning", "total_marks": 150, "due_date": "2026-04-15", "created_at": "2026-03-20"},
    {"id": 7, "batch_id": 4, "teacher_id": user_ids["Dr.Imran.ep9@gmail.com"], "title": "SQL Aggregation and Pivot Queries", "subject": "Data Analytics", "total_marks": 75, "due_date": "2026-03-25", "created_at": "2026-03-12"},
    {"id": 8, "batch_id": 4, "teacher_id": user_ids["Dr.Imran.ep9@gmail.com"], "title": "Power BI Dashboard Project", "subject": "Data Analytics", "total_marks": 100, "due_date": "2026-04-20", "created_at": "2026-03-18"},
    {"id": 9, "batch_id": 5, "teacher_id": user_ids["Teacher.ep9@gmail.com"], "title": "Binary Tree Traversal Algorithms", "subject": "Data Structures", "total_marks": 100, "due_date": "2026-03-28", "created_at": "2026-03-10"},
    {"id": 10, "batch_id": 5, "teacher_id": user_ids["Teacher.ep9@gmail.com"], "title": "Graph Shortest Path Implementation", "subject": "Data Structures", "total_marks": 80, "due_date": "2026-04-10", "created_at": "2026-03-22"},
    {"id": 11, "batch_id": 6, "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "title": "Convolutional Neural Network Lab", "subject": "AI Fundamentals", "total_marks": 120, "due_date": "2026-04-05", "created_at": "2026-03-16"},
    {"id": 12, "batch_id": 6, "teacher_id": user_ids["Prof.Ali.ep9@gmail.com"], "title": "Reinforcement Learning Maze Solver", "subject": "AI Fundamentals", "total_marks": 100, "due_date": "2026-04-25", "created_at": "2026-03-25"},
]
assignments_col.insert_many(assignment_data)
print("  Inserted %d assignments" % len(assignment_data))

# ============================================================
# STUDENT_MARKS
# ============================================================
print("\n[5/12] Seeding student marks...")
student_marks_col = db["student_marks"]
marks_data = []
feedbacks = [
    "Good work overall.", "Needs improvement in key areas.",
    "Excellent understanding of concepts.", "Average performance.",
    "Strong analytical approach.", "Late submission penalty applied.",
    "Well-structured solution.", "Incomplete implementation.",
    "Outstanding effort!", "Meets baseline requirements."
]
for aid_info in assignment_data:
    aid = aid_info["id"]
    batch_id = aid_info["batch_id"]
    total = aid_info["total_marks"]
    batch_sids = [sb["student_id"] for sb in sb_data if sb["batch_id"] == batch_id]
    for sid in batch_sids[:15]:
        pct = random.uniform(0.25, 1.0)
        obtained = int(total * pct)
        marks_data.append({
            "student_id": sid,
            "assignment_id": aid,
            "obtained_marks": obtained,
            "status": "graded",
            "feedback": random.choice(feedbacks),
            "graded_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })
student_marks_col.insert_many(marks_data)
print("  Inserted %d marks records" % len(marks_data))

# ============================================================
# EDUCATIONAL RECORDS (HDFS Records tab)
# ============================================================
print("\n[6/12] Seeding educational records (HDFS)...")
edu_records_col = db["educational_records"]
records = []
for idx, sid in enumerate(student_ids):
    name = student_data[idx][0]
    attendance = max(20, min(100, round(random.gauss(72, 18), 1)))
    marks = max(15, min(100, round(random.gauss(68, 20), 1)))
    lms = max(10, min(100, round(random.gauss(60, 22), 1)))
    prev = max(20, min(100, round(random.gauss(70, 16), 1)))
    avg = (attendance + marks + lms + prev) / 4
    if avg >= 75:
        risk = "Low"
    elif avg >= 55:
        risk = "Medium"
    else:
        risk = "High"
    records.append({
        "student_id": str(sid),
        "student_name": name,
        "attendance": attendance,
        "marks": marks,
        "lms_activity": lms,
        "previous_performance": prev,
        "risk": risk,
        "created_at": datetime(2026, random.randint(1, 6), random.randint(1, 28)).isoformat()
    })
edu_records_col.insert_many(records)
print("  Inserted %d educational records" % len(records))

# ============================================================
# PREDICTIONS
# ============================================================
print("\n[7/12] Seeding predictions...")
predictions_col = db["predictions"]
preds = []
for rec in records:
    grade = random.choices(["A", "B", "C", "D", "F"], weights=[15, 35, 30, 15, 5])[0]
    preds.append({
        "student_id": rec["student_id"],
        "student_name": rec["student_name"],
        "attendance": rec["attendance"],
        "marks": rec["marks"],
        "lms_activity": rec["lms_activity"],
        "previous_performance": rec["previous_performance"],
        "risk": rec["risk"],
        "confidence": round(random.uniform(0.65, 0.98), 4),
        "predicted_grade": grade,
        "predicted_at": rec["created_at"],
        "analyzed_by": "Analyst.ep9@gmail.com"
    })
predictions_col.insert_many(preds)
print("  Inserted %d predictions" % len(preds))

# ============================================================
# ALERTS
# ============================================================
print("\n[8/12] Seeding alerts...")
alerts_col = db["alerts"]
alerts = []
alert_types = ["Academic Risk", "Attendance Anomaly", "Grade Degradation", "LMS Inactivity", "Dropout Warning"]

for rec in records:
    if rec["risk"] == "High":
        alerts.append({
            "student_id": rec["student_id"],
            "student_name": rec["student_name"],
            "alert_type": random.choice(alert_types[:3]),
            "message": "High-risk student detected: %s - Attendance: %s%%, Marks: %s%%" % (rec["student_name"], rec["attendance"], rec["marks"]),
            "severity": random.choice(["High", "Critical"]),
            "status": random.choice(["New", "pending"]),
            "metric_value": "%s%%" % rec["attendance"],
            "created_at": rec["created_at"]
        })
    elif rec["risk"] == "Medium":
        alerts.append({
            "student_id": rec["student_id"],
            "student_name": rec["student_name"],
            "alert_type": random.choice(alert_types),
            "message": "Medium-risk alert for %s - Performance below threshold" % rec["student_name"],
            "severity": "Medium",
            "status": random.choice(["New", "acknowledged"]),
            "metric_value": "%s%%" % rec["marks"],
            "created_at": rec["created_at"]
        })

alerts_col.insert_many(alerts)
print("  Inserted %d baseline alerts" % len(alerts))

# Now generate proper alerts from actual educational records data
print("  Generating detailed alerts from student records...")
predictions_col = db["predictions"]
detailed_alerts = []
for idx, sid in enumerate(student_ids):
    name = student_data[idx][0]
    rec = records[idx]
    attendance = rec["attendance"]
    marks_val = rec["marks"]
    lms_val = rec["lms_activity"]
    risk_level = rec["risk"]
    pred = preds[idx]
    predicted_grade = pred["predicted_grade"]
    confidence = pred["confidence"]

    # Attendance Anomaly
    if attendance < 75.0:
        detailed_alerts.append({
            "alert_type": "Attendance Anomaly",
            "severity": "critical" if attendance < 60.0 else "high",
            "status": "New" if attendance < 60.0 else "pending",
            "message": "%s attendance dropped to %.1f%%, below institutional policy threshold (75%%). Current risk level: %s." % (name, attendance, risk_level),
            "student_id": str(sid),
            "student_name": name,
            "metric_value": "%.1f%%" % attendance,
            "created_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })

    # Grade Degradation
    if marks_val < 50.0:
        detailed_alerts.append({
            "alert_type": "Grade Degradation",
            "severity": "high",
            "status": "pending",
            "message": "%s mean coursework grade dropped to %.1f%%. Remedial support and faculty intervention advised." % (name, marks_val),
            "student_id": str(sid),
            "student_name": name,
            "metric_value": "%.1f%%" % marks_val,
            "created_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })

    # LMS Inactivity
    if lms_val < 40.0:
        detailed_alerts.append({
            "alert_type": "LMS Inactivity",
            "severity": "medium",
            "status": "New",
            "message": "%s LMS engagement score is only %.1f%% - platform disengagement detected." % (name, lms_val),
            "student_id": str(sid),
            "student_name": name,
            "metric_value": "%.1f%%" % lms_val,
            "created_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })

    # Dropout Warning (High Risk)
    if risk_level == "High":
        detailed_alerts.append({
            "alert_type": "Dropout Warning",
            "severity": "critical",
            "status": "New",
            "message": "Dropout probability elevated for %s (Predicted Grade: %s, Confidence: %.0f%%). Attendance: %.1f%%, Marks: %.1f%%, LMS: %.1f%%. Immediate advisor outreach required." % (name, predicted_grade, confidence * 100, attendance, marks_val, lms_val),
            "student_id": str(sid),
            "student_name": name,
            "metric_value": "%.0f%%" % (confidence * 100),
            "created_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })

    # Academic Risk (Medium Risk with low marks)
    if risk_level == "Medium" and marks_val < 55.0:
        detailed_alerts.append({
            "alert_type": "Academic Risk",
            "severity": "medium",
            "status": "pending",
            "message": "%s showing medium academic risk - marks at %.1f%% with %.1f%% attendance. Performance trajectory trending downward." % (name, marks_val, attendance),
            "student_id": str(sid),
            "student_name": name,
            "metric_value": "%.1f%%" % marks_val,
            "created_at": datetime(2026, random.randint(3, 5), random.randint(1, 28)).isoformat()
        })

if detailed_alerts:
    alerts_col.insert_many(detailed_alerts)
print("  Generated %d detailed student-specific alerts" % len(detailed_alerts))

# ============================================================
# SYSTEM LOGS
# ============================================================
print("\n[9/12] Seeding system logs...")
logs_col = db["system_logs"]
logs = [
    {"event": "System Start", "details": "EduPredict Big Data Analytics Engine initialized", "created_at": "2025-10-01T08:00:00"},
    {"event": "Database Connected", "details": "MongoDB cluster connection established on port 27017", "created_at": "2025-10-01T08:00:01"},
    {"event": "HDFS Node Online", "details": "HDFS ingestion partition mounted and ready", "created_at": "2025-10-01T08:00:02"},
    {"event": "Data Import", "details": "Imported 40 initial student records from CSV partition", "created_at": "2025-11-15T10:30:00"},
    {"event": "Model Training", "details": "ML Risk Classification model retrained with 3000 samples - Accuracy: 92.4%", "created_at": "2026-01-15T14:20:00"},
    {"event": "Batch Created", "details": "Created 6 academic cohort partitions", "created_at": "2026-01-20T09:00:00"},
    {"event": "SMTP Daemon Started", "details": "Email alert notification daemon synchronized with Report Generator", "created_at": "2026-02-01T08:30:00"},
    {"event": "User Login", "details": "admin@gmail.com authenticated with role clearance: administrator", "created_at": "2026-03-01T09:00:00"},
    {"event": "Dataset Uploaded", "details": "student_performance_dataset.csv uploaded - 500 rows, 12 columns", "created_at": "2026-03-05T11:15:00"},
    {"event": "Batch Prediction", "details": "Batch risk assessment completed for 40 students", "created_at": "2026-03-10T16:00:00"},
    {"event": "Alert Generated", "details": "High-risk alerts triggered for 8 students", "created_at": "2026-03-10T16:05:00"},
    {"event": "Report Generated", "details": "Student Risk Audit Report compiled and queued for dispatch", "created_at": "2026-03-12T15:44:00"},
    {"event": "Model Retrained", "details": "Grade Prediction model updated with Spring 2026 cohort data", "created_at": "2026-04-01T10:00:00"},
    {"event": "User Login", "details": "analyst@edupredict.com authenticated with role clearance: analyst", "created_at": "2026-04-05T09:30:00"},
    {"event": "Anomaly Detection", "details": "Statistical anomaly scan detected 3 attendance deviations", "created_at": "2026-04-10T14:00:00"},
    {"event": "Email Dispatch", "details": "Risk alert emails dispatched to 5 faculty instructors", "created_at": "2026-04-12T11:00:00"},
    {"event": "System Health", "details": "All cluster nodes operational - Memory: 78%, CPU: 45%, Disk: 62%", "created_at": "2026-05-01T08:00:00"},
    {"event": "Backup Completed", "details": "Full database backup exported to backups/ directory", "created_at": "2026-05-15T23:00:00"},
]
logs_col.insert_many(logs)
print("  Inserted %d system logs" % len(logs))

# ============================================================
# DATASETS (HDFS Partition Store)
# ============================================================
print("\n[10/12] Seeding datasets...")
datasets_col = db["datasets"]
dataset_data = [
    {
        "id": 1, "name": "student_performance_dataset.csv",
        "filename": "student_performance_dataset.csv",
        "file_path": "uploads/student_performance_dataset.csv",
        "uploaded_by": 1, "row_count": 500, "total_records": 500,
        "column_count": 12,
        "columns": ["name", "attendance", "marks", "lms_activity", "previous_performance", "study_hours", "assignment_score", "exam_score", "participation", "age", "gender", "risk_level"],
        "uploaded_at": "2026-03-05T11:15:00"
    },
    {
        "id": 2, "name": "batch_enrollment_records.csv",
        "filename": "batch_enrollment_records.csv",
        "file_path": "uploads/batch_enrollment_records.csv",
        "uploaded_by": 4, "row_count": 320, "total_records": 320,
        "column_count": 8,
        "columns": ["student_id", "batch_id", "enrollment_date", "semester", "status", "gpa", "credit_hours", "advisor"],
        "uploaded_at": "2026-03-18T14:30:00"
    },
    {
        "id": 3, "name": "attendance_log_2026_spring.csv",
        "filename": "attendance_log_2026_spring.csv",
        "file_path": "uploads/attendance_log_2026_spring.csv",
        "uploaded_by": 1, "row_count": 1200, "total_records": 1200,
        "column_count": 6,
        "columns": ["student_id", "date", "status", "course", "batch", "timestamp"],
        "uploaded_at": "2026-04-02T09:00:00"
    },
]
datasets_col.insert_many(dataset_data)
print("  Inserted %d datasets" % len(dataset_data))

# ============================================================
# DATASET MAPPINGS
# ============================================================
print("\n[11/12] Seeding dataset mappings...")
dataset_mappings_col = db["dataset_mappings"]
mappings = [
    {
        "dataset_id": 1,
        "x_columns": '["attendance", "marks", "lms_activity", "previous_performance", "study_hours"]',
        "y_column": "risk_level",
        "model_type": "Classification",
        "score": 0.9240,
        "created_at": "2026-03-06T10:00:00"
    },
    {
        "dataset_id": 1,
        "x_columns": '["attendance", "assignment_score", "participation"]',
        "y_column": "exam_score",
        "model_type": "Regression",
        "score": 0.8573,
        "created_at": "2026-03-07T14:30:00"
    },
    {
        "dataset_id": 3,
        "x_columns": '["student_id", "course", "batch"]',
        "y_column": "status",
        "model_type": "Classification",
        "score": 0.7856,
        "created_at": "2026-04-03T11:00:00"
    },
]
dataset_mappings_col.insert_many(mappings)
print("  Inserted %d dataset mappings" % len(mappings))

# ============================================================
# REPORTS
# ============================================================
print("\n[12/12] Seeding reports...")
reports_col = db["reports"]
report_data = [
    {
        "id": 1, "name": "report_student_risk_20260312_154411.csv",
        "title": "EduPredict Student Risk Audit Report - Spring 2026",
        "type": "student_risk",
        "notes": "Comprehensive risk assessment for all enrolled students",
        "file_path": "static/reports/report_student_risk_20260312_154411.csv",
        "created_by": 1, "created_by_name": "Admin User",
        "created_at": "2026-03-12 15:44:11"
    },
    {
        "id": 2, "name": "report_course_demand_20260401_090000.csv",
        "title": "Course Demand Projection - Summer 2026",
        "type": "course_demand",
        "notes": "Enrollment demand forecast for upcoming semester",
        "file_path": "static/reports/report_course_demand_20260401_090000.csv",
        "created_by": 4, "created_by_name": "Hamza Tariq",
        "created_at": "2026-04-01 09:00:00"
    },
    {
        "id": 3, "name": "report_anomaly_summary_20260410_140000.csv",
        "title": "Anomaly Detection Summary - April 2026",
        "type": "anomaly_summary",
        "notes": "Statistical anomalies detected in attendance and grade patterns",
        "file_path": "static/reports/report_anomaly_summary_20260410_140000.csv",
        "created_by": 4, "created_by_name": "Hamza Tariq",
        "created_at": "2026-04-10 14:00:00"
    },
    {
        "id": 4, "name": "report_retention_analysis_20260501_110000.csv",
        "title": "Student Retention and Dropout Analysis",
        "type": "student_risk",
        "notes": "Dropout risk factors and retention strategy recommendations",
        "file_path": "static/reports/report_retention_analysis_20260501_110000.csv",
        "created_by": 1, "created_by_name": "Admin User",
        "created_at": "2026-05-01 11:00:00"
    },
    {
        "id": 5, "name": "report_ml_model_performance_20260515_160000.csv",
        "title": "ML Model Performance Benchmark",
        "type": "anomaly_summary",
        "notes": "Random Forest and Ridge regression model evaluation metrics",
        "file_path": "static/reports/report_ml_model_performance_20260515_160000.csv",
        "created_by": 4, "created_by_name": "Lead Data Analyst",
        "created_at": "2026-05-15 16:00:00"
    },
]
reports_col.insert_many(report_data)
print("  Inserted %d reports" % len(report_data))

# Materialize report CSV files on disk so send-mail dispatch attaches real data
import csv as _csv
from pymongo import MongoClient as _MC
_reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "reports")
os.makedirs(_reports_dir, exist_ok=True)
for _r in report_data:
    _fp = os.path.join(_reports_dir, _r["name"])
    _rtype = _r.get("type", "student_risk")
    _rows = []
    if _rtype == "student_risk":
        _fields = ["student_id", "student_name", "attendance", "marks", "lms_activity", "risk"]
        for _rec in db["educational_records"].find().sort("student_id", 1).limit(40):
            _st = db["users"].find_one({"id": _rec.get("student_id")})
            _risk = _rec.get("risk")
            _label = "High Risk" if _risk == "High" else ("Low Risk" if _risk == "Low" else "Medium Risk")
            _rows.append([_rec.get("student_id"), (_st or {}).get("name", "Student"), _rec.get("attendance"), _rec.get("marks"), _rec.get("lms_activity"), _label])
    elif _rtype == "course_demand":
        _fields = ["course", "demand_score", "trend"]
        for _a in db["assignments"].find().sort("id", 1).limit(40):
            _b = db["batches"].find_one({"id": _a.get("batch_id")})
            _rows.append([(_b or {}).get("name", "Course"), 90 - _a["id"] * 3, "up" if _a["id"] % 2 == 0 else "down"])
    else:
        _fields = ["student_id", "student_name", "alert_type", "severity", "status"]
        for _al in db["alerts"].find().sort("_id", 1).limit(40):
            _st = db["users"].find_one({"id": _al.get("student_id")})
            _rows.append([_al.get("student_id"), _al.get("student_name", (_st or {}).get("name", "Student")), _al.get("alert_type", _al.get("type")), _al.get("severity"), _al.get("status")])
    with open(_fp, "w", newline="", encoding="utf-8") as _f:
        _w = _csv.writer(_f)
        _w.writerow(_fields)
        _w.writerows(_rows)
    db["reports"].update_one({"id": _r["id"]}, {"$set": {"file_path": _fp}})
print("  Materialized %d report CSV files on disk" % len(report_data))

# ============================================================
# COUNTERS
# ============================================================
print("\nSetting up ID counters...")
counters_col = db["counters"]
counters_col.drop()
counters_col.insert_many([
    {"_id": "users", "seq": analyst_end_id + len(student_data)},
    {"_id": "batches", "seq": len(batch_data)},
    {"_id": "assignments", "seq": len(assignment_data)},
    {"_id": "datasets", "seq": len(dataset_data)},
    {"_id": "reports", "seq": len(report_data)},
])

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("  DATABASE SEEDED SUCCESSFULLY!")
print("=" * 60)
print("  Users:          %d" % users_col.count_documents({}))
print("    - Admin:      2")
print("    - Teachers:   %d" % len(teachers_list))
print("    - Analysts:   %d" % len(analysts_list))
print("    - Students:   %d" % len(student_ids))
print("  Batches:        %d" % batches_col.count_documents({}))
print("  Assignments:    %d" % assignments_col.count_documents({}))
print("  Student Marks:  %d" % student_marks_col.count_documents({}))
print("  Edu Records:    %d" % edu_records_col.count_documents({}))
print("  Predictions:    %d" % predictions_col.count_documents({}))
print("  Alerts:         %d" % alerts_col.count_documents({}))
print("  System Logs:    %d" % logs_col.count_documents({}))
print("  Datasets:       %d" % datasets_col.count_documents({}))
print("  Mappings:       %d" % dataset_mappings_col.count_documents({}))
print("  Reports:        %d" % reports_col.count_documents({}))
print("")
print("  Login Credentials (ALL REAL GMAIL):")
print("    Admin:    admin@gmail.com / admin123")
print("    Admin2:   Admin.ep9@gmail.com / admin123")
print("    Teacher:  Teacher.ep9@gmail.com / teacher123")
print("    Analyst:  Analyst.ep9@gmail.com / analyst123")
print("    Student:  Ahmed.Khan.ep9@gmail.com / student123")
print("=" * 60)

