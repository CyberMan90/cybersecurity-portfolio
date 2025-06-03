#!/bin/bash

echo "🔍 Auditing S3 Buckets..."

# List all S3 buckets
buckets=$(aws s3api list-buckets --query "Buckets[].Name" --output text)

for bucket in $buckets; do
  echo "-----------------------------------------"
  echo "📦 Bucket: $bucket"

  # Check public access block settings
  aws s3api get-bucket-policy-status --bucket "$bucket" --output json 2>/dev/null \
    | grep -q '"IsPublic": true' \
    && echo "❌ Public: Yes (Bucket is publicly accessible!)" \
    || echo "✅ Public: No"

  # Check if default encryption is enabled
  aws s3api get-bucket-encryption --bucket "$bucket" --output json 2>/dev/null \
    && echo "✅ Encryption: Enabled" \
    || echo "⚠️  Encryption: Not Enabled"

  # Check if versioning is enabled
  status=$(aws s3api get-bucket-versioning --bucket "$bucket" --query "Status" --output text 2>/dev/null)
  if [ "$status" == "Enabled" ]; then
    echo "✅ Versioning: Enabled"
  else
    echo "⚠️  Versioning: Not Enabled"
  fi
done

echo "✅ S3 Audit Complete!"
