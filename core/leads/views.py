from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now
import json

from .models import Lead

def format_budget(budget):
    if budget >= 10000000:
        return f"{budget // 10000000} crore"
    elif budget >= 100000:
        return f"{budget // 100000} lakhs"
    else:
        return f"{budget}"

@csrf_exempt
def dialogflow_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        query_text = data.get('queryResult', {}).get('queryText')
        params = data.get('queryResult', {}).get('parameters', {})

        location = params.get('geo_city')
        property_type = params.get('property_type')
        budget = int(params.get('budget', 0))
        formatted_budget = format_budget(budget)

        # Save lead
        Lead.objects.create(
            phone_number=None,  # we'll add phone number later if WhatsApp is used
            location=location,
            property_type=property_type,
            budget=budget,
            formatted_budget=formatted_budget,
            raw_query=query_text
        )

        return JsonResponse({
            "fulfillmentText": f"Thanks! We’re processing your request for a {property_type} in {location} under {formatted_budget}."
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)