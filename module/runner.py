def run_call_simulation():
    context = CallContext()

    print(" Hookfish AI Calling Agent \n")

    name = input("Enter customer name : ").strip()
    if name:
        context.customer_name = name

    print("\n CALL STARTED \n")
    agent_greeting()

    first_reply = input("Customer: ")
    next_state = handle_first_response(context, first_reply)

    if next_state == "INTERESTED_FLOW":
        run_interested_flow(context)
    elif next_state == "BUSY_FLOW":
        run_busy_flow(context)
    elif next_state == "REJECT_FLOW":
        run_reject_flow(context)
    elif next_state == "CLARIFY":
        clarify_and_route(context)

    print("\n CALL SUMMARY ")
    print("Outcome:", context.outcome_status)
    print("Follow-up time:", context.follow_up_time or "None")
    print("Notes:", context.summary_notes)
    print("\n--- CALL ENDED ---")
