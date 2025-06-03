#!/bin/bash

echo "🔍 Auditing IAM Users..."

# List IAM users
echo "-----------------------------------------"
aws iam list-users --output table

# Check if MFA is enabled for users
echo "-----------------------------------------"
echo "🔐 Checking MFA status:"
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
    mfa_devices=$(aws iam list-mfa-devices --user-name "$user" --query 'MFADevices' --output json)
    if [[ "$mfa_devices" == "[]" ]]; then
        echo "❌ $user: MFA NOT enabled"
    else
        echo "✅ $user: MFA enabled"
    fi
done

# Access Key rotation status
echo "-----------------------------------------"
echo "🕒 Checking Access Key Usage:"
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
    keys=$(aws iam list-access-keys --user-name "$user" --query 'AccessKeyMetadata[*].AccessKeyId' --output text)
    for key in $keys; do
        last_used=$(aws iam get-access-key-last-used --access-key-id "$key" --query 'AccessKeyLastUsed.LastUsedDate' --output text)
        echo "🔑 $user | Key: $key | Last Used: $last_used"
    done
done

echo "✅ IAM Audit Complete!"
