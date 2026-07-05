from langgraph.graph import StateGraph, END

from app.models.state import PipelineState

from app.agents.intent_parser import IntentParserAgent
from app.agents.image_analyzer import ImageAnalyzerAgent
from app.agents.storyboard_writer import StoryboardWriterAgent
from app.agents.render_agent import RenderAgent


def build_graph():

    workflow = StateGraph(PipelineState)

    # Register Agents
    workflow.add_node(
        "intent_parser",
        IntentParserAgent()
    )

    workflow.add_node(
        "image_analyzer",
        ImageAnalyzerAgent()
    )

    workflow.add_node(
        "storyboard_writer",
        StoryboardWriterAgent()
    )

    workflow.add_node(
        "render_agent",
        RenderAgent()
    )

    # Entry Point
    workflow.set_entry_point(
        "intent_parser"
    )

    # Workflow
    workflow.add_edge(
        "intent_parser",
        "image_analyzer"
    )

    workflow.add_edge(
        "image_analyzer",
        "storyboard_writer"
    )

    workflow.add_edge(
        "storyboard_writer",
        "render_agent"
    )

    workflow.add_edge(
        "render_agent",
        END
    )

    return workflow.compile()