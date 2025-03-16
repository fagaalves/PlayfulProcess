# Preschool Storytelling App

## Project Objective
Develop a Django-based interactive storytelling app for preschoolers that uses voice input to generate structured stories and AI-generated illustrations. The system stores user-generated stories and images in an SQL database.

## Features
- **User Authentication:** Optional for parents to manage their child's stories.
- **Voice Input:** Utilize the OpenAI Whisper API for speech-to-text conversion.
- **AI-Generated Illustrations:** Use DALL·E for generating images based on story context.
- **Story Structuring:** Leverage OpenAI GPT-4 for structuring and refining stories.
- **Story Playback:** Implement text-to-speech using ElevenLabs or OpenAI TTS.
- **Database:** SQL-based storage using PostgreSQL for production and SQLite for development.
- **Drag-and-Drop Editing:** Intuitive UI for editing stories using JavaScript or React.
- **Export & Sharing:** Export stories as PDFs or interactive storybooks.

## Technical Specifications
- **Backend:** Django (Python)
- **Database:** PostgreSQL for production, SQLite for development
- **Frontend:** Django Templates with JavaScript or React
- **APIs:**
  - OpenAI Whisper for speech-to-text
  - OpenAI GPT-4 for story structuring
  - DALL·E for illustrations
  - ElevenLabs / OpenAI TTS for story playback

## Deployment
- **Dockerized:** For local and cloud deployment
- **Hosting:** Compatible with AWS, GCP, Azure, or Render

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fagaalves/PlayfulProcess.git
   cd PlayfulProcess/PreschoolStorytellingApp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Navigate to `http://localhost:8000` in your browser.
- Register or log in as a parent (optional).
- Start creating stories using voice input.
- Edit stories using the drag-and-drop interface.
- Export and share stories with others.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
ystem stores user-generated stories and images in an SQL database.
