# SkimMed

A robust framework for medical paper analysis and interpretation.

## Project Overview
SkimMed is an advanced medical paper analysis platform that processes, analyzes, and interprets medical research papers using state-of-the-art AI technologies.

## Project Structure
```
SkimMed/
├── 1-multimodal-ingestion/      # MIME routing and document processing
├── 2-parsing-enrichment/        # OCR and biomedical entity recognition
├── 3-dual-indexing/            # Dense and sparse indexing systems
├── 4-retrieval-engine/         # Query processing and retrieval
├── 5-ui-api/                   # Frontend and API interfaces
├── 6-harmonisation/            # Ontology mapping and standardization
├── common/                     # Shared utilities and configurations
└── tests/                      # Test suites for all components
```

## Component Details

### 1. Multi-Modal Ingestion
- MIME-type based routing
- PDF/Image/Audio processing
- Metadata management

### 2. Parsing & Enrichment
- OCR processing
- Table/diagram detection
- UMLS entity linking

### 3. Dual-Indexing Layer
- Dense vector embeddings
- Sparse indices
- Hybrid retrieval system

### 4. Retrieval & Query Engine
- Hybrid search implementation
- Query routing
- Ranking system

### 5. UI & API Layer
- REST/GraphQL endpoints
- Web interface
- Documentation

### 6. Harmonisation & Ontology
- Unit/date normalization
- FHIR/SNOMED mapping
- Schema validation

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/AshNicolus/SkimMed.git
cd SkimMed
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```



## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


