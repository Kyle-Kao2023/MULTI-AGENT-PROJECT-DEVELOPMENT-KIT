from langgraph.graph import StateGraph, START, END
from graph.utils.state_types import P1State

def planner_node(state: P1State) -> P1State:
    state["current_step"] = "planner"
    state["plan"] = f"Dummy plan for {state.get('task','demo')}"
    return state

def dev_node(state: P1State) -> P1State:
    state["current_step"] = "dev"
    state["code_diff"] = "// dummy code diff"
    return state

def executor_node(state: P1State) -> P1State:
    state["current_step"] = "executor"
    state["pr_url"] = "https://example.com/pr/123"
    return state

def gate_node(state: P1State) -> P1State:
    state["current_step"] = "gate"
    state["backtest_report"] = {"sample_out_winrate": 0.72}
    state["gate_passed"] = True
    return state

def build_app():
    g = StateGraph(P1State)
    g.add_node("planner", planner_node)
    g.add_node("dev", dev_node)
    g.add_node("executor", executor_node)
    g.add_node("gate", gate_node)

    g.add_edge(START, "planner")
    g.add_edge("planner", "dev")
    g.add_edge("dev", "executor")
    g.add_edge("executor", "gate")
    g.add_edge("gate", END)

    return g.compile()

if __name__ == "__main__":
    app = build_app()
    out = app.invoke({"task": "demo task"}, config={"thread_id": "demo"})
    print(out)
