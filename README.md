# NodePipleine

**NodePipleine** is a dynamic pipeline builder and visualization tool. It allows users to create, connect, and manage nodes in a visual interface, with real-time updates and backend validation. This project demonstrates full-stack development skills using React for the frontend and FastAPI for the backend.

---

## Features

- **Node Abstraction:** Easily create multiple node types with shared logic and flexible styling.
- **Dynamic Node Connections:** Connect input, output, and text nodes to form pipelines.
- **Text Node Variables:** Define variables in text nodes to dynamically create input handles.
- **Responsive Node Layout:** Nodes automatically adjust size based on content.
- **Pipeline Validation:** Backend validates nodes and edges, checks for directed acyclic graph (DAG) structure.
- **Professional Modal Display:** Dark-themed modal displays node/edge count and DAG status in a clear, user-friendly format.
- **Frontend-Backend Integration:** Full communication between React frontend and FastAPI backend.

---

## Tech Stack

- **Frontend:** React, JavaScript, CSS
- **Backend:** Python, FastAPI
- **State Management:** Custom store (e.g., Zustand or similar)
- **Graph Visualization:** React Flow (or equivalent)

---

## Installation

### Frontend

1. Navigate to the frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) to view the app.

### Backend

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

4. The backend will run on [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

1. Open the frontend app in the browser.
2. Drag and drop nodes onto the canvas.
3. Connect nodes with edges to form a pipeline.
4. Enter text and variables in text nodes; new handles will appear dynamically.
5. Click the **Submit** button to validate the pipeline.
6. A modal will display the number of nodes, edges, and DAG status.

---

## Project Structure

```
NodePipleine/
├─ frontend/
│  ├─ src/
│  │  ├─ components/       # UI components
│  │  ├─ nodes/            # Node types and abstractions
│  │  ├─ store.js          # State management
│  │  └─ submit.js         # Submit button logic
├─ backend/
│  ├─ main.py              # FastAPI backend with DAG validation
│  └─ requirements.txt     # Python dependencies
```

---

## Running Tests

- Frontend:

  ```bash
  npm test
  ```

  Launches the interactive test runner.

- Backend: Add custom Python tests as needed.

---

## Deployment

- Build the frontend for production:

  ```bash
  npm run build
  ```

- Deploy the backend with FastAPI using any preferred platform (Heroku, AWS, etc.).

---

## Notes

- The project is designed to showcase frontend engineering skills, backend integration, and dynamic UI handling.
- Self-loops and internal handles are automatically filtered from pipeline validation to ensure accurate node/edge reporting.
