"""
Configuration for DraGIN-RAG Retrieval Engine
"""

from typing import Dict, List
from pydantic import BaseSettings, Field

class DraGINConfig(BaseSettings):
    # Graph Configuration
    graph_embedding_dim: int = 768
    max_graph_nodes: int = 1000
    edge_threshold: float = 0.6
    
    # Draft Phase Settings
    draft_temperature: float = 0.7
    max_draft_tokens: int = 200
    draft_strategies: List[str] = Field(
        default=["semantic", "keyword", "citation"]
    )
    
    # Retrieve Phase Settings
    max_hops: int = 3
    retrieval_depth: int = 5
    context_window: int = 2000
    similarity_threshold: float = 0.7
    
    # Integration Settings
    integration_temperature: float = 0.4
    max_integration_tokens: int = 500
    synthesis_methods: List[str] = Field(
        default=["aggregate", "compare", "synthesize"]
    )
    
    # Self-critique Settings
    confidence_threshold: float = 0.8
    max_refinement_steps: int = 3
    validation_methods: List[str] = Field(
        default=["consistency", "relevance", "completeness"]
    )
    
    # Cache Settings
    cache_ttl: int = 3600
    max_cache_size: int = 1000
    
    class Config:
        env_prefix = "DRAGIN_"

# Default configuration instance
config = DraGINConfig() 