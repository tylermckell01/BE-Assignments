import { useState } from "react";

export default function NewWorkoutForm() {
  const [formData, setFormData] = useState({
    workout_name: "",
    workout_description: "",
    workout_length: "",
    gym_name: "",
  });

  const handleFieldUpdate = (e) => {
    const { name, value } = e.target;

    setFormData((previous) => ({ ...previous, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("you submitted correctly, now wire it up to your BE!!");
  };

  return (
    <div className="new-workout-form-container">
      <div className="page-title">new workout form</div>
      <form onSubmit={handleSubmit}>
        <div className="new-workout-form">
          <label htmlFor="workout-name">workout name </label>
          <input
            id="workout-name"
            name="workout_name"
            value={formData.workout_name}
            type="text"
            className="workout-name"
            onChange={handleFieldUpdate}
          />

          <label htmlFor="workout-description">workout description</label>
          <input
            id="workout-description"
            name="workout_description"
            value={formData.workout_description}
            type="text"
            className="workout-description"
            onChange={handleFieldUpdate}
          />

          <label htmlFor="workout-length">workout length</label>
          <input
            id="workout-length"
            name="workout_length"
            value={formData.workout_length}
            type="text"
            className="workout-length"
            onChange={handleFieldUpdate}
          />

          <label htmlFor="gym-name">gym name</label>
          <input
            id="gym-name"
            name="gym_name"
            value={formData.gym_name}
            type="text"
            className="gym-name"
            onChange={handleFieldUpdate}
          />
          <button type="submit">Add this workout!</button>
        </div>
      </form>
    </div>
  );
}
