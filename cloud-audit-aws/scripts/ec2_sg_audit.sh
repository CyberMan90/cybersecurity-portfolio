#!/bin/bash

# ec2_sg_audit.sh – Detects overly permissive EC2 security groups

echo "🔍 Auditing EC2 Security Groups for public exposure..."

# Get all security groups
aws ec2 describe-security-groups --query 'SecurityGroups[*].{ID:GroupId,Name:GroupName,Ingress:IpPermissions}' --output json | jq -c '.[]' | while read -r sg; do
  sg_id=$(echo "$sg" | jq -r '.ID')
  sg_name=$(echo "$sg" | jq -r '.Name')
  echo "---------------------------------------------------"
  echo "🔎 Security Group: $sg_name ($sg_id)"

  echo "$sg" | jq -c '.Ingress[]?' | while read -r rule; do
    from_port=$(echo "$rule" | jq -r '.FromPort // "All"')
    to_port=$(echo "$rule" | jq -r '.ToPort // "All"')
    ip_ranges=$(echo "$rule" | jq -c '.IpRanges[]?.CidrIp')

    for cidr in $ip_ranges; do
      cidr_clean=$(echo "$cidr" | tr -d '"')
      if [[ "$cidr_clean" == "0.0.0.0/0" ]]; then
        echo "⚠️  PUBLIC access detected on port(s) $from_port-$to_port → $cidr_clean"
      fi
    done
  done
done

echo "✅ EC2 Security Group audit completed."
