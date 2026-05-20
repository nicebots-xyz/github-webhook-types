# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""TypedDict payloads generated from Octokit's GitHub webhook schema.

Do not edit this module by hand. Run `pdm run generate` instead.
"""

from typing import Any, Literal, NotRequired, Required, TypedDict

__all__ = [
    "BranchProtectionConfigurationDisabledPayloadDict",
    "BranchProtectionConfigurationEnabledPayloadDict",
    "BranchProtectionRuleCreatedPayloadDict",
    "BranchProtectionRuleDeletedPayloadDict",
    "BranchProtectionRuleEditedPayloadDict",
    "CheckRunCompletedPayloadDict",
    "CheckRunCreatedPayloadDict",
    "CheckRunRequestedActionPayloadDict",
    "CheckRunRerequestedPayloadDict",
    "CheckSuiteCompletedPayloadDict",
    "CheckSuiteRequestedPayloadDict",
    "CheckSuiteRerequestedPayloadDict",
    "CodeScanningAlertAppearedInBranchPayloadDict",
    "CodeScanningAlertClosedByUserPayloadDict",
    "CodeScanningAlertCreatedPayloadDict",
    "CodeScanningAlertFixedPayloadDict",
    "CodeScanningAlertReopenedByUserPayloadDict",
    "CodeScanningAlertReopenedPayloadDict",
    "CommitCommentCreatedPayloadDict",
    "CreatePayloadDict",
    "CustomPropertyCreatedPayloadDict",
    "CustomPropertyDeletedPayloadDict",
    "CustomPropertyValuesUpdatedPayloadDict",
    "DeletePayloadDict",
    "DependabotAlertCreatedPayloadDict",
    "DependabotAlertDismissedPayloadDict",
    "DependabotAlertFixedPayloadDict",
    "DependabotAlertReintroducedPayloadDict",
    "DependabotAlertReopenedPayloadDict",
    "DeployKeyCreatedPayloadDict",
    "DeployKeyDeletedPayloadDict",
    "DeploymentCreatedPayloadDict",
    "DeploymentProtectionRuleRequestedPayloadDict",
    "DeploymentReviewApprovedPayloadDict",
    "DeploymentReviewRejectedPayloadDict",
    "DeploymentReviewRequestedPayloadDict",
    "DeploymentStatusCreatedPayloadDict",
    "DiscussionAnsweredPayloadDict",
    "DiscussionCategoryChangedPayloadDict",
    "DiscussionCommentCreatedPayloadDict",
    "DiscussionCommentDeletedPayloadDict",
    "DiscussionCommentEditedPayloadDict",
    "DiscussionCreatedPayloadDict",
    "DiscussionDeletedPayloadDict",
    "DiscussionEditedPayloadDict",
    "DiscussionLabeledPayloadDict",
    "DiscussionLockedPayloadDict",
    "DiscussionPinnedPayloadDict",
    "DiscussionTransferredPayloadDict",
    "DiscussionUnansweredPayloadDict",
    "DiscussionUnlabeledPayloadDict",
    "DiscussionUnlockedPayloadDict",
    "DiscussionUnpinnedPayloadDict",
    "ForkPayloadDict",
    "GithubAppAuthorizationRevokedPayloadDict",
    "GollumPayloadDict",
    "InstallationCreatedPayloadDict",
    "InstallationDeletedPayloadDict",
    "InstallationNewPermissionsAcceptedPayloadDict",
    "InstallationRepositoriesAddedPayloadDict",
    "InstallationRepositoriesRemovedPayloadDict",
    "InstallationSuspendPayloadDict",
    "InstallationTargetRenamedPayloadDict",
    "InstallationUnsuspendPayloadDict",
    "IssueCommentCreatedPayloadDict",
    "IssueCommentDeletedPayloadDict",
    "IssueCommentEditedPayloadDict",
    "IssuesAssignedPayloadDict",
    "IssuesClosedPayloadDict",
    "IssuesDeletedPayloadDict",
    "IssuesDemilestonedPayloadDict",
    "IssuesEditedPayloadDict",
    "IssuesLabeledPayloadDict",
    "IssuesLockedPayloadDict",
    "IssuesMilestonedPayloadDict",
    "IssuesOpenedPayloadDict",
    "IssuesPinnedPayloadDict",
    "IssuesReopenedPayloadDict",
    "IssuesTransferredPayloadDict",
    "IssuesUnassignedPayloadDict",
    "IssuesUnlabeledPayloadDict",
    "IssuesUnlockedPayloadDict",
    "IssuesUnpinnedPayloadDict",
    "LabelCreatedPayloadDict",
    "LabelDeletedPayloadDict",
    "LabelEditedPayloadDict",
    "MarketplacePurchaseCancelledPayloadDict",
    "MarketplacePurchaseChangedPayloadDict",
    "MarketplacePurchasePendingChangeCancelledPayloadDict",
    "MarketplacePurchasePendingChangePayloadDict",
    "MarketplacePurchasePurchasedPayloadDict",
    "MemberAddedPayloadDict",
    "MemberEditedPayloadDict",
    "MemberRemovedPayloadDict",
    "MembershipAddedPayloadDict",
    "MembershipRemovedPayloadDict",
    "MergeGroupChecksRequestedPayloadDict",
    "MergeGroupDestroyedPayloadDict",
    "MetaDeletedPayloadDict",
    "MilestoneClosedPayloadDict",
    "MilestoneCreatedPayloadDict",
    "MilestoneDeletedPayloadDict",
    "MilestoneEditedPayloadDict",
    "MilestoneOpenedPayloadDict",
    "OrgBlockBlockedPayloadDict",
    "OrgBlockUnblockedPayloadDict",
    "OrganizationDeletedPayloadDict",
    "OrganizationMemberAddedPayloadDict",
    "OrganizationMemberInvitedPayloadDict",
    "OrganizationMemberRemovedPayloadDict",
    "OrganizationRenamedPayloadDict",
    "PackagePublishedPayloadDict",
    "PackageUpdatedPayloadDict",
    "PageBuildPayloadDict",
    "PingPayloadDict",
    "ProjectCardConvertedPayloadDict",
    "ProjectCardCreatedPayloadDict",
    "ProjectCardDeletedPayloadDict",
    "ProjectCardEditedPayloadDict",
    "ProjectCardMovedPayloadDict",
    "ProjectClosedPayloadDict",
    "ProjectColumnCreatedPayloadDict",
    "ProjectColumnDeletedPayloadDict",
    "ProjectColumnEditedPayloadDict",
    "ProjectColumnMovedPayloadDict",
    "ProjectCreatedPayloadDict",
    "ProjectDeletedPayloadDict",
    "ProjectEditedPayloadDict",
    "ProjectReopenedPayloadDict",
    "ProjectsV2ItemArchivedPayloadDict",
    "ProjectsV2ItemConvertedPayloadDict",
    "ProjectsV2ItemCreatedPayloadDict",
    "ProjectsV2ItemDeletedPayloadDict",
    "ProjectsV2ItemEditedPayloadDict",
    "ProjectsV2ItemReorderedPayloadDict",
    "ProjectsV2ItemRestoredPayloadDict",
    "PublicPayloadDict",
    "PullRequestAssignedPayloadDict",
    "PullRequestAutoMergeDisabledPayloadDict",
    "PullRequestAutoMergeEnabledPayloadDict",
    "PullRequestClosedPayloadDict",
    "PullRequestConvertedToDraftPayloadDict",
    "PullRequestDemilestonedPayloadDict",
    "PullRequestDequeuedPayloadDict",
    "PullRequestEditedPayloadDict",
    "PullRequestEnqueuedPayloadDict",
    "PullRequestLabeledPayloadDict",
    "PullRequestLockedPayloadDict",
    "PullRequestMilestonedPayloadDict",
    "PullRequestOpenedPayloadDict",
    "PullRequestPayloadDict",
    "PullRequestReadyForReviewPayloadDict",
    "PullRequestReopenedPayloadDict",
    "PullRequestReviewCommentCreatedPayloadDict",
    "PullRequestReviewCommentDeletedPayloadDict",
    "PullRequestReviewCommentEditedPayloadDict",
    "PullRequestReviewDismissedPayloadDict",
    "PullRequestReviewEditedPayloadDict",
    "PullRequestReviewSubmittedPayloadDict",
    "PullRequestReviewThreadResolvedPayloadDict",
    "PullRequestReviewThreadUnresolvedPayloadDict",
    "PullRequestSynchronizePayloadDict",
    "PullRequestUnassignedPayloadDict",
    "PullRequestUnlabeledPayloadDict",
    "PullRequestUnlockedPayloadDict",
    "PushPayloadDict",
    "RegistryPackagePublishedPayloadDict",
    "RegistryPackageUpdatedPayloadDict",
    "ReleaseCreatedPayloadDict",
    "ReleaseDeletedPayloadDict",
    "ReleaseEditedPayloadDict",
    "ReleasePrereleasedPayloadDict",
    "ReleasePublishedPayloadDict",
    "ReleaseReleasedPayloadDict",
    "ReleaseUnpublishedPayloadDict",
    "RepositoryArchivedPayloadDict",
    "RepositoryCreatedPayloadDict",
    "RepositoryDeletedPayloadDict",
    "RepositoryDispatchPayloadDict",
    "RepositoryEditedPayloadDict",
    "RepositoryImportPayloadDict",
    "RepositoryPrivatizedPayloadDict",
    "RepositoryPublicizedPayloadDict",
    "RepositoryRenamedPayloadDict",
    "RepositoryTransferredPayloadDict",
    "RepositoryUnarchivedPayloadDict",
    "RepositoryVulnerabilityAlertCreatePayloadDict",
    "RepositoryVulnerabilityAlertDismissPayloadDict",
    "RepositoryVulnerabilityAlertReopenPayloadDict",
    "RepositoryVulnerabilityAlertResolvePayloadDict",
    "SecretScanningAlertCreatedPayloadDict",
    "SecretScanningAlertLocationCreatedPayloadDict",
    "SecretScanningAlertReopenedPayloadDict",
    "SecretScanningAlertResolvedPayloadDict",
    "SecretScanningAlertRevokedPayloadDict",
    "SecurityAdvisoryPerformedPayloadDict",
    "SecurityAdvisoryPublishedPayloadDict",
    "SecurityAdvisoryUpdatedPayloadDict",
    "SecurityAdvisoryWithdrawnPayloadDict",
    "SponsorshipCancelledPayloadDict",
    "SponsorshipCreatedPayloadDict",
    "SponsorshipEditedPayloadDict",
    "SponsorshipPendingCancellationPayloadDict",
    "SponsorshipPendingTierChangePayloadDict",
    "SponsorshipTierChangedPayloadDict",
    "StarCreatedPayloadDict",
    "StarDeletedPayloadDict",
    "StatusPayloadDict",
    "TeamAddPayloadDict",
    "TeamAddedToRepositoryPayloadDict",
    "TeamCreatedPayloadDict",
    "TeamDeletedPayloadDict",
    "TeamEditedPayloadDict",
    "TeamRemovedFromRepositoryPayloadDict",
    "WatchStartedPayloadDict",
    "WebhookPayload",
    "WorkflowDispatchPayloadDict",
    "WorkflowJobCompletedPayloadDict",
    "WorkflowJobInProgressPayloadDict",
    "WorkflowJobQueuedPayloadDict",
    "WorkflowJobWaitingPayloadDict",
    "WorkflowRunCompletedPayloadDict",
    "WorkflowRunInProgressPayloadDict",
    "WorkflowRunRequestedPayloadDict",
]


class BranchProtectionConfigurationDisabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `disabled`."""

    action: Required[Literal["disabled"]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class BranchProtectionConfigurationEnabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `enabled`."""

    action: Required[Literal["enabled"]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class BranchProtectionRuleCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `created`."""

    action: Required[Literal["created"]]
    rule: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class BranchProtectionRuleDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    rule: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class BranchProtectionRuleEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    rule: Required[dict[str, Any]]
    changes: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckRunCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    check_run: Required[dict[str, Any]]
    requested_action: NotRequired[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckRunCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `created`."""

    action: Required[Literal["created"]]
    check_run: Required[dict[str, Any]]
    requested_action: NotRequired[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckRunRequestedActionPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `requested_action`."""

    action: Required[Literal["requested_action"]]
    check_run: Required[dict[str, Any]]
    requested_action: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckRunRerequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `rerequested`."""

    action: Required[Literal["rerequested"]]
    check_run: Required[dict[str, Any]]
    requested_action: NotRequired[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckSuiteCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    check_suite: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckSuiteRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    check_suite: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CheckSuiteRerequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `rerequested`."""

    action: Required[Literal["rerequested"]]
    check_suite: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertAppearedInBranchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `appeared_in_branch`."""

    action: Required[Literal["appeared_in_branch"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertClosedByUserPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `closed_by_user`."""

    action: Required[Literal["closed_by_user"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertFixedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `fixed`."""

    action: Required[Literal["fixed"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CodeScanningAlertReopenedByUserPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened_by_user`."""

    action: Required[Literal["reopened_by_user"]]
    alert: Required[dict[str, Any]]
    ref: Required[str]
    commit_oid: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CommitCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `commit_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CreatePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `create` webhook."""

    ref: Required[str]
    ref_type: Required[Literal["tag", "branch"]]
    master_branch: Required[str]
    description: Required[None | str]
    pusher_type: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class CustomPropertyCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `created`."""

    action: Required[Literal["created"]]
    definition: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: NotRequired[dict[str, Any]]


class CustomPropertyDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    definition: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: NotRequired[dict[str, Any]]


class CustomPropertyValuesUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property_values` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    installation: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    new_property_values: Required[list[dict[str, Any]]]
    old_property_values: Required[list[dict[str, Any]]]


class DeletePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `delete` webhook."""

    ref: Required[str]
    ref_type: Required[Literal["tag", "branch"]]
    pusher_type: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DependabotAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DependabotAlertDismissedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `dismissed`."""

    action: Required[Literal["dismissed"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DependabotAlertFixedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `fixed`."""

    action: Required[Literal["fixed"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DependabotAlertReintroducedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `reintroduced`."""

    action: Required[Literal["reintroduced"]]
    alert: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DependabotAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DeployKeyCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deploy_key` webhook with action `created`."""

    action: Required[Literal["created"]]
    key: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DeployKeyDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deploy_key` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    key: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DeploymentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment` webhook with action `created`."""

    action: Required[Literal["created"]]
    deployment: Required[dict[str, Any]]
    workflow: Required[None | dict[str, Any]]
    workflow_run: Required[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DeploymentProtectionRuleRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_protection_rule` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[dict[str, Any]]
    pull_requests: NotRequired[list[dict[str, Any]]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DeploymentReviewApprovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `approved`."""

    action: Required[Literal["approved"]]
    workflow_run: Required[dict[str, Any]]
    since: Required[str]
    workflow_job_run: NotRequired[dict[str, Any]]
    workflow_job_runs: NotRequired[list[dict[str, Any]]]
    reviewers: NotRequired[list[dict[str, Any]]]
    approver: NotRequired[dict[str, Any]]
    comment: NotRequired[str]
    repository: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class DeploymentReviewRejectedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `rejected`."""

    action: Required[Literal["rejected"]]
    workflow_run: Required[dict[str, Any]]
    since: Required[str]
    workflow_job_run: NotRequired[dict[str, Any]]
    workflow_job_runs: NotRequired[list[dict[str, Any]]]
    reviewers: NotRequired[list[dict[str, Any]]]
    approver: NotRequired[dict[str, Any]]
    comment: NotRequired[str]
    repository: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class DeploymentReviewRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    workflow_run: Required[None | dict[str, Any]]
    since: Required[str]
    workflow_job_run: Required[dict[str, Any]]
    environment: Required[str]
    reviewers: Required[list[dict[str, Any]]]
    requestor: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class DeploymentStatusCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_status` webhook with action `created`."""

    action: Required[Literal["created"]]
    deployment_status: Required[dict[str, Any]]
    deployment: Required[dict[str, Any]]
    check_run: NotRequired[dict[str, Any]]
    workflow_run: NotRequired[dict[str, Any]]
    workflow: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionAnsweredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `answered`."""

    action: Required[Literal["answered"]]
    discussion: Required[Any]
    answer: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionCategoryChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `category_changed`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["category_changed"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `created`."""

    action: Required[Literal["created"]]
    discussion: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `edited`."""

    changes: NotRequired[dict[str, Any]]
    action: Required[Literal["edited"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    discussion: Required[dict[str, Any]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    discussion: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionPinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `pinned`."""

    action: Required[Literal["pinned"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `transferred`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["transferred"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionUnansweredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unanswered`."""

    action: Required[Literal["unanswered"]]
    discussion: Required[Any]
    old_answer: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    discussion: Required[dict[str, Any]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    discussion: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionUnpinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unpinned`."""

    action: Required[Literal["unpinned"]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[dict[str, Any]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    comment: Required[dict[str, Any]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class DiscussionCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `edited`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["edited"]]
    comment: Required[dict[str, Any]]
    discussion: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ForkPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `fork` webhook."""

    forkee: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class GithubAppAuthorizationRevokedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `github_app_authorization` webhook with action `revoked`."""

    action: Required[Literal["revoked"]]
    sender: Required[dict[str, Any]]


class GollumPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `gollum` webhook."""

    pages: Required[list[dict[str, Any]]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class InstallationCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `created`."""

    action: Required[Literal["created"]]
    installation: Required[dict[str, Any]]
    repositories: NotRequired[list[dict[str, Any]]]
    requester: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class InstallationDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    installation: Required[dict[str, Any]]
    repositories: NotRequired[list[dict[str, Any]]]
    requester: NotRequired[None]
    sender: Required[dict[str, Any]]


class InstallationNewPermissionsAcceptedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `new_permissions_accepted`."""

    action: Required[Literal["new_permissions_accepted"]]
    installation: Required[dict[str, Any]]
    repositories: NotRequired[list[dict[str, Any]]]
    requester: NotRequired[None]
    sender: Required[dict[str, Any]]


class InstallationSuspendPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `suspend`."""

    action: Required[Literal["suspend"]]
    installation: Required[Any]
    repositories: NotRequired[list[dict[str, Any]]]
    requester: NotRequired[None]
    sender: Required[dict[str, Any]]


class InstallationUnsuspendPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `unsuspend`."""

    action: Required[Literal["unsuspend"]]
    installation: Required[Any]
    repositories: NotRequired[list[dict[str, Any]]]
    requester: NotRequired[None]
    sender: Required[dict[str, Any]]


class InstallationRepositoriesAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_repositories` webhook with action `added`."""

    action: Required[Literal["added"]]
    installation: Required[dict[str, Any]]
    repository_selection: Required[Literal["all", "selected"]]
    repositories_added: Required[list[dict[str, Any]]]
    repositories_removed: Required[list[dict[str, Any]]]
    requester: Required[None | dict[str, Any]]
    sender: Required[dict[str, Any]]


class InstallationRepositoriesRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_repositories` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    installation: Required[dict[str, Any]]
    repository_selection: Required[Literal["all", "selected"]]
    repositories_added: Required[list[dict[str, Any]]]
    repositories_removed: Required[list[dict[str, Any]]]
    requester: Required[None | dict[str, Any]]
    sender: Required[dict[str, Any]]


class InstallationTargetRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_target` webhook with action `renamed`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["renamed"]]
    account: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: NotRequired[dict[str, Any]]
    installation: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    target_type: Required[str]


class IssueCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    issue: Required[Any]
    comment: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssueCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    issue: Required[Any]
    comment: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssueCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    issue: Required[Any]
    comment: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesAssignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `assigned`."""

    action: Required[Literal["assigned"]]
    issue: Required[dict[str, Any]]
    assignee: NotRequired[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    issue: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    issue: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesDemilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `demilestoned`."""

    action: Required[Literal["demilestoned"]]
    issue: Required[Any]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    issue: Required[dict[str, Any]]
    label: NotRequired[dict[str, Any]]
    changes: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    issue: Required[dict[str, Any]]
    label: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    issue: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesMilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `milestoned`."""

    action: Required[Literal["milestoned"]]
    issue: Required[Any]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    changes: NotRequired[dict[str, Any]]
    issue: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesPinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `pinned`."""

    action: Required[Literal["pinned"]]
    issue: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    issue: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `transferred`."""

    action: Required[Literal["transferred"]]
    changes: Required[dict[str, Any]]
    issue: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesUnassignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unassigned`."""

    action: Required[Literal["unassigned"]]
    issue: Required[dict[str, Any]]
    assignee: NotRequired[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    issue: Required[dict[str, Any]]
    label: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    issue: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class IssuesUnpinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unpinned`."""

    action: Required[Literal["unpinned"]]
    issue: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class LabelCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `created`."""

    action: Required[Literal["created"]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class LabelDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class LabelEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    label: Required[dict[str, Any]]
    changes: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MarketplacePurchaseCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `cancelled`."""

    action: Required[Literal["cancelled"]]
    effective_date: Required[str]
    sender: Required[dict[str, Any]]
    marketplace_purchase: Required[Any]
    previous_marketplace_purchase: NotRequired[dict[str, Any]]


class MarketplacePurchaseChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `changed`."""

    action: Required[Literal["changed"]]
    effective_date: Required[str]
    sender: Required[dict[str, Any]]
    marketplace_purchase: Required[Any]
    previous_marketplace_purchase: NotRequired[dict[str, Any]]


class MarketplacePurchasePendingChangePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change`."""

    action: Required[Literal["pending_change"]]
    effective_date: Required[str]
    sender: Required[dict[str, Any]]
    marketplace_purchase: Required[Any]
    previous_marketplace_purchase: NotRequired[dict[str, Any]]


class MarketplacePurchasePendingChangeCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change_cancelled`."""

    action: Required[Literal["pending_change_cancelled"]]
    effective_date: Required[str]
    sender: Required[dict[str, Any]]
    marketplace_purchase: Required[Any]
    previous_marketplace_purchase: NotRequired[dict[str, Any]]


class MarketplacePurchasePurchasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `purchased`."""

    action: Required[Literal["purchased"]]
    effective_date: Required[str]
    sender: Required[dict[str, Any]]
    marketplace_purchase: Required[Any]
    previous_marketplace_purchase: NotRequired[dict[str, Any]]


class MemberAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `added`."""

    action: Required[Literal["added"]]
    changes: NotRequired[dict[str, Any]]
    member: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class MemberEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    member: Required[dict[str, Any]]
    changes: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class MemberRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    member: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class MembershipAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `membership` webhook with action `added`."""

    action: Required[Literal["added"]]
    scope: Required[Literal["team"]]
    member: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    team: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class MembershipRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `membership` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    scope: Required[Literal["team", "organization"]]
    member: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    team: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class MergeGroupChecksRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `merge_group` webhook with action `checks_requested`."""

    action: Required[Literal["checks_requested"]]
    merge_group: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MergeGroupDestroyedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `merge_group` webhook with action `destroyed`."""

    action: Required[Literal["destroyed"]]
    merge_group: Required[dict[str, Any]]
    reason: Required[Literal["dequeued", "invalidated", "merged"]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MetaDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `meta` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    hook_id: Required[int]
    hook: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class MilestoneClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    milestone: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MilestoneCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `created`."""

    action: Required[Literal["created"]]
    milestone: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MilestoneDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MilestoneEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class MilestoneOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    milestone: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class OrgBlockBlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `org_block` webhook with action `blocked`."""

    action: Required[Literal["blocked"]]
    blocked_user: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrgBlockUnblockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `org_block` webhook with action `unblocked`."""

    action: Required[Literal["unblocked"]]
    blocked_user: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrganizationDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    membership: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrganizationMemberAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_added`."""

    action: Required[Literal["member_added"]]
    membership: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrganizationMemberInvitedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_invited`."""

    action: Required[Literal["member_invited"]]
    invitation: Required[dict[str, Any]]
    user: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrganizationMemberRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_removed`."""

    action: Required[Literal["member_removed"]]
    membership: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class OrganizationRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `renamed`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["renamed"]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class PackagePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `package` webhook with action `published`."""

    action: Required[Literal["published"]]
    package: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PackageUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `package` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    package: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PageBuildPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `page_build` webhook."""

    id: Required[int]
    build: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PingPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `ping` webhook."""

    zen: Required[str]
    hook_id: Required[int]
    hook: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    project: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `created`."""

    action: Required[Literal["created"]]
    project: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    project: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[dict[str, Any]]
    project: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    project: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectCardConvertedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `converted`."""

    action: Required[Literal["converted"]]
    changes: Required[dict[str, Any]]
    project_card: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectCardCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `created`."""

    action: Required[Literal["created"]]
    project_card: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectCardDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    project_card: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectCardEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    project_card: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectCardMovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `moved`."""

    action: Required[Literal["moved"]]
    changes: NotRequired[dict[str, Any]]
    project_card: Required[Any]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectColumnCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `created`."""

    action: Required[Literal["created"]]
    project_column: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectColumnDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    project_column: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectColumnEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    project_column: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectColumnMovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `moved`."""

    action: Required[Literal["moved"]]
    project_column: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ProjectsV2ItemArchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `archived`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["archived"]]
    projects_v2_item: Required[Any]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemConvertedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `converted`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["converted"]]
    projects_v2_item: Required[Any]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `created`."""

    action: Required[Literal["created"]]
    projects_v2_item: Required[Any]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    projects_v2_item: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `edited`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["edited"]]
    projects_v2_item: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemReorderedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `reordered`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["reordered"]]
    projects_v2_item: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class ProjectsV2ItemRestoredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `restored`."""

    changes: Required[dict[str, Any]]
    action: Required[Literal["restored"]]
    projects_v2_item: Required[Any]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class PublicPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `public` webhook."""

    repository: Required[Any]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PullRequestPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook."""


class PullRequestAssignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `assigned`."""

    action: Required[Literal["assigned"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    assignee: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestAutoMergeDisabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_disabled`."""

    action: Required[Literal["auto_merge_disabled"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    reason: Required[str]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestAutoMergeEnabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_enabled`."""

    action: Required[Literal["auto_merge_enabled"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    reason: Required[str]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    number: Required[int]
    pull_request: Required[Any]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestConvertedToDraftPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `converted_to_draft`."""

    action: Required[Literal["converted_to_draft"]]
    number: Required[int]
    pull_request: Required[Any]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestDemilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `demilestoned`."""

    action: Required[Literal["demilestoned"]]
    number: Required[int]
    pull_request: Required[Any]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PullRequestDequeuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `dequeued`."""

    action: Required[Literal["dequeued"]]
    number: Required[int]
    reason: Required[str]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    number: Required[int]
    changes: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestEnqueuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `enqueued`."""

    action: Required[Literal["enqueued"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestMilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `milestoned`."""

    action: Required[Literal["milestoned"]]
    number: Required[int]
    pull_request: Required[Any]
    milestone: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class PullRequestOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    number: Required[int]
    pull_request: Required[Any]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReadyForReviewPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `ready_for_review`."""

    action: Required[Literal["ready_for_review"]]
    number: Required[int]
    pull_request: Required[Any]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    number: Required[int]
    pull_request: Required[Any]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestSynchronizePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `synchronize`."""

    action: Required[Literal["synchronize"]]
    number: Required[int]
    before: Required[str]
    after: Required[str]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestUnassignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unassigned`."""

    action: Required[Literal["unassigned"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    assignee: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    label: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    number: Required[int]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewDismissedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `dismissed`."""

    action: Required[Literal["dismissed"]]
    review: Required[Any]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    review: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewSubmittedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `submitted`."""

    action: Required[Literal["submitted"]]
    review: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    comment: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    comment: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewThreadResolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `resolved`."""

    action: Required[Literal["resolved"]]
    thread: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PullRequestReviewThreadUnresolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `unresolved`."""

    action: Required[Literal["unresolved"]]
    thread: Required[dict[str, Any]]
    pull_request: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class PushPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `push` webhook."""

    ref: Required[str]
    before: Required[str]
    after: Required[str]
    created: Required[bool]
    deleted: Required[bool]
    forced: Required[bool]
    base_ref: Required[None | str]
    compare: Required[str]
    commits: Required[list[dict[str, Any]]]
    head_commit: Required[None | dict[str, Any]]
    repository: Required[dict[str, Any]]
    pusher: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RegistryPackagePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `registry_package` webhook with action `published`."""

    action: Required[Literal["published"]]
    registry_package: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RegistryPackageUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `registry_package` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    registry_package: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleaseCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `created`."""

    action: Required[Literal["created"]]
    release: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleaseDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    release: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleaseEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    release: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleasePrereleasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `prereleased`."""

    action: Required[Literal["prereleased"]]
    release: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleasePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `published`."""

    action: Required[Literal["published"]]
    release: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleaseReleasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `released`."""

    action: Required[Literal["released"]]
    release: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class ReleaseUnpublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `unpublished`."""

    action: Required[Literal["unpublished"]]
    release: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryArchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `archived`."""

    action: Required[Literal["archived"]]
    repository: Required[Any]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `created`."""

    action: Required[Literal["created"]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryPrivatizedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `privatized`."""

    action: Required[Literal["privatized"]]
    repository: Required[Any]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryPublicizedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `publicized`."""

    action: Required[Literal["publicized"]]
    repository: Required[Any]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `renamed`."""

    action: Required[Literal["renamed"]]
    changes: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `transferred`."""

    action: Required[Literal["transferred"]]
    changes: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryUnarchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `unarchived`."""

    action: Required[Literal["unarchived"]]
    repository: Required[Any]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryDispatchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_dispatch` webhook."""

    action: Required[str]
    branch: Required[str]
    client_payload: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryImportPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_import` webhook."""

    status: Required[Literal["success", "cancelled", "failure"]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryVulnerabilityAlertCreatePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `create`."""

    action: Required[Literal["create"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryVulnerabilityAlertDismissPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `dismiss`."""

    action: Required[Literal["dismiss"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryVulnerabilityAlertReopenPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `reopen`."""

    action: Required[Literal["reopen"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class RepositoryVulnerabilityAlertResolvePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `resolve`."""

    action: Required[Literal["resolve"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class SecretScanningAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class SecretScanningAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SecretScanningAlertResolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `resolved`."""

    action: Required[Literal["resolved"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SecretScanningAlertRevokedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `revoked`."""

    action: Required[Literal["revoked"]]
    alert: Required[Any]
    repository: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SecretScanningAlertLocationCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert_location` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[dict[str, Any]]
    location: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class SecurityAdvisoryPerformedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `performed`."""

    action: Required[Literal["performed"]]
    security_advisory: Required[dict[str, Any]]


class SecurityAdvisoryPublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `published`."""

    action: Required[Literal["published"]]
    security_advisory: Required[dict[str, Any]]


class SecurityAdvisoryUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    security_advisory: Required[dict[str, Any]]


class SecurityAdvisoryWithdrawnPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `withdrawn`."""

    action: Required[Literal["withdrawn"]]
    security_advisory: Required[dict[str, Any]]


class SponsorshipCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `cancelled`."""

    action: Required[Literal["cancelled"]]
    sponsorship: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SponsorshipCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `created`."""

    action: Required[Literal["created"]]
    sponsorship: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SponsorshipEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    sponsorship: Required[dict[str, Any]]
    changes: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SponsorshipPendingCancellationPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `pending_cancellation`."""

    action: Required[Literal["pending_cancellation"]]
    sponsorship: Required[dict[str, Any]]
    effective_date: NotRequired[str]
    sender: Required[dict[str, Any]]


class SponsorshipPendingTierChangePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `pending_tier_change`."""

    action: Required[Literal["pending_tier_change"]]
    sponsorship: Required[dict[str, Any]]
    effective_date: NotRequired[str]
    changes: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class SponsorshipTierChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `tier_changed`."""

    action: Required[Literal["tier_changed"]]
    sponsorship: Required[dict[str, Any]]
    changes: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]


class StarCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `star` webhook with action `created`."""

    action: Required[Literal["created"]]
    starred_at: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class StarDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `star` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    starred_at: Required[None]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class StatusPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `status` webhook."""

    id: Required[int]
    sha: Required[str]
    name: Required[str]
    avatar_url: NotRequired[None | str]
    target_url: Required[None | str]
    context: Required[str]
    description: Required[None | str]
    state: Required[Literal["pending", "success", "failure", "error"]]
    commit: Required[dict[str, Any]]
    branches: Required[list[dict[str, Any]]]
    created_at: Required[str]
    updated_at: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class TeamAddedToRepositoryPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `added_to_repository`."""

    action: Required[Literal["added_to_repository"]]
    team: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class TeamCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `created`."""

    action: Required[Literal["created"]]
    team: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class TeamDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    team: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class TeamEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[dict[str, Any]]
    team: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class TeamRemovedFromRepositoryPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `removed_from_repository`."""

    action: Required[Literal["removed_from_repository"]]
    team: Required[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    sender: Required[dict[str, Any]]
    organization: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class TeamAddPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team_add` webhook."""

    team: Required[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: Required[dict[str, Any]]


class WatchStartedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `watch` webhook with action `started`."""

    action: Required[Literal["started"]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]


class WorkflowDispatchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_dispatch` webhook."""

    inputs: Required[None | dict[str, Any]]
    ref: Required[str]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    organization: NotRequired[dict[str, Any]]
    workflow: Required[str]


class WorkflowJobCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    deployment: NotRequired[dict[str, Any]]
    workflow_job: Required[Any]


class WorkflowJobInProgressPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `in_progress`."""

    action: Required[Literal["in_progress"]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    deployment: NotRequired[dict[str, Any]]
    workflow_job: Required[Any]


class WorkflowJobQueuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `queued`."""

    action: Required[Literal["queued"]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    deployment: NotRequired[dict[str, Any]]
    workflow_job: Required[Any]


class WorkflowJobWaitingPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `waiting`."""

    action: Required[Literal["waiting"]]
    organization: NotRequired[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    deployment: NotRequired[dict[str, Any]]
    workflow_job: Required[Any]


class WorkflowRunCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    organization: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    workflow: Required[dict[str, Any]]
    workflow_run: Required[Any]
    installation: NotRequired[dict[str, Any]]


class WorkflowRunInProgressPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `in_progress`."""

    action: Required[Literal["in_progress"]]
    organization: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    workflow: Required[dict[str, Any]]
    workflow_run: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


class WorkflowRunRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    organization: NotRequired[dict[str, Any]]
    repository: Required[dict[str, Any]]
    sender: Required[dict[str, Any]]
    workflow: Required[dict[str, Any]]
    workflow_run: Required[dict[str, Any]]
    installation: NotRequired[dict[str, Any]]


type WebhookPayload = dict[str, Any]
