"""
Tests for DraGIN-RAG Engine
"""

import pytest
import numpy as np
from typing import Dict, Any
from ..src.engine import DraGINEngine, GraphNode, GraphEdge
from ..src.config import DraGINConfig

@pytest.fixture
def dragin_engine():
    config = DraGINConfig()
    return DraGINEngine(config)

@pytest.fixture
def sample_graph_node():
    return GraphNode(
        id="node1",
        content="Sample medical content",
        embedding=np.random.rand(768),
        metadata={"type": "research_paper", "year": 2023}
    )

@pytest.fixture
def sample_context():
    return {
        "session_id": "test_session",
        "previous_queries": [],
        "domain": "medical_research"
    }

@pytest.mark.asyncio
async def test_draft_query(dragin_engine):
    query = "What are the latest treatments for diabetes?"
    draft_result = await dragin_engine.draft_query(query)
    
    assert isinstance(draft_result, dict)
    assert "strategy" in draft_result
    assert "path" in draft_result

@pytest.mark.asyncio
async def test_retrieve_information(dragin_engine, sample_graph_node):
    draft_strategy = {
        "strategy": "semantic",
        "focus": "diabetes_treatment",
        "path": []
    }
    
    results = await dragin_engine.retrieve_information(draft_strategy)
    assert isinstance(results, list)
    assert all(isinstance(node, GraphNode) for node in results)

@pytest.mark.asyncio
async def test_integrate_information(dragin_engine, sample_graph_node):
    nodes = [sample_graph_node]
    draft_strategy = {
        "strategy": "semantic",
        "focus": "diabetes_treatment",
        "path": []
    }
    
    result = await dragin_engine.integrate_information(nodes, draft_strategy)
    assert isinstance(result, dict)
    assert "synthesis" in result

def test_self_critique(dragin_engine):
    answer = {
        "content": "Sample answer",
        "confidence": 0.8,
        "sources": ["node1"]
    }
    context = {
        "query": "Sample query",
        "domain": "medical"
    }
    
    critique = dragin_engine.self_critique(answer, context)
    assert isinstance(critique, dict)
    assert "confidence" in critique
    assert "suggestions" in critique

@pytest.mark.asyncio
async def test_complete_dragin_loop(dragin_engine, sample_context):
    query = "What are the latest treatments for diabetes?"
    
    result = await dragin_engine.execute_dragin_loop(
        query,
        context=sample_context
    )
    
    assert isinstance(result, dict)
    assert "answer" in result
    assert "reasoning_path" in result
    assert "confidence" in result
    assert "sources" in result 