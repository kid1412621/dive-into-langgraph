"""
默认版系统提示词
"""


def get_system_prompt() -> str:
    """生成系统提示词"""
    return "You are a helpful assistant. Be concise and accurate."


if __name__ == "__main__":
    print(get_system_prompt())
