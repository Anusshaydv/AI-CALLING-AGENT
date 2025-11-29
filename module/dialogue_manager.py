def agent_greeting():
    print("Agent: Hello! This is an automated assistant calling from Hookfish Realty.")
    print("Agent: You had shown interest in real-estate properties earlier.")
    print("Agent: Is this a good time to talk about a property that might fit your needs?")


def handle_first_response(context: CallContext, user_text: str) -> str:
    intent = detect_intent(user_text)

    if intent == "INTERESTED":
        context.interested = True
        print("\nAgent: That’s great to hear! Let me ask some quick questions.")
        return "INTERESTED_FLOW"

    elif intent == "BUSY":
        context.busy = True
        print("\nAgent: No worries, I understand you're busy.")
        print("Agent: When would be a good time for us to call back?")
        return "BUSY_FLOW"

    elif intent == "REJECT":
        context.rejected = True
        print("\nAgent: Understood. We'll avoid disturbing you.")
        return "REJECT_FLOW"

    else:
        print("\nAgent: I didn’t understand that.")
        print("Agent: Are you interested, busy, or not interested?")
        return "CLARIFY"
def run_interested_flow(context: CallContext):
    print("\nAgent: What is your preferred location?")
    location = input("Customer: ").strip()
    if location:
        context.preferred_location = location

    print("\nAgent: What type of property are you looking for?")
    print("Agent: (For example: apartment, villa, independent house, or plot)")
    property_type = input("Customer: ").strip()
    if property_type:
        context.property_type = property_type

    print("\nAgent: And what is your budget range?")
    budget = input("Customer: ").strip()
    if budget:
        context.budget = budget


    print("\nAgent: Thank you! Our team will contact you soon with suitable properties.")
    print("Agent: Have a nice day!")


def run_busy_flow(context: CallContext):
    follow_up = input("Customer (follow-up time): ").strip()
    if follow_up:
        context.follow_up_time = follow_up

    print("\nAgent: Great, I have noted that.")
    print("Agent: We'll contact you at that time.")
    print("Agent: Have a good day!")


def run_reject_flow(context: CallContext):
    print("\nAgent: Thank you for your time.")
    print("Agent: Feel free to reach out if you change your mind.")
    print("Agent: Goodbye!")


def clarify_and_route(context: CallContext):
    user_text = input("Customer: ")
    next_state = handle_first_response(context, user_text)

    if next_state == "INTERESTED_FLOW":
        run_interested_flow(context)
    elif next_state == "BUSY_FLOW":
        run_busy_flow(context)
    elif next_state == "REJECT_FLOW":
        run_reject_flow(context)
    else:
        print("\nAgent: I'm still confused. Ending call.")
        print("Agent: Have a good day!")
