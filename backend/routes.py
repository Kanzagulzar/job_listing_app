from flask import Blueprint, request, jsonify
from models import db, Job
from sqlalchemy import desc, asc
from utils import parse_sort_param

api = Blueprint("api", __name__)

@api.route("/jobs", methods=["GET"])
def list_jobs():
    query = Job.query

    if job_type := request.args.get("job_type"):
        query = query.filter_by(job_type=job_type)

    if location := request.args.get("location"):
        query = query.filter(Job.location.ilike(f"%{location}%"))

    if tag := request.args.get("tag"):
        query = query.filter(Job.tags.ilike(f"%{tag}%"))

    if keyword := request.args.get("q"):
        query = query.filter(
            Job.title.ilike(f"%{keyword}%") | Job.company.ilike(f"%{keyword}%")
        )

    sort_param = request.args.get("sort")
    if sort_param:
        query = query.order_by(parse_sort_param(sort_param))
    else:
        query = query.order_by(desc(Job.posting_date))

    jobs = query.all()
    return jsonify([job.serialize() for job in jobs])


@api.route("/jobs", methods=["POST"])
def create_job():
    data = request.json
    required = ["title", "company", "location"]
    if not all(data.get(field) for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    job = Job(
        title=data["title"],
        company=data["company"],
        location=data["location"],
        posting_date=data.get("posting_date"),
        job_type=data.get("job_type"),
        tags=",".join(data.get("tags", [])),
    )
    db.session.add(job)
    db.session.commit()
    return jsonify(job.serialize()), 201


# @api.route("/jobs/<int:job_id>", methods=["PUT", "PATCH"])
# def update_job(job_id):
#     job = Job.query.get(job_id)
#     if not job:
#         return jsonify({"error": "Job not found"}), 404

#     data = request.json
#     for field in ["title", "company", "location", "job_type", "tags", "posting_date"]:
#         if field in data:
#             setattr(job, field, ",".join(data[field]) if field == "tags" else data[field])

#     db.session.commit()
#     return jsonify(job.serialize())


@api.route("/jobs/<int:id>", methods=["PUT"])
def update_job(id):
    job = Job.query.get_or_404(id)
    data = request.get_json()
    job.title = data["title"]
    job.company = data["company"]
    job.location = data["location"]
    job.job_type = data["job_type"]
    job.tags = ",".join(data["tags"])
    db.session.commit()
    return jsonify({"message": "Updated"}), 200


@api.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted"}), 200
