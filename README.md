# 🎬 FotoOwl AI
## AI-Powered Automated Cinematic Video Generation using Multi-Agent AI

---

## 📖 Overview

FotoOwl AI is an AI-powered automated video generation system that transforms a collection of images into a cinematic video using Artificial Intelligence.

The system understands the user's editing intent, analyzes image quality, retrieves professional video editing knowledge using Retrieval-Augmented Generation (RAG), generates a cinematic storyboard, and automatically renders a professional MP4 video using Remotion.

The entire workflow is orchestrated using LangGraph's multi-agent architecture.

---

## 🚀 Features

- 🤖 Multi-Agent AI Workflow using LangGraph
- 🧠 Intent Understanding using Groq LLM
- 📷 Automatic Image Quality Analysis using OpenCV
- 📚 Retrieval-Augmented Generation (RAG) using ChromaDB
- 📝 AI Storyboard Generation
- 🎞 Automatic Timeline Generation
- 🎥 Automated Video Rendering using Remotion
- ✨ Cinematic Transitions and Animations
- ⚡ One-Command Video Generation

---

# 🏗️ System Architecture

```
                     User Prompt
                          │
                          ▼
                 Intent Parser Agent
                    (Groq LLM)
                          │
                          ▼
                Image Analyzer Agent
                      (OpenCV)
                          │
                          ▼
              ChromaDB Knowledge Base
                  (RAG Retrieval)
                          │
                          ▼
             Storyboard Writer Agent
           (LLM + Retrieved Knowledge)
                          │
                          ▼
                 Timeline Generator
                          │
                          ▼
                   Render Agent
             (Remotion Integration)
                          │
                          ▼
                 Final MP4 Video
```

---

# 🧠 AI Workflow

## 1. Intent Parser Agent

This agent understands the user's prompt and extracts:

- Video pacing
- Visual style
- Caption tone
- Transition style

Example Input

```
Create a cinematic wedding reel with warm colors and emotional storytelling.
```

Example Output

```json
{
  "pacing": "slow",
  "visual_style": "warm cinematic",
  "caption_tone": "minimal",
  "transition_style": "fade"
}
```

---

## 2. Image Analyzer Agent

Uses OpenCV to evaluate every image based on:

- Resolution
- Brightness
- Blur Detection
- Overall Quality Score

The highest-quality images are automatically selected for the final video.

---

## 3. RAG (Retrieval-Augmented Generation)

Instead of relying only on the LLM, FotoOwl AI retrieves professional editing guidelines from a ChromaDB knowledge base.

The retrieved context is combined with the user's prompt before generating the storyboard.

This improves consistency and ensures that cinematic editing principles are followed.

---

## 4. Storyboard Writer Agent

Using:

- User Prompt
- Retrieved Editing Knowledge
- Selected Images

The LLM generates a structured storyboard including:

- Image order
- Captions
- Duration
- Animation
- Transition

---

## 5. Timeline Generator

The storyboard is converted into a frame-based timeline used by Remotion.

Each scene contains:

- Image
- Caption
- Animation
- Transition
- Start Frame
- Duration

---

## 6. Render Agent

The Render Agent automatically:

- Generates timeline.json
- Copies required assets
- Launches Remotion
- Renders the final MP4

No manual intervention is required.

---

# 📚 RAG Workflow

```
User Prompt
      │
      ▼
Query ChromaDB
      │
      ▼
Retrieve Editing Knowledge
      │
      ▼
Groq LLM
      │
      ▼
Storyboard Generation
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| LangGraph | Multi-Agent Workflow |
| Groq LLM | Intent Parsing & Storyboard Generation |
| ChromaDB | Retrieval-Augmented Generation |
| OpenCV | Image Analysis |
| React | Video Components |
| Remotion | Automated Video Rendering |
| TypeScript | Remotion Components |

---

# 📂 Project Structure

```
FotoOwl-AI
│
├── app
│   ├── agents
│   ├── graph
│   ├── models
│   ├── services
│   └── config.py
│
├── chroma_db
│
├── data
│   ├── images
│   └── knowledge
│
├── dev
│
├── output
│
├── remotion
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# ▶️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd FotoOwl-AI
```

---

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Remotion Dependencies

```bash
cd remotion

npm install

cd ..
```

---

## 4. Load Knowledge Base (Only Once)

```bash
python dev/load_rag.py
```

---

## 5. Generate Video

```bash
python main.py
```

---

# 📁 Output

Generated files are stored inside:

```
output/

├── image_analysis.json
├── storyboard.json
└── final_video.mp4
```

---

# 📸 Sample Workflow

```
Input Images
      │
      ▼
Image Quality Analysis
      │
      ▼
Intent Detection
      │
      ▼
RAG Knowledge Retrieval
      │
      ▼
Storyboard Generation
      │
      ▼
Timeline Generation
      │
      ▼
Remotion Rendering
      │
      ▼
Final MP4 Video
```

---

# 🎯 Objectives

- Automate cinematic video creation using AI.
- Reduce manual video editing effort.
- Demonstrate Multi-Agent AI architecture.
- Integrate Retrieval-Augmented Generation (RAG).
- Render videos programmatically using Remotion.

---

# 📈 Future Enhancements

- AI Face Recognition
- Scene Detection
- AI Voice-over Generation
- Automatic Background Music Selection
- Multiple Aspect Ratio Support (9:16, 16:9, 1:1)
- AI Color Grading
- Emotion-Based Storytelling

---

# 📚 Challenges Faced

- Migration from Gemini API to Groq due to API quota limitations.
- Integrating multiple AI agents using LangGraph.
- Ensuring reliable video rendering by replacing AI-generated React code with a reusable Remotion component.
- Integrating Retrieval-Augmented Generation (RAG) using ChromaDB for improved storyboard quality.

---

# 👨‍💻 Authors

**Project Name:** FotoOwl AI

Developed as a Final Year Engineering Project.

---

# ⭐ Conclusion

FotoOwl AI demonstrates how Large Language Models, Retrieval-Augmented Generation (RAG), Computer Vision, and Programmatic Video Rendering can be combined to automate the creation of cinematic videos. The project showcases a scalable Multi-Agent AI architecture capable of transforming static images into engaging visual stories with minimal human intervention.