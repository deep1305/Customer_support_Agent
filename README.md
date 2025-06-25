# 🎧 Flipkart Audio Assistant

An intelligent audio product specialist chatbot powered by AI, designed to help customers find the perfect headphones, earbuds, and audio accessories. Specializes in audio products from brands like BoAt, OnePlus, Realme, and U&I using natural language processing and vector-based retrieval.

## ✨ Features

### 🎯 Core Functionality
- **Audio Product Search**: Natural language queries for finding headphones, earbuds, and neckbands
- **Smart Audio Recommendations**: AI-powered suggestions based on bass preferences, sound quality, and budget
- **Real-time Chat Interface**: Modern, responsive web-based chat interface optimized for audio products
- **Vector-based Retrieval**: Efficient semantic search using embeddings for audio product features
- **Audio Review Analysis**: Insights from customer reviews focusing on sound quality, bass, and comfort

### 🎨 User Interface
- **Modern Glassmorphism Design**: Beautiful gradient backgrounds with blur effects
- **Mobile Responsive**: Optimized for all screen sizes and devices
- **Smooth Animations**: Enhanced user experience with fluid transitions
- **Professional Styling**: Flipkart-inspired orange theme with clean typography
- **Audio-Focused Quick Suggestions**: Pre-defined chips for wireless headphones, wired headsets, Bluetooth neckbands, and budget audio

### 🔧 Technical Features
- **Smart Data Ingestion**: Prevents duplicate data insertion in vector store
- **Configurable Pipeline**: Easy setup and configuration management
- **Modular Architecture**: Clean separation of concerns with organized modules
- **Error Handling**: Robust error management and logging
- **Performance Optimized**: Hardware-accelerated animations and efficient queries

## 🏗️ Project Structure

```
Customer_support_Agent/
├── config/                     # Configuration files
│   └── config.yaml
├── data/                       # Audio product dataset
│   └── flipkart_product_review.csv  # Audio product reviews (headphones, earbuds, neckbands)
├── data_collection_pipeline/   # Web scraping modules
│   └── flipkart_scrapper.py
├── data_ingestion/            # Data processing pipeline
│   └── ingestion_pipeline.py
├── prompt_library/            # AI prompts and templates
│   └── prompt.py
├── retriever/                 # Vector search and retrieval
│   └── retrieval.py
├── utils/                     # Utility functions
│   ├── config_loader.py
│   └── model_loader.py
├── static/                    # CSS and static assets
│   └── style.css
├── templates/                 # HTML templates
│   └── chat.html
├── notebook/                  # Jupyter notebooks for experimentation
│   └── customer_support.ipynb
├── main.py                    # FastAPI application entry point
├── test.py                    # Testing and validation
└── requirements.txt           # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Customer_support_Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install setuptools  # If you encounter import errors
   ```

3. **Configure environment**
   - Update `config/config.yaml` with your settings
   - Set up any required API keys for AI models

4. **Run data ingestion** (first time only)
   ```bash
   python -c "from data_ingestion.ingestion_pipeline import DataIngestionPipeline; pipeline = DataIngestionPipeline(); pipeline.insert_data_once()"
   ```

5. **Start the application**
   ```bash
   uvicorn main:app --reload
   ```
   Or alternatively:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. **Access the audio assistant**
   Open your browser and navigate to `http://localhost:8000`

## 🎵 Available Audio Products

The assistant specializes in the following audio product categories:

### 🎧 **Wireless Headphones & Neckbands**
- **BoAt Rockerz 235v2** - Bluetooth headset with ASAP charging
- **OnePlus Bullets Wireless Z** - Premium wireless headphones with fast charging
- **realme Buds Wireless** - Comfortable Bluetooth headset with magnetic controls
- **realme Buds Q** - Compact Bluetooth earbuds
- **U&I Titanic Series** - Budget-friendly Bluetooth neckband

### 🎵 **Wired Headsets**
- **realme Buds 2** - Wired headset with enhanced bass
- **BoAt BassHeads 100** - Wired headset with superior sound quality

### 🔊 **True Wireless Earbuds**
- **BoAt Airdopes 131** - Bluetooth true wireless earbuds

### 🏷️ **Key Features Available**
- **Bass Quality**: Deep bass and enhanced low-frequency response
- **Sound Clarity**: Crystal clear audio and balanced sound
- **Battery Life**: Long-lasting battery with fast charging options
- **Comfort**: Ergonomic design for extended wear
- **Brand Variety**: BoAt, OnePlus, Realme, and U&I products

## 💬 Usage Examples

### Customer Queries
- "Best wireless headphones under ₹2000"
- "I need good headphones with strong bass"
- "Recommend Bluetooth neckbands for workouts"
- "Show me budget audio products with good reviews"
- "OnePlus vs BoAt headphones comparison"

### Audio-Specific Support Features
- Audio product comparisons (bass, sound quality, battery life)
- Price range filtering for audio accessories
- Review-based recommendations focusing on sound quality
- Brand-specific audio product guidance (BoAt, OnePlus, Realme, U&I)

## 🛠️ Development

### Running in Development Mode
```bash
# Install in development mode
pip install -e .

# Run with auto-reload
uvicorn main:app --reload
```

### Testing
```bash
python test.py
```

## 🔮 Future Improvements & Roadmap

### 🌐 Web Scraping Enhancements
- **Real-time Product Scraping**: 
  - Live product data from multiple e-commerce platforms
  - Price tracking and comparison across websites
  - Automated inventory updates and availability checks
  - Dynamic product catalog expansion

- **Advanced Scraping Features**:
  - Multi-threaded scraping for faster data collection
  - Respect robots.txt and implement ethical scraping practices
  - Captcha handling and anti-bot detection bypass
  - Scheduled scraping with cron jobs

### 🤖 AI & Machine Learning
- **Enhanced NLP Capabilities**:
  - Sentiment analysis for customer feedback
  - Intent classification for better query understanding
  - Multi-language support for global customers
  - Voice-to-text integration for audio queries

- **Recommendation Engine**:
  - Collaborative filtering based on user behavior
  - Deep learning models for personalized suggestions
  - A/B testing framework for recommendation optimization
  - Real-time learning from user interactions

### 📊 Analytics & Insights
- **Customer Analytics Dashboard**:
  - User behavior tracking and analysis
  - Popular product trends and insights
  - Conversion rate optimization metrics
  - Customer satisfaction scoring

- **Business Intelligence**:
  - Sales performance analytics
  - Product performance insights
  - Customer journey mapping
  - Predictive analytics for demand forecasting

### 🔗 Integration & API
- **Third-party Integrations**:
  - Payment gateway integration
  - Inventory management systems
  - CRM system connectivity
  - Social media platform integration

- **API Development**:
  - RESTful API for mobile applications
  - Webhook support for real-time notifications
  - GraphQL endpoint for flexible data queries
  - Rate limiting and authentication

### 🎨 User Experience
- **Advanced UI Features**:
  - Dark/light theme toggle
  - Customizable chat themes
  - Rich media support (images, videos, documents)
  - Interactive product carousels

- **Accessibility Improvements**:
  - Screen reader compatibility
  - Keyboard navigation support
  - High contrast mode
  - Multi-device synchronization

### 🔐 Security & Performance
- **Security Enhancements**:
  - OAuth 2.0 authentication
  - Data encryption at rest and in transit
  - GDPR compliance features
  - Security audit logging

- **Performance Optimization**:
  - Redis caching for faster responses
  - CDN integration for static assets
  - Database query optimization
  - Microservices architecture migration

### 📱 Mobile & Cross-platform
- **Mobile Applications**:
  - Native iOS and Android apps
  - Progressive Web App (PWA) support
  - Push notifications
  - Offline functionality

### 🧪 Advanced Features
- **Experimental Technologies**:
  - Augmented Reality (AR) product visualization
  - Blockchain integration for supply chain transparency
  - IoT device compatibility
  - Edge computing for faster response times

### 🌍 Scalability & Infrastructure
- **Cloud & DevOps**:
  - Docker containerization
  - Kubernetes orchestration
  - CI/CD pipeline automation
  - Multi-region deployment

- **Monitoring & Observability**:
  - Application performance monitoring
  - Error tracking and alerting
  - Log aggregation and analysis
  - Health check endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Deep Shah** - *Initial work* - [shahdeep1399@gmail.com](mailto:shahdeep1399@gmail.com)

## 🙏 Acknowledgments

- Flipkart for product data inspiration
- LangChain community for AI framework
- FastAPI for the excellent web framework
- All contributors and supporters of this project

## 📞 Support

For support, email shahdeep1399@gmail.com or create an issue in the repository.

---

⭐ **Star this repository if you find it helpful!** ⭐
