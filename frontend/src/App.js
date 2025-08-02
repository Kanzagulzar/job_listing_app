import React, { useEffect, useState } from "react";
import axios from "axios";

const API = "http://localhost:5000/jobs";

function App() {
  const [jobs, setJobs] = useState([]);
  const [filters, setFilters] = useState({
    keyword: "",
    job_type: "All",
    location: "All",
  });

  const [availableLocations, setAvailableLocations] = useState([]);
  const [availableJobTypes, setAvailableJobTypes] = useState([]);

  const [form, setForm] = useState({
    title: "",
    company: "",
    location: "",
    job_type: "",
    tags: "",
  });

  const [successMessage, setSuccessMessage] = useState("");
  const [editId, setEditId] = useState(null); // <-- track editing job

  const fetchJobs = async () => {
    const res = await axios.get(API);
    setJobs(res.data);

    const locations = new Set();
    const types = new Set();

    res.data.forEach((job) => {
      locations.add(job.location);
      types.add(job.job_type || "N/A");
    });

    setAvailableLocations(["All", ...locations]);
    setAvailableJobTypes(["All", ...types]);
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  const handleFilterChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = { ...form, tags: form.tags.split(",") };

    if (editId) {
      await axios.put(`${API}/${editId}`, payload);
      setSuccessMessage("✅ Job updated.");
    } else {
      await axios.post(API, payload);
      setSuccessMessage("✅ Job added.");
    }

    setForm({ title: "", company: "", location: "", job_type: "", tags: "" });
    setEditId(null);
    fetchJobs();
    setTimeout(() => setSuccessMessage(""), 3000);
  };

  const handleEdit = (job) => {
    setEditId(job.id);
    setForm({
      title: job.title,
      company: job.company,
      location: job.location,
      job_type: job.job_type,
      tags: job.tags.join(","),
    });
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleDelete = async (id) => {
    if (window.confirm("Delete this job?")) {
      await axios.delete(`${API}/${id}`);
      setSuccessMessage("🗑️ Job deleted.");
      fetchJobs();
      setTimeout(() => setSuccessMessage(""), 3000);
    }
  };

  const matchesFilter = (job) => {
    const keyword = filters.keyword.toLowerCase();
    const titleMatch = job.title.toLowerCase().includes(keyword);
    const companyMatch = job.company.toLowerCase().includes(keyword);
    const jobTypeMatch = filters.job_type === "All" || job.job_type === filters.job_type;
    const locationMatch = filters.location === "All" || job.location === filters.location;
    return (titleMatch || companyMatch) && jobTypeMatch && locationMatch;
  };

  const filteredJobs = jobs.filter(matchesFilter);

  return (
    <div className="container">
      <style>{`
        body {
          font-family: 'Segoe UI', sans-serif;
          background: #f7fafc;
          margin: 0;
          padding: 0;
        }
        .container {
          max-width: 900px;
          margin: 40px auto;
          padding: 20px;
          background: white;
          border-radius: 12px;
          box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        }
        h1 {
          text-align: center;
          color: #2a4365;
        }
        input, select {
          width: 100%;
          padding: 10px;
          margin: 6px 0;
          border: 1px solid #ccc;
          border-radius: 8px;
          font-size: 14px;
        }
        button {
          padding: 10px 20px;
          background: #3182ce;
          color: white;
          border: none;
          border-radius: 8px;
          cursor: pointer;
          margin-top: 10px;
          margin-right: 10px;
        }
        button:hover {
          background: #2b6cb0;
        }
        .job-card {
          background: #edf2f7;
          padding: 15px;
          border-radius: 10px;
          margin-bottom: 20px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .tag {
          background: #3182ce;
          color: white;
          padding: 4px 10px;
          margin: 3px;
          border-radius: 20px;
          display: inline-block;
          font-size: 12px;
        }
        .filters {
          margin-bottom: 20px;
        }
        .success-message {
          background: #c6f6d5;
          color: #22543d;
          padding: 10px;
          border-radius: 8px;
          margin-bottom: 20px;
          font-weight: bold;
          text-align: center;
        }
      `}</style>

      <h1>{editId ? "✏️ Edit Job" : "🎯 Add Job"}</h1>

      {successMessage && <div className="success-message">{successMessage}</div>}

      <form onSubmit={handleSubmit}>
        <input name="title" value={form.title} onChange={handleChange} placeholder="Title" required />
        <input name="company" value={form.company} onChange={handleChange} placeholder="Company" required />
        <input name="location" value={form.location} onChange={handleChange} placeholder="Location" required />
        <input name="job_type" value={form.job_type} onChange={handleChange} placeholder="Job Type" />
        <input name="tags" value={form.tags} onChange={handleChange} placeholder="Tags (comma-separated)" />
        <button type="submit">{editId ? "Update Job" : "Add Job"}</button>
        {editId && (
          <button type="button" onClick={() => { setEditId(null); setForm({ title: "", company: "", location: "", job_type: "", tags: "" }); }}>
            Cancel
          </button>
        )}
      </form>

      <div className="filters">
        <input
          type="text"
          name="keyword"
          placeholder="🔍 Search by title or company"
          value={filters.keyword}
          onChange={handleFilterChange}
        />

        <select name="job_type" value={filters.job_type} onChange={handleFilterChange}>
          {availableJobTypes.map((type, idx) => (
            <option key={idx} value={type}>{type}</option>
          ))}
        </select>

        <select name="location" value={filters.location} onChange={handleFilterChange}>
          {availableLocations.map((loc, idx) => (
            <option key={idx} value={loc}>{loc}</option>
          ))}
        </select>
      </div>

      {filteredJobs.map((job) => (
        <div key={job.id} className="job-card">
          <h3>{job.title}</h3>
          <p>
            <strong>{job.company}</strong> — {job.location} ({job.job_type})
          </p>
          <p>📅 Posted on: {new Date(job.posting_date).toLocaleDateString()}</p>
          <div className="tags">
            {job.tags.map((tag, idx) => (
              <span key={idx} className="tag">{tag}</span>
            ))}
          </div>
          <button onClick={() => handleEdit(job)}>✏️ Edit</button>
          <button onClick={() => handleDelete(job.id)}>🗑️ Delete</button>
        </div>
      ))}

      {filteredJobs.length === 0 && <p>No jobs found matching your filters.</p>}
    </div>
  );
}

export default App;
