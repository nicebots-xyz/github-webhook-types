# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Pydantic models generated from Octokit's GitHub webhook schema.

Do not edit this module by hand. Run `pdm run generate` instead.
"""

from pydantic import BaseModel

from github_webhook_types._model_factory import build_model_from_typeddict
from github_webhook_types.generated.typed_dicts import (
    BranchProtectionConfigurationDisabledPayloadDict,
    BranchProtectionConfigurationEnabledPayloadDict,
    BranchProtectionRuleCreatedPayloadDict,
    BranchProtectionRuleDeletedPayloadDict,
    BranchProtectionRuleEditedPayloadDict,
    CheckRunCompletedPayloadDict,
    CheckRunCreatedPayloadDict,
    CheckRunRequestedActionPayloadDict,
    CheckRunRerequestedPayloadDict,
    CheckSuiteCompletedPayloadDict,
    CheckSuiteRequestedPayloadDict,
    CheckSuiteRerequestedPayloadDict,
    CodeScanningAlertAppearedInBranchPayloadDict,
    CodeScanningAlertClosedByUserPayloadDict,
    CodeScanningAlertCreatedPayloadDict,
    CodeScanningAlertFixedPayloadDict,
    CodeScanningAlertReopenedByUserPayloadDict,
    CodeScanningAlertReopenedPayloadDict,
    CommitCommentCreatedPayloadDict,
    CreatePayloadDict,
    CustomPropertyCreatedPayloadDict,
    CustomPropertyDeletedPayloadDict,
    CustomPropertyValuesUpdatedPayloadDict,
    DeletePayloadDict,
    DependabotAlertCreatedPayloadDict,
    DependabotAlertDismissedPayloadDict,
    DependabotAlertFixedPayloadDict,
    DependabotAlertReintroducedPayloadDict,
    DependabotAlertReopenedPayloadDict,
    DeployKeyCreatedPayloadDict,
    DeployKeyDeletedPayloadDict,
    DeploymentCreatedPayloadDict,
    DeploymentProtectionRuleRequestedPayloadDict,
    DeploymentReviewApprovedPayloadDict,
    DeploymentReviewRejectedPayloadDict,
    DeploymentReviewRequestedPayloadDict,
    DeploymentStatusCreatedPayloadDict,
    DiscussionAnsweredPayloadDict,
    DiscussionCategoryChangedPayloadDict,
    DiscussionCommentCreatedPayloadDict,
    DiscussionCommentDeletedPayloadDict,
    DiscussionCommentEditedPayloadDict,
    DiscussionCreatedPayloadDict,
    DiscussionDeletedPayloadDict,
    DiscussionEditedPayloadDict,
    DiscussionLabeledPayloadDict,
    DiscussionLockedPayloadDict,
    DiscussionPinnedPayloadDict,
    DiscussionTransferredPayloadDict,
    DiscussionUnansweredPayloadDict,
    DiscussionUnlabeledPayloadDict,
    DiscussionUnlockedPayloadDict,
    DiscussionUnpinnedPayloadDict,
    ForkPayloadDict,
    GithubAppAuthorizationRevokedPayloadDict,
    GollumPayloadDict,
    InstallationCreatedPayloadDict,
    InstallationDeletedPayloadDict,
    InstallationNewPermissionsAcceptedPayloadDict,
    InstallationRepositoriesAddedPayloadDict,
    InstallationRepositoriesRemovedPayloadDict,
    InstallationSuspendPayloadDict,
    InstallationTargetRenamedPayloadDict,
    InstallationUnsuspendPayloadDict,
    IssueCommentCreatedPayloadDict,
    IssueCommentDeletedPayloadDict,
    IssueCommentEditedPayloadDict,
    IssuesAssignedPayloadDict,
    IssuesClosedPayloadDict,
    IssuesDeletedPayloadDict,
    IssuesDemilestonedPayloadDict,
    IssuesEditedPayloadDict,
    IssuesLabeledPayloadDict,
    IssuesLockedPayloadDict,
    IssuesMilestonedPayloadDict,
    IssuesOpenedPayloadDict,
    IssuesPinnedPayloadDict,
    IssuesReopenedPayloadDict,
    IssuesTransferredPayloadDict,
    IssuesUnassignedPayloadDict,
    IssuesUnlabeledPayloadDict,
    IssuesUnlockedPayloadDict,
    IssuesUnpinnedPayloadDict,
    LabelCreatedPayloadDict,
    LabelDeletedPayloadDict,
    LabelEditedPayloadDict,
    MarketplacePurchaseCancelledPayloadDict,
    MarketplacePurchaseChangedPayloadDict,
    MarketplacePurchasePendingChangeCancelledPayloadDict,
    MarketplacePurchasePendingChangePayloadDict,
    MarketplacePurchasePurchasedPayloadDict,
    MemberAddedPayloadDict,
    MemberEditedPayloadDict,
    MemberRemovedPayloadDict,
    MembershipAddedPayloadDict,
    MembershipRemovedPayloadDict,
    MergeGroupChecksRequestedPayloadDict,
    MergeGroupDestroyedPayloadDict,
    MetaDeletedPayloadDict,
    MilestoneClosedPayloadDict,
    MilestoneCreatedPayloadDict,
    MilestoneDeletedPayloadDict,
    MilestoneEditedPayloadDict,
    MilestoneOpenedPayloadDict,
    OrganizationDeletedPayloadDict,
    OrganizationMemberAddedPayloadDict,
    OrganizationMemberInvitedPayloadDict,
    OrganizationMemberRemovedPayloadDict,
    OrganizationRenamedPayloadDict,
    OrgBlockBlockedPayloadDict,
    OrgBlockUnblockedPayloadDict,
    PackagePublishedPayloadDict,
    PackageUpdatedPayloadDict,
    PageBuildPayloadDict,
    PingPayloadDict,
    ProjectCardConvertedPayloadDict,
    ProjectCardCreatedPayloadDict,
    ProjectCardDeletedPayloadDict,
    ProjectCardEditedPayloadDict,
    ProjectCardMovedPayloadDict,
    ProjectClosedPayloadDict,
    ProjectColumnCreatedPayloadDict,
    ProjectColumnDeletedPayloadDict,
    ProjectColumnEditedPayloadDict,
    ProjectColumnMovedPayloadDict,
    ProjectCreatedPayloadDict,
    ProjectDeletedPayloadDict,
    ProjectEditedPayloadDict,
    ProjectReopenedPayloadDict,
    ProjectsV2ItemArchivedPayloadDict,
    ProjectsV2ItemConvertedPayloadDict,
    ProjectsV2ItemCreatedPayloadDict,
    ProjectsV2ItemDeletedPayloadDict,
    ProjectsV2ItemEditedPayloadDict,
    ProjectsV2ItemReorderedPayloadDict,
    ProjectsV2ItemRestoredPayloadDict,
    PublicPayloadDict,
    PullRequestAssignedPayloadDict,
    PullRequestAutoMergeDisabledPayloadDict,
    PullRequestAutoMergeEnabledPayloadDict,
    PullRequestClosedPayloadDict,
    PullRequestConvertedToDraftPayloadDict,
    PullRequestDemilestonedPayloadDict,
    PullRequestDequeuedPayloadDict,
    PullRequestEditedPayloadDict,
    PullRequestEnqueuedPayloadDict,
    PullRequestLabeledPayloadDict,
    PullRequestLockedPayloadDict,
    PullRequestMilestonedPayloadDict,
    PullRequestOpenedPayloadDict,
    PullRequestPayloadDict,
    PullRequestReadyForReviewPayloadDict,
    PullRequestReopenedPayloadDict,
    PullRequestReviewCommentCreatedPayloadDict,
    PullRequestReviewCommentDeletedPayloadDict,
    PullRequestReviewCommentEditedPayloadDict,
    PullRequestReviewDismissedPayloadDict,
    PullRequestReviewEditedPayloadDict,
    PullRequestReviewSubmittedPayloadDict,
    PullRequestReviewThreadResolvedPayloadDict,
    PullRequestReviewThreadUnresolvedPayloadDict,
    PullRequestSynchronizePayloadDict,
    PullRequestUnassignedPayloadDict,
    PullRequestUnlabeledPayloadDict,
    PullRequestUnlockedPayloadDict,
    PushPayloadDict,
    RegistryPackagePublishedPayloadDict,
    RegistryPackageUpdatedPayloadDict,
    ReleaseCreatedPayloadDict,
    ReleaseDeletedPayloadDict,
    ReleaseEditedPayloadDict,
    ReleasePrereleasedPayloadDict,
    ReleasePublishedPayloadDict,
    ReleaseReleasedPayloadDict,
    ReleaseUnpublishedPayloadDict,
    RepositoryArchivedPayloadDict,
    RepositoryCreatedPayloadDict,
    RepositoryDeletedPayloadDict,
    RepositoryDispatchPayloadDict,
    RepositoryEditedPayloadDict,
    RepositoryImportPayloadDict,
    RepositoryPrivatizedPayloadDict,
    RepositoryPublicizedPayloadDict,
    RepositoryRenamedPayloadDict,
    RepositoryTransferredPayloadDict,
    RepositoryUnarchivedPayloadDict,
    RepositoryVulnerabilityAlertCreatePayloadDict,
    RepositoryVulnerabilityAlertDismissPayloadDict,
    RepositoryVulnerabilityAlertReopenPayloadDict,
    RepositoryVulnerabilityAlertResolvePayloadDict,
    SecretScanningAlertCreatedPayloadDict,
    SecretScanningAlertLocationCreatedPayloadDict,
    SecretScanningAlertReopenedPayloadDict,
    SecretScanningAlertResolvedPayloadDict,
    SecretScanningAlertRevokedPayloadDict,
    SecurityAdvisoryPerformedPayloadDict,
    SecurityAdvisoryPublishedPayloadDict,
    SecurityAdvisoryUpdatedPayloadDict,
    SecurityAdvisoryWithdrawnPayloadDict,
    SponsorshipCancelledPayloadDict,
    SponsorshipCreatedPayloadDict,
    SponsorshipEditedPayloadDict,
    SponsorshipPendingCancellationPayloadDict,
    SponsorshipPendingTierChangePayloadDict,
    SponsorshipTierChangedPayloadDict,
    StarCreatedPayloadDict,
    StarDeletedPayloadDict,
    StatusPayloadDict,
    TeamAddedToRepositoryPayloadDict,
    TeamAddPayloadDict,
    TeamCreatedPayloadDict,
    TeamDeletedPayloadDict,
    TeamEditedPayloadDict,
    TeamRemovedFromRepositoryPayloadDict,
    WatchStartedPayloadDict,
    WorkflowDispatchPayloadDict,
    WorkflowJobCompletedPayloadDict,
    WorkflowJobInProgressPayloadDict,
    WorkflowJobQueuedPayloadDict,
    WorkflowJobWaitingPayloadDict,
    WorkflowRunCompletedPayloadDict,
    WorkflowRunInProgressPayloadDict,
    WorkflowRunRequestedPayloadDict,
)

__all__ = [
    "BranchProtectionConfigurationDisabledPayload",
    "BranchProtectionConfigurationEnabledPayload",
    "BranchProtectionRuleCreatedPayload",
    "BranchProtectionRuleDeletedPayload",
    "BranchProtectionRuleEditedPayload",
    "CheckRunCompletedPayload",
    "CheckRunCreatedPayload",
    "CheckRunRequestedActionPayload",
    "CheckRunRerequestedPayload",
    "CheckSuiteCompletedPayload",
    "CheckSuiteRequestedPayload",
    "CheckSuiteRerequestedPayload",
    "CodeScanningAlertAppearedInBranchPayload",
    "CodeScanningAlertClosedByUserPayload",
    "CodeScanningAlertCreatedPayload",
    "CodeScanningAlertFixedPayload",
    "CodeScanningAlertReopenedByUserPayload",
    "CodeScanningAlertReopenedPayload",
    "CommitCommentCreatedPayload",
    "CreatePayload",
    "CustomPropertyCreatedPayload",
    "CustomPropertyDeletedPayload",
    "CustomPropertyValuesUpdatedPayload",
    "DeletePayload",
    "DependabotAlertCreatedPayload",
    "DependabotAlertDismissedPayload",
    "DependabotAlertFixedPayload",
    "DependabotAlertReintroducedPayload",
    "DependabotAlertReopenedPayload",
    "DeployKeyCreatedPayload",
    "DeployKeyDeletedPayload",
    "DeploymentCreatedPayload",
    "DeploymentProtectionRuleRequestedPayload",
    "DeploymentReviewApprovedPayload",
    "DeploymentReviewRejectedPayload",
    "DeploymentReviewRequestedPayload",
    "DeploymentStatusCreatedPayload",
    "DiscussionAnsweredPayload",
    "DiscussionCategoryChangedPayload",
    "DiscussionCommentCreatedPayload",
    "DiscussionCommentDeletedPayload",
    "DiscussionCommentEditedPayload",
    "DiscussionCreatedPayload",
    "DiscussionDeletedPayload",
    "DiscussionEditedPayload",
    "DiscussionLabeledPayload",
    "DiscussionLockedPayload",
    "DiscussionPinnedPayload",
    "DiscussionTransferredPayload",
    "DiscussionUnansweredPayload",
    "DiscussionUnlabeledPayload",
    "DiscussionUnlockedPayload",
    "DiscussionUnpinnedPayload",
    "ForkPayload",
    "GithubAppAuthorizationRevokedPayload",
    "GollumPayload",
    "InstallationCreatedPayload",
    "InstallationDeletedPayload",
    "InstallationNewPermissionsAcceptedPayload",
    "InstallationRepositoriesAddedPayload",
    "InstallationRepositoriesRemovedPayload",
    "InstallationSuspendPayload",
    "InstallationTargetRenamedPayload",
    "InstallationUnsuspendPayload",
    "IssueCommentCreatedPayload",
    "IssueCommentDeletedPayload",
    "IssueCommentEditedPayload",
    "IssuesAssignedPayload",
    "IssuesClosedPayload",
    "IssuesDeletedPayload",
    "IssuesDemilestonedPayload",
    "IssuesEditedPayload",
    "IssuesLabeledPayload",
    "IssuesLockedPayload",
    "IssuesMilestonedPayload",
    "IssuesOpenedPayload",
    "IssuesPinnedPayload",
    "IssuesReopenedPayload",
    "IssuesTransferredPayload",
    "IssuesUnassignedPayload",
    "IssuesUnlabeledPayload",
    "IssuesUnlockedPayload",
    "IssuesUnpinnedPayload",
    "LabelCreatedPayload",
    "LabelDeletedPayload",
    "LabelEditedPayload",
    "MarketplacePurchaseCancelledPayload",
    "MarketplacePurchaseChangedPayload",
    "MarketplacePurchasePendingChangeCancelledPayload",
    "MarketplacePurchasePendingChangePayload",
    "MarketplacePurchasePurchasedPayload",
    "MemberAddedPayload",
    "MemberEditedPayload",
    "MemberRemovedPayload",
    "MembershipAddedPayload",
    "MembershipRemovedPayload",
    "MergeGroupChecksRequestedPayload",
    "MergeGroupDestroyedPayload",
    "MetaDeletedPayload",
    "MilestoneClosedPayload",
    "MilestoneCreatedPayload",
    "MilestoneDeletedPayload",
    "MilestoneEditedPayload",
    "MilestoneOpenedPayload",
    "OrgBlockBlockedPayload",
    "OrgBlockUnblockedPayload",
    "OrganizationDeletedPayload",
    "OrganizationMemberAddedPayload",
    "OrganizationMemberInvitedPayload",
    "OrganizationMemberRemovedPayload",
    "OrganizationRenamedPayload",
    "PackagePublishedPayload",
    "PackageUpdatedPayload",
    "PageBuildPayload",
    "PingPayload",
    "ProjectCardConvertedPayload",
    "ProjectCardCreatedPayload",
    "ProjectCardDeletedPayload",
    "ProjectCardEditedPayload",
    "ProjectCardMovedPayload",
    "ProjectClosedPayload",
    "ProjectColumnCreatedPayload",
    "ProjectColumnDeletedPayload",
    "ProjectColumnEditedPayload",
    "ProjectColumnMovedPayload",
    "ProjectCreatedPayload",
    "ProjectDeletedPayload",
    "ProjectEditedPayload",
    "ProjectReopenedPayload",
    "ProjectsV2ItemArchivedPayload",
    "ProjectsV2ItemConvertedPayload",
    "ProjectsV2ItemCreatedPayload",
    "ProjectsV2ItemDeletedPayload",
    "ProjectsV2ItemEditedPayload",
    "ProjectsV2ItemReorderedPayload",
    "ProjectsV2ItemRestoredPayload",
    "PublicPayload",
    "PullRequestAssignedPayload",
    "PullRequestAutoMergeDisabledPayload",
    "PullRequestAutoMergeEnabledPayload",
    "PullRequestClosedPayload",
    "PullRequestConvertedToDraftPayload",
    "PullRequestDemilestonedPayload",
    "PullRequestDequeuedPayload",
    "PullRequestEditedPayload",
    "PullRequestEnqueuedPayload",
    "PullRequestLabeledPayload",
    "PullRequestLockedPayload",
    "PullRequestMilestonedPayload",
    "PullRequestOpenedPayload",
    "PullRequestPayload",
    "PullRequestReadyForReviewPayload",
    "PullRequestReopenedPayload",
    "PullRequestReviewCommentCreatedPayload",
    "PullRequestReviewCommentDeletedPayload",
    "PullRequestReviewCommentEditedPayload",
    "PullRequestReviewDismissedPayload",
    "PullRequestReviewEditedPayload",
    "PullRequestReviewSubmittedPayload",
    "PullRequestReviewThreadResolvedPayload",
    "PullRequestReviewThreadUnresolvedPayload",
    "PullRequestSynchronizePayload",
    "PullRequestUnassignedPayload",
    "PullRequestUnlabeledPayload",
    "PullRequestUnlockedPayload",
    "PushPayload",
    "RegistryPackagePublishedPayload",
    "RegistryPackageUpdatedPayload",
    "ReleaseCreatedPayload",
    "ReleaseDeletedPayload",
    "ReleaseEditedPayload",
    "ReleasePrereleasedPayload",
    "ReleasePublishedPayload",
    "ReleaseReleasedPayload",
    "ReleaseUnpublishedPayload",
    "RepositoryArchivedPayload",
    "RepositoryCreatedPayload",
    "RepositoryDeletedPayload",
    "RepositoryDispatchPayload",
    "RepositoryEditedPayload",
    "RepositoryImportPayload",
    "RepositoryPrivatizedPayload",
    "RepositoryPublicizedPayload",
    "RepositoryRenamedPayload",
    "RepositoryTransferredPayload",
    "RepositoryUnarchivedPayload",
    "RepositoryVulnerabilityAlertCreatePayload",
    "RepositoryVulnerabilityAlertDismissPayload",
    "RepositoryVulnerabilityAlertReopenPayload",
    "RepositoryVulnerabilityAlertResolvePayload",
    "SecretScanningAlertCreatedPayload",
    "SecretScanningAlertLocationCreatedPayload",
    "SecretScanningAlertReopenedPayload",
    "SecretScanningAlertResolvedPayload",
    "SecretScanningAlertRevokedPayload",
    "SecurityAdvisoryPerformedPayload",
    "SecurityAdvisoryPublishedPayload",
    "SecurityAdvisoryUpdatedPayload",
    "SecurityAdvisoryWithdrawnPayload",
    "SponsorshipCancelledPayload",
    "SponsorshipCreatedPayload",
    "SponsorshipEditedPayload",
    "SponsorshipPendingCancellationPayload",
    "SponsorshipPendingTierChangePayload",
    "SponsorshipTierChangedPayload",
    "StarCreatedPayload",
    "StarDeletedPayload",
    "StatusPayload",
    "TeamAddPayload",
    "TeamAddedToRepositoryPayload",
    "TeamCreatedPayload",
    "TeamDeletedPayload",
    "TeamEditedPayload",
    "TeamRemovedFromRepositoryPayload",
    "WatchStartedPayload",
    "WebhookPayloadModel",
    "WorkflowDispatchPayload",
    "WorkflowJobCompletedPayload",
    "WorkflowJobInProgressPayload",
    "WorkflowJobQueuedPayload",
    "WorkflowJobWaitingPayload",
    "WorkflowRunCompletedPayload",
    "WorkflowRunInProgressPayload",
    "WorkflowRunRequestedPayload",
]

BranchProtectionConfigurationDisabledPayload = build_model_from_typeddict(
    "BranchProtectionConfigurationDisabledPayload",
    BranchProtectionConfigurationDisabledPayloadDict,
    doc="Pydantic model for the GitHub `branch_protection_configuration` webhook with action `disabled`.",
)
BranchProtectionConfigurationEnabledPayload = build_model_from_typeddict(
    "BranchProtectionConfigurationEnabledPayload",
    BranchProtectionConfigurationEnabledPayloadDict,
    doc="Pydantic model for the GitHub `branch_protection_configuration` webhook with action `enabled`.",
)
BranchProtectionRuleCreatedPayload = build_model_from_typeddict(
    "BranchProtectionRuleCreatedPayload",
    BranchProtectionRuleCreatedPayloadDict,
    doc="Pydantic model for the GitHub `branch_protection_rule` webhook with action `created`.",
)
BranchProtectionRuleDeletedPayload = build_model_from_typeddict(
    "BranchProtectionRuleDeletedPayload",
    BranchProtectionRuleDeletedPayloadDict,
    doc="Pydantic model for the GitHub `branch_protection_rule` webhook with action `deleted`.",
)
BranchProtectionRuleEditedPayload = build_model_from_typeddict(
    "BranchProtectionRuleEditedPayload",
    BranchProtectionRuleEditedPayloadDict,
    doc="Pydantic model for the GitHub `branch_protection_rule` webhook with action `edited`.",
)
CheckRunCompletedPayload = build_model_from_typeddict(
    "CheckRunCompletedPayload",
    CheckRunCompletedPayloadDict,
    doc="Pydantic model for the GitHub `check_run` webhook with action `completed`.",
)
CheckRunCreatedPayload = build_model_from_typeddict(
    "CheckRunCreatedPayload",
    CheckRunCreatedPayloadDict,
    doc="Pydantic model for the GitHub `check_run` webhook with action `created`.",
)
CheckRunRequestedActionPayload = build_model_from_typeddict(
    "CheckRunRequestedActionPayload",
    CheckRunRequestedActionPayloadDict,
    doc="Pydantic model for the GitHub `check_run` webhook with action `requested_action`.",
)
CheckRunRerequestedPayload = build_model_from_typeddict(
    "CheckRunRerequestedPayload",
    CheckRunRerequestedPayloadDict,
    doc="Pydantic model for the GitHub `check_run` webhook with action `rerequested`.",
)
CheckSuiteCompletedPayload = build_model_from_typeddict(
    "CheckSuiteCompletedPayload",
    CheckSuiteCompletedPayloadDict,
    doc="Pydantic model for the GitHub `check_suite` webhook with action `completed`.",
)
CheckSuiteRequestedPayload = build_model_from_typeddict(
    "CheckSuiteRequestedPayload",
    CheckSuiteRequestedPayloadDict,
    doc="Pydantic model for the GitHub `check_suite` webhook with action `requested`.",
)
CheckSuiteRerequestedPayload = build_model_from_typeddict(
    "CheckSuiteRerequestedPayload",
    CheckSuiteRerequestedPayloadDict,
    doc="Pydantic model for the GitHub `check_suite` webhook with action `rerequested`.",
)
CodeScanningAlertAppearedInBranchPayload = build_model_from_typeddict(
    "CodeScanningAlertAppearedInBranchPayload",
    CodeScanningAlertAppearedInBranchPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `appeared_in_branch`.",
)
CodeScanningAlertClosedByUserPayload = build_model_from_typeddict(
    "CodeScanningAlertClosedByUserPayload",
    CodeScanningAlertClosedByUserPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `closed_by_user`.",
)
CodeScanningAlertCreatedPayload = build_model_from_typeddict(
    "CodeScanningAlertCreatedPayload",
    CodeScanningAlertCreatedPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `created`.",
)
CodeScanningAlertFixedPayload = build_model_from_typeddict(
    "CodeScanningAlertFixedPayload",
    CodeScanningAlertFixedPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `fixed`.",
)
CodeScanningAlertReopenedPayload = build_model_from_typeddict(
    "CodeScanningAlertReopenedPayload",
    CodeScanningAlertReopenedPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `reopened`.",
)
CodeScanningAlertReopenedByUserPayload = build_model_from_typeddict(
    "CodeScanningAlertReopenedByUserPayload",
    CodeScanningAlertReopenedByUserPayloadDict,
    doc="Pydantic model for the GitHub `code_scanning_alert` webhook with action `reopened_by_user`.",
)
CommitCommentCreatedPayload = build_model_from_typeddict(
    "CommitCommentCreatedPayload",
    CommitCommentCreatedPayloadDict,
    doc="Pydantic model for the GitHub `commit_comment` webhook with action `created`.",
)
CreatePayload = build_model_from_typeddict(
    "CreatePayload", CreatePayloadDict, doc="Pydantic model for the GitHub `create` webhook."
)
CustomPropertyCreatedPayload = build_model_from_typeddict(
    "CustomPropertyCreatedPayload",
    CustomPropertyCreatedPayloadDict,
    doc="Pydantic model for the GitHub `custom_property` webhook with action `created`.",
)
CustomPropertyDeletedPayload = build_model_from_typeddict(
    "CustomPropertyDeletedPayload",
    CustomPropertyDeletedPayloadDict,
    doc="Pydantic model for the GitHub `custom_property` webhook with action `deleted`.",
)
CustomPropertyValuesUpdatedPayload = build_model_from_typeddict(
    "CustomPropertyValuesUpdatedPayload",
    CustomPropertyValuesUpdatedPayloadDict,
    doc="Pydantic model for the GitHub `custom_property_values` webhook with action `updated`.",
)
DeletePayload = build_model_from_typeddict(
    "DeletePayload", DeletePayloadDict, doc="Pydantic model for the GitHub `delete` webhook."
)
DependabotAlertCreatedPayload = build_model_from_typeddict(
    "DependabotAlertCreatedPayload",
    DependabotAlertCreatedPayloadDict,
    doc="Pydantic model for the GitHub `dependabot_alert` webhook with action `created`.",
)
DependabotAlertDismissedPayload = build_model_from_typeddict(
    "DependabotAlertDismissedPayload",
    DependabotAlertDismissedPayloadDict,
    doc="Pydantic model for the GitHub `dependabot_alert` webhook with action `dismissed`.",
)
DependabotAlertFixedPayload = build_model_from_typeddict(
    "DependabotAlertFixedPayload",
    DependabotAlertFixedPayloadDict,
    doc="Pydantic model for the GitHub `dependabot_alert` webhook with action `fixed`.",
)
DependabotAlertReintroducedPayload = build_model_from_typeddict(
    "DependabotAlertReintroducedPayload",
    DependabotAlertReintroducedPayloadDict,
    doc="Pydantic model for the GitHub `dependabot_alert` webhook with action `reintroduced`.",
)
DependabotAlertReopenedPayload = build_model_from_typeddict(
    "DependabotAlertReopenedPayload",
    DependabotAlertReopenedPayloadDict,
    doc="Pydantic model for the GitHub `dependabot_alert` webhook with action `reopened`.",
)
DeployKeyCreatedPayload = build_model_from_typeddict(
    "DeployKeyCreatedPayload",
    DeployKeyCreatedPayloadDict,
    doc="Pydantic model for the GitHub `deploy_key` webhook with action `created`.",
)
DeployKeyDeletedPayload = build_model_from_typeddict(
    "DeployKeyDeletedPayload",
    DeployKeyDeletedPayloadDict,
    doc="Pydantic model for the GitHub `deploy_key` webhook with action `deleted`.",
)
DeploymentCreatedPayload = build_model_from_typeddict(
    "DeploymentCreatedPayload",
    DeploymentCreatedPayloadDict,
    doc="Pydantic model for the GitHub `deployment` webhook with action `created`.",
)
DeploymentProtectionRuleRequestedPayload = build_model_from_typeddict(
    "DeploymentProtectionRuleRequestedPayload",
    DeploymentProtectionRuleRequestedPayloadDict,
    doc="Pydantic model for the GitHub `deployment_protection_rule` webhook with action `requested`.",
)
DeploymentReviewApprovedPayload = build_model_from_typeddict(
    "DeploymentReviewApprovedPayload",
    DeploymentReviewApprovedPayloadDict,
    doc="Pydantic model for the GitHub `deployment_review` webhook with action `approved`.",
)
DeploymentReviewRejectedPayload = build_model_from_typeddict(
    "DeploymentReviewRejectedPayload",
    DeploymentReviewRejectedPayloadDict,
    doc="Pydantic model for the GitHub `deployment_review` webhook with action `rejected`.",
)
DeploymentReviewRequestedPayload = build_model_from_typeddict(
    "DeploymentReviewRequestedPayload",
    DeploymentReviewRequestedPayloadDict,
    doc="Pydantic model for the GitHub `deployment_review` webhook with action `requested`.",
)
DeploymentStatusCreatedPayload = build_model_from_typeddict(
    "DeploymentStatusCreatedPayload",
    DeploymentStatusCreatedPayloadDict,
    doc="Pydantic model for the GitHub `deployment_status` webhook with action `created`.",
)
DiscussionAnsweredPayload = build_model_from_typeddict(
    "DiscussionAnsweredPayload",
    DiscussionAnsweredPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `answered`.",
)
DiscussionCategoryChangedPayload = build_model_from_typeddict(
    "DiscussionCategoryChangedPayload",
    DiscussionCategoryChangedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `category_changed`.",
)
DiscussionCreatedPayload = build_model_from_typeddict(
    "DiscussionCreatedPayload",
    DiscussionCreatedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `created`.",
)
DiscussionDeletedPayload = build_model_from_typeddict(
    "DiscussionDeletedPayload",
    DiscussionDeletedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `deleted`.",
)
DiscussionEditedPayload = build_model_from_typeddict(
    "DiscussionEditedPayload",
    DiscussionEditedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `edited`.",
)
DiscussionLabeledPayload = build_model_from_typeddict(
    "DiscussionLabeledPayload",
    DiscussionLabeledPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `labeled`.",
)
DiscussionLockedPayload = build_model_from_typeddict(
    "DiscussionLockedPayload",
    DiscussionLockedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `locked`.",
)
DiscussionPinnedPayload = build_model_from_typeddict(
    "DiscussionPinnedPayload",
    DiscussionPinnedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `pinned`.",
)
DiscussionTransferredPayload = build_model_from_typeddict(
    "DiscussionTransferredPayload",
    DiscussionTransferredPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `transferred`.",
)
DiscussionUnansweredPayload = build_model_from_typeddict(
    "DiscussionUnansweredPayload",
    DiscussionUnansweredPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `unanswered`.",
)
DiscussionUnlabeledPayload = build_model_from_typeddict(
    "DiscussionUnlabeledPayload",
    DiscussionUnlabeledPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `unlabeled`.",
)
DiscussionUnlockedPayload = build_model_from_typeddict(
    "DiscussionUnlockedPayload",
    DiscussionUnlockedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `unlocked`.",
)
DiscussionUnpinnedPayload = build_model_from_typeddict(
    "DiscussionUnpinnedPayload",
    DiscussionUnpinnedPayloadDict,
    doc="Pydantic model for the GitHub `discussion` webhook with action `unpinned`.",
)
DiscussionCommentCreatedPayload = build_model_from_typeddict(
    "DiscussionCommentCreatedPayload",
    DiscussionCommentCreatedPayloadDict,
    doc="Pydantic model for the GitHub `discussion_comment` webhook with action `created`.",
)
DiscussionCommentDeletedPayload = build_model_from_typeddict(
    "DiscussionCommentDeletedPayload",
    DiscussionCommentDeletedPayloadDict,
    doc="Pydantic model for the GitHub `discussion_comment` webhook with action `deleted`.",
)
DiscussionCommentEditedPayload = build_model_from_typeddict(
    "DiscussionCommentEditedPayload",
    DiscussionCommentEditedPayloadDict,
    doc="Pydantic model for the GitHub `discussion_comment` webhook with action `edited`.",
)
ForkPayload = build_model_from_typeddict(
    "ForkPayload", ForkPayloadDict, doc="Pydantic model for the GitHub `fork` webhook."
)
GithubAppAuthorizationRevokedPayload = build_model_from_typeddict(
    "GithubAppAuthorizationRevokedPayload",
    GithubAppAuthorizationRevokedPayloadDict,
    doc="Pydantic model for the GitHub `github_app_authorization` webhook with action `revoked`.",
)
GollumPayload = build_model_from_typeddict(
    "GollumPayload", GollumPayloadDict, doc="Pydantic model for the GitHub `gollum` webhook."
)
InstallationCreatedPayload = build_model_from_typeddict(
    "InstallationCreatedPayload",
    InstallationCreatedPayloadDict,
    doc="Pydantic model for the GitHub `installation` webhook with action `created`.",
)
InstallationDeletedPayload = build_model_from_typeddict(
    "InstallationDeletedPayload",
    InstallationDeletedPayloadDict,
    doc="Pydantic model for the GitHub `installation` webhook with action `deleted`.",
)
InstallationNewPermissionsAcceptedPayload = build_model_from_typeddict(
    "InstallationNewPermissionsAcceptedPayload",
    InstallationNewPermissionsAcceptedPayloadDict,
    doc="Pydantic model for the GitHub `installation` webhook with action `new_permissions_accepted`.",
)
InstallationSuspendPayload = build_model_from_typeddict(
    "InstallationSuspendPayload",
    InstallationSuspendPayloadDict,
    doc="Pydantic model for the GitHub `installation` webhook with action `suspend`.",
)
InstallationUnsuspendPayload = build_model_from_typeddict(
    "InstallationUnsuspendPayload",
    InstallationUnsuspendPayloadDict,
    doc="Pydantic model for the GitHub `installation` webhook with action `unsuspend`.",
)
InstallationRepositoriesAddedPayload = build_model_from_typeddict(
    "InstallationRepositoriesAddedPayload",
    InstallationRepositoriesAddedPayloadDict,
    doc="Pydantic model for the GitHub `installation_repositories` webhook with action `added`.",
)
InstallationRepositoriesRemovedPayload = build_model_from_typeddict(
    "InstallationRepositoriesRemovedPayload",
    InstallationRepositoriesRemovedPayloadDict,
    doc="Pydantic model for the GitHub `installation_repositories` webhook with action `removed`.",
)
InstallationTargetRenamedPayload = build_model_from_typeddict(
    "InstallationTargetRenamedPayload",
    InstallationTargetRenamedPayloadDict,
    doc="Pydantic model for the GitHub `installation_target` webhook with action `renamed`.",
)
IssueCommentCreatedPayload = build_model_from_typeddict(
    "IssueCommentCreatedPayload",
    IssueCommentCreatedPayloadDict,
    doc="Pydantic model for the GitHub `issue_comment` webhook with action `created`.",
)
IssueCommentDeletedPayload = build_model_from_typeddict(
    "IssueCommentDeletedPayload",
    IssueCommentDeletedPayloadDict,
    doc="Pydantic model for the GitHub `issue_comment` webhook with action `deleted`.",
)
IssueCommentEditedPayload = build_model_from_typeddict(
    "IssueCommentEditedPayload",
    IssueCommentEditedPayloadDict,
    doc="Pydantic model for the GitHub `issue_comment` webhook with action `edited`.",
)
IssuesAssignedPayload = build_model_from_typeddict(
    "IssuesAssignedPayload",
    IssuesAssignedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `assigned`.",
)
IssuesClosedPayload = build_model_from_typeddict(
    "IssuesClosedPayload",
    IssuesClosedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `closed`.",
)
IssuesDeletedPayload = build_model_from_typeddict(
    "IssuesDeletedPayload",
    IssuesDeletedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `deleted`.",
)
IssuesDemilestonedPayload = build_model_from_typeddict(
    "IssuesDemilestonedPayload",
    IssuesDemilestonedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `demilestoned`.",
)
IssuesEditedPayload = build_model_from_typeddict(
    "IssuesEditedPayload",
    IssuesEditedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `edited`.",
)
IssuesLabeledPayload = build_model_from_typeddict(
    "IssuesLabeledPayload",
    IssuesLabeledPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `labeled`.",
)
IssuesLockedPayload = build_model_from_typeddict(
    "IssuesLockedPayload",
    IssuesLockedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `locked`.",
)
IssuesMilestonedPayload = build_model_from_typeddict(
    "IssuesMilestonedPayload",
    IssuesMilestonedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `milestoned`.",
)
IssuesOpenedPayload = build_model_from_typeddict(
    "IssuesOpenedPayload",
    IssuesOpenedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `opened`.",
)
IssuesPinnedPayload = build_model_from_typeddict(
    "IssuesPinnedPayload",
    IssuesPinnedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `pinned`.",
)
IssuesReopenedPayload = build_model_from_typeddict(
    "IssuesReopenedPayload",
    IssuesReopenedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `reopened`.",
)
IssuesTransferredPayload = build_model_from_typeddict(
    "IssuesTransferredPayload",
    IssuesTransferredPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `transferred`.",
)
IssuesUnassignedPayload = build_model_from_typeddict(
    "IssuesUnassignedPayload",
    IssuesUnassignedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `unassigned`.",
)
IssuesUnlabeledPayload = build_model_from_typeddict(
    "IssuesUnlabeledPayload",
    IssuesUnlabeledPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `unlabeled`.",
)
IssuesUnlockedPayload = build_model_from_typeddict(
    "IssuesUnlockedPayload",
    IssuesUnlockedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `unlocked`.",
)
IssuesUnpinnedPayload = build_model_from_typeddict(
    "IssuesUnpinnedPayload",
    IssuesUnpinnedPayloadDict,
    doc="Pydantic model for the GitHub `issues` webhook with action `unpinned`.",
)
LabelCreatedPayload = build_model_from_typeddict(
    "LabelCreatedPayload",
    LabelCreatedPayloadDict,
    doc="Pydantic model for the GitHub `label` webhook with action `created`.",
)
LabelDeletedPayload = build_model_from_typeddict(
    "LabelDeletedPayload",
    LabelDeletedPayloadDict,
    doc="Pydantic model for the GitHub `label` webhook with action `deleted`.",
)
LabelEditedPayload = build_model_from_typeddict(
    "LabelEditedPayload",
    LabelEditedPayloadDict,
    doc="Pydantic model for the GitHub `label` webhook with action `edited`.",
)
MarketplacePurchaseCancelledPayload = build_model_from_typeddict(
    "MarketplacePurchaseCancelledPayload",
    MarketplacePurchaseCancelledPayloadDict,
    doc="Pydantic model for the GitHub `marketplace_purchase` webhook with action `cancelled`.",
)
MarketplacePurchaseChangedPayload = build_model_from_typeddict(
    "MarketplacePurchaseChangedPayload",
    MarketplacePurchaseChangedPayloadDict,
    doc="Pydantic model for the GitHub `marketplace_purchase` webhook with action `changed`.",
)
MarketplacePurchasePendingChangePayload = build_model_from_typeddict(
    "MarketplacePurchasePendingChangePayload",
    MarketplacePurchasePendingChangePayloadDict,
    doc="Pydantic model for the GitHub `marketplace_purchase` webhook with action `pending_change`.",
)
MarketplacePurchasePendingChangeCancelledPayload = build_model_from_typeddict(
    "MarketplacePurchasePendingChangeCancelledPayload",
    MarketplacePurchasePendingChangeCancelledPayloadDict,
    doc="Pydantic model for the GitHub `marketplace_purchase` webhook with action `pending_change_cancelled`.",
)
MarketplacePurchasePurchasedPayload = build_model_from_typeddict(
    "MarketplacePurchasePurchasedPayload",
    MarketplacePurchasePurchasedPayloadDict,
    doc="Pydantic model for the GitHub `marketplace_purchase` webhook with action `purchased`.",
)
MemberAddedPayload = build_model_from_typeddict(
    "MemberAddedPayload",
    MemberAddedPayloadDict,
    doc="Pydantic model for the GitHub `member` webhook with action `added`.",
)
MemberEditedPayload = build_model_from_typeddict(
    "MemberEditedPayload",
    MemberEditedPayloadDict,
    doc="Pydantic model for the GitHub `member` webhook with action `edited`.",
)
MemberRemovedPayload = build_model_from_typeddict(
    "MemberRemovedPayload",
    MemberRemovedPayloadDict,
    doc="Pydantic model for the GitHub `member` webhook with action `removed`.",
)
MembershipAddedPayload = build_model_from_typeddict(
    "MembershipAddedPayload",
    MembershipAddedPayloadDict,
    doc="Pydantic model for the GitHub `membership` webhook with action `added`.",
)
MembershipRemovedPayload = build_model_from_typeddict(
    "MembershipRemovedPayload",
    MembershipRemovedPayloadDict,
    doc="Pydantic model for the GitHub `membership` webhook with action `removed`.",
)
MergeGroupChecksRequestedPayload = build_model_from_typeddict(
    "MergeGroupChecksRequestedPayload",
    MergeGroupChecksRequestedPayloadDict,
    doc="Pydantic model for the GitHub `merge_group` webhook with action `checks_requested`.",
)
MergeGroupDestroyedPayload = build_model_from_typeddict(
    "MergeGroupDestroyedPayload",
    MergeGroupDestroyedPayloadDict,
    doc="Pydantic model for the GitHub `merge_group` webhook with action `destroyed`.",
)
MetaDeletedPayload = build_model_from_typeddict(
    "MetaDeletedPayload",
    MetaDeletedPayloadDict,
    doc="Pydantic model for the GitHub `meta` webhook with action `deleted`.",
)
MilestoneClosedPayload = build_model_from_typeddict(
    "MilestoneClosedPayload",
    MilestoneClosedPayloadDict,
    doc="Pydantic model for the GitHub `milestone` webhook with action `closed`.",
)
MilestoneCreatedPayload = build_model_from_typeddict(
    "MilestoneCreatedPayload",
    MilestoneCreatedPayloadDict,
    doc="Pydantic model for the GitHub `milestone` webhook with action `created`.",
)
MilestoneDeletedPayload = build_model_from_typeddict(
    "MilestoneDeletedPayload",
    MilestoneDeletedPayloadDict,
    doc="Pydantic model for the GitHub `milestone` webhook with action `deleted`.",
)
MilestoneEditedPayload = build_model_from_typeddict(
    "MilestoneEditedPayload",
    MilestoneEditedPayloadDict,
    doc="Pydantic model for the GitHub `milestone` webhook with action `edited`.",
)
MilestoneOpenedPayload = build_model_from_typeddict(
    "MilestoneOpenedPayload",
    MilestoneOpenedPayloadDict,
    doc="Pydantic model for the GitHub `milestone` webhook with action `opened`.",
)
OrgBlockBlockedPayload = build_model_from_typeddict(
    "OrgBlockBlockedPayload",
    OrgBlockBlockedPayloadDict,
    doc="Pydantic model for the GitHub `org_block` webhook with action `blocked`.",
)
OrgBlockUnblockedPayload = build_model_from_typeddict(
    "OrgBlockUnblockedPayload",
    OrgBlockUnblockedPayloadDict,
    doc="Pydantic model for the GitHub `org_block` webhook with action `unblocked`.",
)
OrganizationDeletedPayload = build_model_from_typeddict(
    "OrganizationDeletedPayload",
    OrganizationDeletedPayloadDict,
    doc="Pydantic model for the GitHub `organization` webhook with action `deleted`.",
)
OrganizationMemberAddedPayload = build_model_from_typeddict(
    "OrganizationMemberAddedPayload",
    OrganizationMemberAddedPayloadDict,
    doc="Pydantic model for the GitHub `organization` webhook with action `member_added`.",
)
OrganizationMemberInvitedPayload = build_model_from_typeddict(
    "OrganizationMemberInvitedPayload",
    OrganizationMemberInvitedPayloadDict,
    doc="Pydantic model for the GitHub `organization` webhook with action `member_invited`.",
)
OrganizationMemberRemovedPayload = build_model_from_typeddict(
    "OrganizationMemberRemovedPayload",
    OrganizationMemberRemovedPayloadDict,
    doc="Pydantic model for the GitHub `organization` webhook with action `member_removed`.",
)
OrganizationRenamedPayload = build_model_from_typeddict(
    "OrganizationRenamedPayload",
    OrganizationRenamedPayloadDict,
    doc="Pydantic model for the GitHub `organization` webhook with action `renamed`.",
)
PackagePublishedPayload = build_model_from_typeddict(
    "PackagePublishedPayload",
    PackagePublishedPayloadDict,
    doc="Pydantic model for the GitHub `package` webhook with action `published`.",
)
PackageUpdatedPayload = build_model_from_typeddict(
    "PackageUpdatedPayload",
    PackageUpdatedPayloadDict,
    doc="Pydantic model for the GitHub `package` webhook with action `updated`.",
)
PageBuildPayload = build_model_from_typeddict(
    "PageBuildPayload", PageBuildPayloadDict, doc="Pydantic model for the GitHub `page_build` webhook."
)
PingPayload = build_model_from_typeddict(
    "PingPayload", PingPayloadDict, doc="Pydantic model for the GitHub `ping` webhook."
)
ProjectClosedPayload = build_model_from_typeddict(
    "ProjectClosedPayload",
    ProjectClosedPayloadDict,
    doc="Pydantic model for the GitHub `project` webhook with action `closed`.",
)
ProjectCreatedPayload = build_model_from_typeddict(
    "ProjectCreatedPayload",
    ProjectCreatedPayloadDict,
    doc="Pydantic model for the GitHub `project` webhook with action `created`.",
)
ProjectDeletedPayload = build_model_from_typeddict(
    "ProjectDeletedPayload",
    ProjectDeletedPayloadDict,
    doc="Pydantic model for the GitHub `project` webhook with action `deleted`.",
)
ProjectEditedPayload = build_model_from_typeddict(
    "ProjectEditedPayload",
    ProjectEditedPayloadDict,
    doc="Pydantic model for the GitHub `project` webhook with action `edited`.",
)
ProjectReopenedPayload = build_model_from_typeddict(
    "ProjectReopenedPayload",
    ProjectReopenedPayloadDict,
    doc="Pydantic model for the GitHub `project` webhook with action `reopened`.",
)
ProjectCardConvertedPayload = build_model_from_typeddict(
    "ProjectCardConvertedPayload",
    ProjectCardConvertedPayloadDict,
    doc="Pydantic model for the GitHub `project_card` webhook with action `converted`.",
)
ProjectCardCreatedPayload = build_model_from_typeddict(
    "ProjectCardCreatedPayload",
    ProjectCardCreatedPayloadDict,
    doc="Pydantic model for the GitHub `project_card` webhook with action `created`.",
)
ProjectCardDeletedPayload = build_model_from_typeddict(
    "ProjectCardDeletedPayload",
    ProjectCardDeletedPayloadDict,
    doc="Pydantic model for the GitHub `project_card` webhook with action `deleted`.",
)
ProjectCardEditedPayload = build_model_from_typeddict(
    "ProjectCardEditedPayload",
    ProjectCardEditedPayloadDict,
    doc="Pydantic model for the GitHub `project_card` webhook with action `edited`.",
)
ProjectCardMovedPayload = build_model_from_typeddict(
    "ProjectCardMovedPayload",
    ProjectCardMovedPayloadDict,
    doc="Pydantic model for the GitHub `project_card` webhook with action `moved`.",
)
ProjectColumnCreatedPayload = build_model_from_typeddict(
    "ProjectColumnCreatedPayload",
    ProjectColumnCreatedPayloadDict,
    doc="Pydantic model for the GitHub `project_column` webhook with action `created`.",
)
ProjectColumnDeletedPayload = build_model_from_typeddict(
    "ProjectColumnDeletedPayload",
    ProjectColumnDeletedPayloadDict,
    doc="Pydantic model for the GitHub `project_column` webhook with action `deleted`.",
)
ProjectColumnEditedPayload = build_model_from_typeddict(
    "ProjectColumnEditedPayload",
    ProjectColumnEditedPayloadDict,
    doc="Pydantic model for the GitHub `project_column` webhook with action `edited`.",
)
ProjectColumnMovedPayload = build_model_from_typeddict(
    "ProjectColumnMovedPayload",
    ProjectColumnMovedPayloadDict,
    doc="Pydantic model for the GitHub `project_column` webhook with action `moved`.",
)
ProjectsV2ItemArchivedPayload = build_model_from_typeddict(
    "ProjectsV2ItemArchivedPayload",
    ProjectsV2ItemArchivedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `archived`.",
)
ProjectsV2ItemConvertedPayload = build_model_from_typeddict(
    "ProjectsV2ItemConvertedPayload",
    ProjectsV2ItemConvertedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `converted`.",
)
ProjectsV2ItemCreatedPayload = build_model_from_typeddict(
    "ProjectsV2ItemCreatedPayload",
    ProjectsV2ItemCreatedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `created`.",
)
ProjectsV2ItemDeletedPayload = build_model_from_typeddict(
    "ProjectsV2ItemDeletedPayload",
    ProjectsV2ItemDeletedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `deleted`.",
)
ProjectsV2ItemEditedPayload = build_model_from_typeddict(
    "ProjectsV2ItemEditedPayload",
    ProjectsV2ItemEditedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `edited`.",
)
ProjectsV2ItemReorderedPayload = build_model_from_typeddict(
    "ProjectsV2ItemReorderedPayload",
    ProjectsV2ItemReorderedPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `reordered`.",
)
ProjectsV2ItemRestoredPayload = build_model_from_typeddict(
    "ProjectsV2ItemRestoredPayload",
    ProjectsV2ItemRestoredPayloadDict,
    doc="Pydantic model for the GitHub `projects_v2_item` webhook with action `restored`.",
)
PublicPayload = build_model_from_typeddict(
    "PublicPayload", PublicPayloadDict, doc="Pydantic model for the GitHub `public` webhook."
)
PullRequestPayload = build_model_from_typeddict(
    "PullRequestPayload", PullRequestPayloadDict, doc="Pydantic model for the GitHub `pull_request` webhook."
)
PullRequestAssignedPayload = build_model_from_typeddict(
    "PullRequestAssignedPayload",
    PullRequestAssignedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `assigned`.",
)
PullRequestAutoMergeDisabledPayload = build_model_from_typeddict(
    "PullRequestAutoMergeDisabledPayload",
    PullRequestAutoMergeDisabledPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `auto_merge_disabled`.",
)
PullRequestAutoMergeEnabledPayload = build_model_from_typeddict(
    "PullRequestAutoMergeEnabledPayload",
    PullRequestAutoMergeEnabledPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `auto_merge_enabled`.",
)
PullRequestClosedPayload = build_model_from_typeddict(
    "PullRequestClosedPayload",
    PullRequestClosedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `closed`.",
)
PullRequestConvertedToDraftPayload = build_model_from_typeddict(
    "PullRequestConvertedToDraftPayload",
    PullRequestConvertedToDraftPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `converted_to_draft`.",
)
PullRequestDemilestonedPayload = build_model_from_typeddict(
    "PullRequestDemilestonedPayload",
    PullRequestDemilestonedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `demilestoned`.",
)
PullRequestDequeuedPayload = build_model_from_typeddict(
    "PullRequestDequeuedPayload",
    PullRequestDequeuedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `dequeued`.",
)
PullRequestEditedPayload = build_model_from_typeddict(
    "PullRequestEditedPayload",
    PullRequestEditedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `edited`.",
)
PullRequestEnqueuedPayload = build_model_from_typeddict(
    "PullRequestEnqueuedPayload",
    PullRequestEnqueuedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `enqueued`.",
)
PullRequestLabeledPayload = build_model_from_typeddict(
    "PullRequestLabeledPayload",
    PullRequestLabeledPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `labeled`.",
)
PullRequestLockedPayload = build_model_from_typeddict(
    "PullRequestLockedPayload",
    PullRequestLockedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `locked`.",
)
PullRequestMilestonedPayload = build_model_from_typeddict(
    "PullRequestMilestonedPayload",
    PullRequestMilestonedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `milestoned`.",
)
PullRequestOpenedPayload = build_model_from_typeddict(
    "PullRequestOpenedPayload",
    PullRequestOpenedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `opened`.",
)
PullRequestReadyForReviewPayload = build_model_from_typeddict(
    "PullRequestReadyForReviewPayload",
    PullRequestReadyForReviewPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `ready_for_review`.",
)
PullRequestReopenedPayload = build_model_from_typeddict(
    "PullRequestReopenedPayload",
    PullRequestReopenedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `reopened`.",
)
PullRequestSynchronizePayload = build_model_from_typeddict(
    "PullRequestSynchronizePayload",
    PullRequestSynchronizePayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `synchronize`.",
)
PullRequestUnassignedPayload = build_model_from_typeddict(
    "PullRequestUnassignedPayload",
    PullRequestUnassignedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `unassigned`.",
)
PullRequestUnlabeledPayload = build_model_from_typeddict(
    "PullRequestUnlabeledPayload",
    PullRequestUnlabeledPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `unlabeled`.",
)
PullRequestUnlockedPayload = build_model_from_typeddict(
    "PullRequestUnlockedPayload",
    PullRequestUnlockedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request` webhook with action `unlocked`.",
)
PullRequestReviewDismissedPayload = build_model_from_typeddict(
    "PullRequestReviewDismissedPayload",
    PullRequestReviewDismissedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review` webhook with action `dismissed`.",
)
PullRequestReviewEditedPayload = build_model_from_typeddict(
    "PullRequestReviewEditedPayload",
    PullRequestReviewEditedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review` webhook with action `edited`.",
)
PullRequestReviewSubmittedPayload = build_model_from_typeddict(
    "PullRequestReviewSubmittedPayload",
    PullRequestReviewSubmittedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review` webhook with action `submitted`.",
)
PullRequestReviewCommentCreatedPayload = build_model_from_typeddict(
    "PullRequestReviewCommentCreatedPayload",
    PullRequestReviewCommentCreatedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review_comment` webhook with action `created`.",
)
PullRequestReviewCommentDeletedPayload = build_model_from_typeddict(
    "PullRequestReviewCommentDeletedPayload",
    PullRequestReviewCommentDeletedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review_comment` webhook with action `deleted`.",
)
PullRequestReviewCommentEditedPayload = build_model_from_typeddict(
    "PullRequestReviewCommentEditedPayload",
    PullRequestReviewCommentEditedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review_comment` webhook with action `edited`.",
)
PullRequestReviewThreadResolvedPayload = build_model_from_typeddict(
    "PullRequestReviewThreadResolvedPayload",
    PullRequestReviewThreadResolvedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review_thread` webhook with action `resolved`.",
)
PullRequestReviewThreadUnresolvedPayload = build_model_from_typeddict(
    "PullRequestReviewThreadUnresolvedPayload",
    PullRequestReviewThreadUnresolvedPayloadDict,
    doc="Pydantic model for the GitHub `pull_request_review_thread` webhook with action `unresolved`.",
)
PushPayload = build_model_from_typeddict(
    "PushPayload", PushPayloadDict, doc="Pydantic model for the GitHub `push` webhook."
)
RegistryPackagePublishedPayload = build_model_from_typeddict(
    "RegistryPackagePublishedPayload",
    RegistryPackagePublishedPayloadDict,
    doc="Pydantic model for the GitHub `registry_package` webhook with action `published`.",
)
RegistryPackageUpdatedPayload = build_model_from_typeddict(
    "RegistryPackageUpdatedPayload",
    RegistryPackageUpdatedPayloadDict,
    doc="Pydantic model for the GitHub `registry_package` webhook with action `updated`.",
)
ReleaseCreatedPayload = build_model_from_typeddict(
    "ReleaseCreatedPayload",
    ReleaseCreatedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `created`.",
)
ReleaseDeletedPayload = build_model_from_typeddict(
    "ReleaseDeletedPayload",
    ReleaseDeletedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `deleted`.",
)
ReleaseEditedPayload = build_model_from_typeddict(
    "ReleaseEditedPayload",
    ReleaseEditedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `edited`.",
)
ReleasePrereleasedPayload = build_model_from_typeddict(
    "ReleasePrereleasedPayload",
    ReleasePrereleasedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `prereleased`.",
)
ReleasePublishedPayload = build_model_from_typeddict(
    "ReleasePublishedPayload",
    ReleasePublishedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `published`.",
)
ReleaseReleasedPayload = build_model_from_typeddict(
    "ReleaseReleasedPayload",
    ReleaseReleasedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `released`.",
)
ReleaseUnpublishedPayload = build_model_from_typeddict(
    "ReleaseUnpublishedPayload",
    ReleaseUnpublishedPayloadDict,
    doc="Pydantic model for the GitHub `release` webhook with action `unpublished`.",
)
RepositoryArchivedPayload = build_model_from_typeddict(
    "RepositoryArchivedPayload",
    RepositoryArchivedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `archived`.",
)
RepositoryCreatedPayload = build_model_from_typeddict(
    "RepositoryCreatedPayload",
    RepositoryCreatedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `created`.",
)
RepositoryDeletedPayload = build_model_from_typeddict(
    "RepositoryDeletedPayload",
    RepositoryDeletedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `deleted`.",
)
RepositoryEditedPayload = build_model_from_typeddict(
    "RepositoryEditedPayload",
    RepositoryEditedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `edited`.",
)
RepositoryPrivatizedPayload = build_model_from_typeddict(
    "RepositoryPrivatizedPayload",
    RepositoryPrivatizedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `privatized`.",
)
RepositoryPublicizedPayload = build_model_from_typeddict(
    "RepositoryPublicizedPayload",
    RepositoryPublicizedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `publicized`.",
)
RepositoryRenamedPayload = build_model_from_typeddict(
    "RepositoryRenamedPayload",
    RepositoryRenamedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `renamed`.",
)
RepositoryTransferredPayload = build_model_from_typeddict(
    "RepositoryTransferredPayload",
    RepositoryTransferredPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `transferred`.",
)
RepositoryUnarchivedPayload = build_model_from_typeddict(
    "RepositoryUnarchivedPayload",
    RepositoryUnarchivedPayloadDict,
    doc="Pydantic model for the GitHub `repository` webhook with action `unarchived`.",
)
RepositoryDispatchPayload = build_model_from_typeddict(
    "RepositoryDispatchPayload",
    RepositoryDispatchPayloadDict,
    doc="Pydantic model for the GitHub `repository_dispatch` webhook.",
)
RepositoryImportPayload = build_model_from_typeddict(
    "RepositoryImportPayload",
    RepositoryImportPayloadDict,
    doc="Pydantic model for the GitHub `repository_import` webhook.",
)
RepositoryVulnerabilityAlertCreatePayload = build_model_from_typeddict(
    "RepositoryVulnerabilityAlertCreatePayload",
    RepositoryVulnerabilityAlertCreatePayloadDict,
    doc="Pydantic model for the GitHub `repository_vulnerability_alert` webhook with action `create`.",
)
RepositoryVulnerabilityAlertDismissPayload = build_model_from_typeddict(
    "RepositoryVulnerabilityAlertDismissPayload",
    RepositoryVulnerabilityAlertDismissPayloadDict,
    doc="Pydantic model for the GitHub `repository_vulnerability_alert` webhook with action `dismiss`.",
)
RepositoryVulnerabilityAlertReopenPayload = build_model_from_typeddict(
    "RepositoryVulnerabilityAlertReopenPayload",
    RepositoryVulnerabilityAlertReopenPayloadDict,
    doc="Pydantic model for the GitHub `repository_vulnerability_alert` webhook with action `reopen`.",
)
RepositoryVulnerabilityAlertResolvePayload = build_model_from_typeddict(
    "RepositoryVulnerabilityAlertResolvePayload",
    RepositoryVulnerabilityAlertResolvePayloadDict,
    doc="Pydantic model for the GitHub `repository_vulnerability_alert` webhook with action `resolve`.",
)
SecretScanningAlertCreatedPayload = build_model_from_typeddict(
    "SecretScanningAlertCreatedPayload",
    SecretScanningAlertCreatedPayloadDict,
    doc="Pydantic model for the GitHub `secret_scanning_alert` webhook with action `created`.",
)
SecretScanningAlertReopenedPayload = build_model_from_typeddict(
    "SecretScanningAlertReopenedPayload",
    SecretScanningAlertReopenedPayloadDict,
    doc="Pydantic model for the GitHub `secret_scanning_alert` webhook with action `reopened`.",
)
SecretScanningAlertResolvedPayload = build_model_from_typeddict(
    "SecretScanningAlertResolvedPayload",
    SecretScanningAlertResolvedPayloadDict,
    doc="Pydantic model for the GitHub `secret_scanning_alert` webhook with action `resolved`.",
)
SecretScanningAlertRevokedPayload = build_model_from_typeddict(
    "SecretScanningAlertRevokedPayload",
    SecretScanningAlertRevokedPayloadDict,
    doc="Pydantic model for the GitHub `secret_scanning_alert` webhook with action `revoked`.",
)
SecretScanningAlertLocationCreatedPayload = build_model_from_typeddict(
    "SecretScanningAlertLocationCreatedPayload",
    SecretScanningAlertLocationCreatedPayloadDict,
    doc="Pydantic model for the GitHub `secret_scanning_alert_location` webhook with action `created`.",
)
SecurityAdvisoryPerformedPayload = build_model_from_typeddict(
    "SecurityAdvisoryPerformedPayload",
    SecurityAdvisoryPerformedPayloadDict,
    doc="Pydantic model for the GitHub `security_advisory` webhook with action `performed`.",
)
SecurityAdvisoryPublishedPayload = build_model_from_typeddict(
    "SecurityAdvisoryPublishedPayload",
    SecurityAdvisoryPublishedPayloadDict,
    doc="Pydantic model for the GitHub `security_advisory` webhook with action `published`.",
)
SecurityAdvisoryUpdatedPayload = build_model_from_typeddict(
    "SecurityAdvisoryUpdatedPayload",
    SecurityAdvisoryUpdatedPayloadDict,
    doc="Pydantic model for the GitHub `security_advisory` webhook with action `updated`.",
)
SecurityAdvisoryWithdrawnPayload = build_model_from_typeddict(
    "SecurityAdvisoryWithdrawnPayload",
    SecurityAdvisoryWithdrawnPayloadDict,
    doc="Pydantic model for the GitHub `security_advisory` webhook with action `withdrawn`.",
)
SponsorshipCancelledPayload = build_model_from_typeddict(
    "SponsorshipCancelledPayload",
    SponsorshipCancelledPayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `cancelled`.",
)
SponsorshipCreatedPayload = build_model_from_typeddict(
    "SponsorshipCreatedPayload",
    SponsorshipCreatedPayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `created`.",
)
SponsorshipEditedPayload = build_model_from_typeddict(
    "SponsorshipEditedPayload",
    SponsorshipEditedPayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `edited`.",
)
SponsorshipPendingCancellationPayload = build_model_from_typeddict(
    "SponsorshipPendingCancellationPayload",
    SponsorshipPendingCancellationPayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `pending_cancellation`.",
)
SponsorshipPendingTierChangePayload = build_model_from_typeddict(
    "SponsorshipPendingTierChangePayload",
    SponsorshipPendingTierChangePayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `pending_tier_change`.",
)
SponsorshipTierChangedPayload = build_model_from_typeddict(
    "SponsorshipTierChangedPayload",
    SponsorshipTierChangedPayloadDict,
    doc="Pydantic model for the GitHub `sponsorship` webhook with action `tier_changed`.",
)
StarCreatedPayload = build_model_from_typeddict(
    "StarCreatedPayload",
    StarCreatedPayloadDict,
    doc="Pydantic model for the GitHub `star` webhook with action `created`.",
)
StarDeletedPayload = build_model_from_typeddict(
    "StarDeletedPayload",
    StarDeletedPayloadDict,
    doc="Pydantic model for the GitHub `star` webhook with action `deleted`.",
)
StatusPayload = build_model_from_typeddict(
    "StatusPayload", StatusPayloadDict, doc="Pydantic model for the GitHub `status` webhook."
)
TeamAddedToRepositoryPayload = build_model_from_typeddict(
    "TeamAddedToRepositoryPayload",
    TeamAddedToRepositoryPayloadDict,
    doc="Pydantic model for the GitHub `team` webhook with action `added_to_repository`.",
)
TeamCreatedPayload = build_model_from_typeddict(
    "TeamCreatedPayload",
    TeamCreatedPayloadDict,
    doc="Pydantic model for the GitHub `team` webhook with action `created`.",
)
TeamDeletedPayload = build_model_from_typeddict(
    "TeamDeletedPayload",
    TeamDeletedPayloadDict,
    doc="Pydantic model for the GitHub `team` webhook with action `deleted`.",
)
TeamEditedPayload = build_model_from_typeddict(
    "TeamEditedPayload", TeamEditedPayloadDict, doc="Pydantic model for the GitHub `team` webhook with action `edited`."
)
TeamRemovedFromRepositoryPayload = build_model_from_typeddict(
    "TeamRemovedFromRepositoryPayload",
    TeamRemovedFromRepositoryPayloadDict,
    doc="Pydantic model for the GitHub `team` webhook with action `removed_from_repository`.",
)
TeamAddPayload = build_model_from_typeddict(
    "TeamAddPayload", TeamAddPayloadDict, doc="Pydantic model for the GitHub `team_add` webhook."
)
WatchStartedPayload = build_model_from_typeddict(
    "WatchStartedPayload",
    WatchStartedPayloadDict,
    doc="Pydantic model for the GitHub `watch` webhook with action `started`.",
)
WorkflowDispatchPayload = build_model_from_typeddict(
    "WorkflowDispatchPayload",
    WorkflowDispatchPayloadDict,
    doc="Pydantic model for the GitHub `workflow_dispatch` webhook.",
)
WorkflowJobCompletedPayload = build_model_from_typeddict(
    "WorkflowJobCompletedPayload",
    WorkflowJobCompletedPayloadDict,
    doc="Pydantic model for the GitHub `workflow_job` webhook with action `completed`.",
)
WorkflowJobInProgressPayload = build_model_from_typeddict(
    "WorkflowJobInProgressPayload",
    WorkflowJobInProgressPayloadDict,
    doc="Pydantic model for the GitHub `workflow_job` webhook with action `in_progress`.",
)
WorkflowJobQueuedPayload = build_model_from_typeddict(
    "WorkflowJobQueuedPayload",
    WorkflowJobQueuedPayloadDict,
    doc="Pydantic model for the GitHub `workflow_job` webhook with action `queued`.",
)
WorkflowJobWaitingPayload = build_model_from_typeddict(
    "WorkflowJobWaitingPayload",
    WorkflowJobWaitingPayloadDict,
    doc="Pydantic model for the GitHub `workflow_job` webhook with action `waiting`.",
)
WorkflowRunCompletedPayload = build_model_from_typeddict(
    "WorkflowRunCompletedPayload",
    WorkflowRunCompletedPayloadDict,
    doc="Pydantic model for the GitHub `workflow_run` webhook with action `completed`.",
)
WorkflowRunInProgressPayload = build_model_from_typeddict(
    "WorkflowRunInProgressPayload",
    WorkflowRunInProgressPayloadDict,
    doc="Pydantic model for the GitHub `workflow_run` webhook with action `in_progress`.",
)
WorkflowRunRequestedPayload = build_model_from_typeddict(
    "WorkflowRunRequestedPayload",
    WorkflowRunRequestedPayloadDict,
    doc="Pydantic model for the GitHub `workflow_run` webhook with action `requested`.",
)
type WebhookPayloadModel = BaseModel
