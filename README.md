# AI-Researcher: Automated Web Research Assistant

## Description
AI-Researcher is a Streamlit-based application designed to streamline web research. It leverages advanced AI models to perform web searches, summarize results, and generate concise, informative responses to user queries. Built with [LangChain](https://www.langchain.com/), [Ollama](https://ollama.ai/), and [Tavily](https://tavily.com/), this tool is ideal for researchers, students, and developers seeking quick, reliable insights from the web.

## Features
- **Automated Web Research**: Uses Tavily to fetch relevant web content based on user queries.
- **AI-Powered Summarization**: Summarizes search results using the Ollama `deepseek-r1:1.5b` model for clarity.
- **Response Generation**: Crafts concise answers tailored to the query using summarized content.
- **User-Friendly Interface**: Simple Streamlit UI for seamless query input and result display.
- **State Machine Workflow**: Employs [LangGraph](https://github.com/langchain-ai/langgraph) for structured research processing.

## Installation
1. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install python-dotenv streamlit langchain-ollama langchain-community langgraph langchain-core typing-extensions
   ```
2. **Set Up Ollama**:
   Install [Ollama](https://ollama.ai/) and run the `deepseek-r1:1.5b` model:
   ```bash
   ollama run deepseek-r1:1.5b
   ```
3. **Configure Tavily API**:
   Obtain a [Tavily API key](https://tavily.com/) and create a `.env` file in the project root with:
   ```
   TAVILY_API_KEY=your_api_key_here
   ```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run ai.py
   ```
2. Open the provided URL in your browser.
3. Enter a research query in the text input field (e.g., "What is the capital of France?").
4. View the generated response and source URLs displayed on the page.

## How It Works
AI-Researcher uses a state machine defined with [LangGraph](https://github.com/langchain-ai/langgraph) to manage the research process, consisting of three key stages:
1. **Web Search**: The `search_web` function uses [Tavily](https://tavily.com/) to fetch the top three search results, storing their URLs and content.
2. **Result Summarization**: The `summarize_results` function processes each search result using the Ollama `deepseek-r1:1.5b` model, generating concise summaries. A `clean_text` function removes `<think>` tags (model-generated reasoning) for clarity.
3. **Response Generation**: The `generate_response` function combines summaries into a single context and uses the Ollama model to craft a final response tailored to the query.

The state machine ensures a smooth flow from search to summarization to response generation, with typed dictionaries (`ResearchState`, `ResearchStateInput`, `ResearchStateOutput`) maintaining clear data structures.

## Dependencies
- [python-dotenv](https://github.com/theskumar/python-dotenv): Loads environment variables from `.env`.
- [streamlit](https://streamlit.io/): Powers the web-based user interface.
- [langchain-ollama](https://github.com/langchain-ai/langchain/tree/master/libs/langchain/langchain_ollama): Integrates Ollama models with LangChain.
- [langchain-community](https://github.com/langchain-ai/langchain/tree/master/libs/community): Provides Tavily search tools.
- [langgraph](https://github.com/langchain-ai/langgraph): Defines the state machine workflow.
- [langchain-core](https://github.com/langchain-ai/langchain/tree/master/libs/core): Supplies prompt templates.
- [typing-extensions](https://github.com/python/typing): Enhances type hints for Python.

## Limitations
- **External Service Dependency**: Relies on Tavily for search and Ollama for AI processing, requiring active internet and valid API keys.
- **Model Performance**: Response quality depends on the `deepseek-r1:1.5b` model, which may vary by query complexity.
- **English-Centric**: Optimized for English queries, with potential limitations for other languages.
- **Search Result Quality**: Accuracy depends on Tavily’s search results, which may include outdated or irrelevant content.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please open an issue to discuss major changes before submitting code.

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Related Projects
Explore similar AI-driven research tools:
- [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher): A system for automated scientific discovery.
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher): An LLM-based agent for deep research with citations.
- [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist): A tool for fully automated scientific discovery.

## Notes
- This tool is intended for research purposes only. Always verify generated information for accuracy.
- Ensure Ollama and Tavily services are running before launching the app.
- Customize the code to experiment with different AI models or search engines for enhanced functionality.
