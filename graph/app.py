from langgraph.graph import StateGraph, START, END
from graph.utils.state_types import P1State
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

def planner_node(state: P1State) -> P1State:
    state["current_step"] = "planner"
    task = state.get("task", "demo task")
    llm = ChatAnthropic(model="claude-3-7-sonnet-latest", temperature=0.2)
    prompt = f"""你是專案規劃顧問。請用 3-6 個步驟為此任務擬定技術規劃與測試大綱：
任務：{task}
輸出格式：每行一個步驟，盡量具體可驗收。"""
    resp = llm.invoke(prompt)
    state["plan"] = resp.content
    return state

def dev_node(state: P1State) -> P1State:
    state["current_step"] = "dev"
    task = state.get("task", "demo feature")
    plan = state.get("plan", "")
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""你是資深工程師。根據規劃，產出可合併的最小變更（以 Python 片段或明確 diff/偽代碼描述）：
任務：{task}
規劃：
{plan}
只輸出代碼或明確修改清單，不要多餘解釋。"""
    resp = llm.invoke(prompt)
    state["code_diff"] = resp.content
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
