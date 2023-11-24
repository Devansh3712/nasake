from models.schemas import Test, TestQuestion, TestScore

options = {"YES": 1, "NO": 0}

ptsd_test = Test(
    name="PTSD Test",
    prompt="Sometimes things happen to people that are unusually or especially frightening, - horrible, or traumatic. \
        For example:\n\t- a serious accident or fire\n\t- a physical or sexual assault or abuse\n\t- an earthquake or flood\n\t- a war\n\t- seeing someone be killed or seriously injured\n\t- having a loved one die through homicide or suicide.\
            \nHave you ever experienced this kind of event?\nIf YES - please answer the questions below.\nIn the past month, have you...",
    scores=[
        TestScore(score=(0, 0), result="No Signs of PTSD"),
        TestScore(score=(1, 2), result="Minimal Signs of PTSD"),
        TestScore(score=(3, 5), result="Severe Signs of PTSD"),
    ],
    content={
        1: TestQuestion(
            question="had nightmares about the event(s) or thought about the event(s) when you did not want to?",
            options=options,
        ),
        2: TestQuestion(
            question="tried hard not to think about the event(s) or went out of your way to avoid situations that reminded you of the event(s)?",
            options=options,
        ),
        3: TestQuestion(
            question="been constantly on guard, watchful, or easily startled?",
            options=options,
        ),
        4: TestQuestion(
            question="felt numb or detached from people, activities, or your surroundings?",
            options=options,
        ),
        5: TestQuestion(
            question="felt guilty or unable to stop blaming yourself or others for the event(s) or any problems the event(s) may have caused?",
            options=options,
        ),
    },
)
