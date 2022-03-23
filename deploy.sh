gcloud \
    functions \
    deploy translate_pytorch \
    --runtime python37 \
    --trigger-http \
    --allow-unauthenticated \
    --project chris-loves-ai \
    --region us-central1 \
    --memory 2048 \
    --timeout 540