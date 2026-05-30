LearnFlow AI 📘🎥🧠

LearnFlow AI is an intelligent, automated course curation and real-time evaluation platform. It leverages local Large Language Models (LLMs) and video metadata alignment engines to generate customized, progressive learning pathways integrated with targeted study materials and automatic diagnostic assessments.

🚀 Key Features

Dynamic Syllabus Synthesis: Generates logical, structured $N$-step curriculum pathways tailored strictly to the user's selected focus (Beginner, Intermediate, Advanced).

Automated Video Resource Curation: Dynamically parses syllabus topics to query and map highly contextual visual media tutorials directly within the study pipeline.

Multi-Tier Diagnostic Assessments: Automatically synthesizes balanced diagnostic evaluations, compiling multiple-choice questions across distinct, progressive difficulty spectrums (Easy, Medium, Hard).

📸 Application Walkthrough

1. Interactive Course Curation

Specify any course subject along with your target proficiency level. LearnFlow AI instantly calculates a sequential, high-pacing learning path with explicit target outcomes.

2. Tailored Visual Study Labs

Each structured curriculum step automatically aligns with high-quality video resources, embedded with custom components designed for premium readability.

3. Comprehensive Competency Diagnostics

Test your retention through diagnostic quizzes generated directly from your syllabus topics, complete with real-time scoring, input state validation, and immediate correctness feedback loops.

🛠️ System Architecture

LearnFlow AI relies on a clean, decoupled service architecture, ensuring frontend presentation code remains isolated from dynamic AI generation modules:

├── App.py                  # Main navigation router & entry-point
├── Pages/
│   ├── learning_plan_page.py # UI: Course parameter setup & Syllabus render
│   ├── youtube_page.py       # UI: Video tutorial hub & custom video styling
│   └── quiz_page.py          # UI: Interactive multi-tier diagnostics
├── Services/
│   ├── llm_service.py        # Central Ollama LLM setup & parsing schemas
│   ├── roadmap_service.py    # Curates syllabus structure from Ollama responses
│   ├── mcq_service.py        # Concurrent Easy/Medium/Hard quiz generator
│   └── youtube_service.py    # Queries live YouTube video metadata API endpoints
└── Utils/
    ├── prompt.py             # System prompt templates
    └── parsers.py            # Custom JSON extraction and cleaning utilities


🚀 Getting Started

Follow these instructions to spin up a local instance of LearnFlow AI on your machine.

Prerequisites

Python 3.9+ installed.

Ollama installed and running locally. Run the following command to pull the baseline model:

ollama pull llama3



Installation

Clone this repository:

git clone [https://github.com/your-username/learnflow-ai.git](https://github.com/your-username/learnflow-ai.git)
cd learnflow-ai



Install dependencies:

pip install -r requirements.txt



Run the application:

streamlit run App.py



📈 Planned Roadmap (What's Next!)

⚡ Concurrent Execution (Phase 1): Implementing asynchronous generation pipelines using Python's asyncio to fetch Easy, Medium, and Hard quiz collections in parallel, reducing page loading latency by over 50%.

🎯 Dynamic RAG Cache (Phase 2): Migrating from active text-search queries to an embedded, localized Vector Database (ChromaDB). This will enable offline caching, dynamic indexing, and metadata-filtered search optimization.