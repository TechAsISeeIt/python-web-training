from django.shortcuts import render
from .models import Query


# Create your views here.
def core(request):
    name = "Uday Doppalapudi"
    queries = Query.objects.all().order_by("-created_at")
    if request.method == "POST":
        name = request.POST.get("delete_query_id")
        Query.objects.filter(id=name).delete()
    return render(request, "index.html", {"queries": queries, "name": name})


def chat(request):
    question = None
    answer = None
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides accurate and concise answers to user questions.",
        }
    ]
    if request.method == "POST":
        question = request.POST.get("question")

        from .openai_model import query

        messages.append({"role": "user", "content": question})

        answer = query(user_input=messages)

        messages.append({"role": "assistant", "content": answer})

        # Save the question and answer to the database
        Query.objects.create(question=question, answer=answer)

    return render(
        request,
        "chat.html",
        {"question": question, "answer": answer, "messages": messages},
    )
