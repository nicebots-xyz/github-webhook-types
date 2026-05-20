# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Pydantic models generated from Octokit's GitHub webhook schema.

Do not edit this module by hand. Run `pdm run generate` instead.
"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

__all__ = [
    "AppPermissions",
    "BranchProtectionConfigurationDisabledPayload",
    "BranchProtectionConfigurationEnabledPayload",
    "BranchProtectionRuleCreatedPayload",
    "BranchProtectionRuleDeletedPayload",
    "BranchProtectionRuleEditedPayload",
    "BranchProtectionRuleEditedPayloadChanges",
    "BranchProtectionRuleEditedPayloadChangesAdminEnforced",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorNames",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnly",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnly",
    "BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevel",
    "BranchProtectionRuleEditedPayloadChangesLockAllowsForkSync",
    "BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevel",
    "BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevel",
    "BranchProtectionRuleEditedPayloadChangesRequireLastPushApproval",
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecks",
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevel",
    "CheckRunCompletedPayload",
    "CheckRunCreatedPayload",
    "CheckRunRequestedActionPayload",
    "CheckRunRequestedActionPayloadRequestedAction",
    "CheckRunRerequestedPayload",
    "CheckRunWithSimpleCheckSuite",
    "CheckRunWithSimpleCheckSuiteOutput",
    "CheckSuiteCompletedPayload",
    "CheckSuiteCompletedPayloadCheckSuite",
    "CheckSuiteCompletedPayloadCheckSuiteApp",
    "CheckSuiteCompletedPayloadCheckSuiteAppPermissions",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommit",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthor",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitter",
    "CheckSuiteCompletedPayloadCheckSuitePullRequest",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestBase",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepo",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestHead",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepo",
    "CheckSuiteRequestedPayload",
    "CheckSuiteRequestedPayloadCheckSuite",
    "CheckSuiteRequestedPayloadCheckSuiteApp",
    "CheckSuiteRequestedPayloadCheckSuiteAppPermissions",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommit",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthor",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitter",
    "CheckSuiteRequestedPayloadCheckSuitePullRequest",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestBase",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepo",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestHead",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepo",
    "CheckSuiteRerequestedPayload",
    "CheckSuiteRerequestedPayloadCheckSuite",
    "CheckSuiteRerequestedPayloadCheckSuiteApp",
    "CheckSuiteRerequestedPayloadCheckSuiteAppPermissions",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommit",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthor",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitter",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequest",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestBase",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepo",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestHead",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepo",
    "CodeOfConduct",
    "CodeOfConductSimple",
    "CodeScanningAlertAppearedInBranchPayload",
    "CodeScanningAlertAppearedInBranchPayloadAlert",
    "CodeScanningAlertAppearedInBranchPayloadAlertRule",
    "CodeScanningAlertAppearedInBranchPayloadAlertTool",
    "CodeScanningAlertClosedByUserPayload",
    "CodeScanningAlertClosedByUserPayloadAlert",
    "CodeScanningAlertClosedByUserPayloadAlertRule",
    "CodeScanningAlertClosedByUserPayloadAlertTool",
    "CodeScanningAlertCreatedPayload",
    "CodeScanningAlertCreatedPayloadAlert",
    "CodeScanningAlertCreatedPayloadAlertRule",
    "CodeScanningAlertFixedPayload",
    "CodeScanningAlertFixedPayloadAlert",
    "CodeScanningAlertFixedPayloadAlertRule",
    "CodeScanningAlertFixedPayloadAlertTool",
    "CodeScanningAlertReopenedByUserPayload",
    "CodeScanningAlertReopenedByUserPayloadAlert",
    "CodeScanningAlertReopenedByUserPayloadAlertRule",
    "CodeScanningAlertReopenedByUserPayloadAlertTool",
    "CodeScanningAlertReopenedPayload",
    "CodeScanningAlertReopenedPayloadAlert",
    "CodeScanningAlertReopenedPayloadAlertRule",
    "CodeScanningAlertReopenedPayloadAlertTool",
    "CommitCommentCreatedPayload",
    "CommitCommentCreatedPayloadComment",
    "CommitCommentCreatedPayloadCommentReactions",
    "CreatePayload",
    "CustomProperty",
    "CustomPropertyCreatedPayload",
    "CustomPropertyDeletedPayload",
    "CustomPropertyDeletedPayloadDefinition",
    "CustomPropertyPromoteToEnterprisePayload",
    "CustomPropertyUpdatedPayload",
    "CustomPropertyValue",
    "CustomPropertyValuesUpdatedPayload",
    "DeletePayload",
    "DependabotAlert",
    "DependabotAlertAutoDismissedPayload",
    "DependabotAlertAutoReopenedPayload",
    "DependabotAlertCreatedPayload",
    "DependabotAlertDependency",
    "DependabotAlertDismissedPayload",
    "DependabotAlertFixedPayload",
    "DependabotAlertPackage",
    "DependabotAlertReintroducedPayload",
    "DependabotAlertReopenedPayload",
    "DependabotAlertSecurityAdvisory",
    "DependabotAlertSecurityAdvisoryCvss",
    "DependabotAlertSecurityAdvisoryCwe",
    "DependabotAlertSecurityAdvisoryIdentifier",
    "DependabotAlertSecurityAdvisoryReference",
    "DependabotAlertSecurityVulnerability",
    "DeployKeyCreatedPayload",
    "DeployKeyDeletedPayload",
    "Deployment",
    "DeploymentCreatedPayload",
    "DeploymentCreatedPayloadDeployment",
    "DeploymentProtectionRuleRequestedPayload",
    "DeploymentReviewApprovedPayload",
    "DeploymentReviewApprovedPayloadReviewer",
    "DeploymentReviewApprovedPayloadWorkflowJobRun",
    "DeploymentReviewRejectedPayload",
    "DeploymentReviewRejectedPayloadReviewer",
    "DeploymentReviewRejectedPayloadWorkflowJobRun",
    "DeploymentReviewRequestedPayload",
    "DeploymentReviewRequestedPayloadReviewer",
    "DeploymentReviewRequestedPayloadWorkflowJobRun",
    "DeploymentSimple",
    "DeploymentStatusCreatedPayload",
    "DeploymentStatusCreatedPayloadDeployment",
    "DeploymentStatusCreatedPayloadDeploymentStatus",
    "Discussion",
    "DiscussionAnsweredPayload",
    "DiscussionCategory",
    "DiscussionCategoryChangedPayload",
    "DiscussionCategoryChangedPayloadChanges",
    "DiscussionCategoryChangedPayloadChangesCategory",
    "DiscussionCategoryChangedPayloadChangesCategoryFrom",
    "DiscussionClosedPayload",
    "DiscussionCommentCreatedPayload",
    "DiscussionCommentDeletedPayload",
    "DiscussionCommentEditedPayload",
    "DiscussionCommentEditedPayloadChanges",
    "DiscussionCommentEditedPayloadChangesBody",
    "DiscussionCreatedPayload",
    "DiscussionDeletedPayload",
    "DiscussionEditedPayload",
    "DiscussionEditedPayloadChanges",
    "DiscussionEditedPayloadChangesBody",
    "DiscussionEditedPayloadChangesTitle",
    "DiscussionLabeledPayload",
    "DiscussionLockedPayload",
    "DiscussionPinnedPayload",
    "DiscussionReactions",
    "DiscussionReopenedPayload",
    "DiscussionTransferredPayload",
    "DiscussionTransferredPayloadChanges",
    "DiscussionUnansweredPayload",
    "DiscussionUnlabeledPayload",
    "DiscussionUnlockedPayload",
    "DiscussionUnpinnedPayload",
    "Enterprise",
    "Enterprise2",
    "ForkPayload",
    "FullRepository",
    "FullRepositoryPermissions",
    "GithubAppAuthorizationRevokedPayload",
    "GollumPayload",
    "GollumPayloadPage",
    "HookResponse",
    "Installation",
    "Installation2",
    "InstallationCreatedPayload",
    "InstallationCreatedPayloadRepository",
    "InstallationDeletedPayload",
    "InstallationDeletedPayloadRepository",
    "InstallationNewPermissionsAcceptedPayload",
    "InstallationNewPermissionsAcceptedPayloadRepository",
    "InstallationRepositoriesAddedPayload",
    "InstallationRepositoriesAddedPayloadRepositoriesAdded",
    "InstallationRepositoriesAddedPayloadRepositoriesRemoved",
    "InstallationRepositoriesRemovedPayload",
    "InstallationRepositoriesRemovedPayloadRepositoriesAdded",
    "InstallationRepositoriesRemovedPayloadRepositoriesRemoved",
    "InstallationSuspendPayload",
    "InstallationSuspendPayloadRepository",
    "InstallationTargetRenamedPayload",
    "InstallationTargetRenamedPayloadAccount",
    "InstallationTargetRenamedPayloadChanges",
    "InstallationTargetRenamedPayloadChangesLogin",
    "InstallationTargetRenamedPayloadChangesSlug",
    "InstallationUnsuspendPayload",
    "InstallationUnsuspendPayloadRepository",
    "Issue",
    "IssueCommentCreatedPayload",
    "IssueCommentCreatedPayloadComment",
    "IssueCommentCreatedPayloadCommentReactions",
    "IssueCommentDeletedPayload",
    "IssueCommentEditedPayload",
    "IssueDependenciesBlockedByAddedPayload",
    "IssueDependenciesBlockedByRemovedPayload",
    "IssueDependenciesBlockingAddedPayload",
    "IssueDependenciesBlockingRemovedPayload",
    "IssueDependenciesSummary",
    "IssueFieldValue",
    "IssueLabelOption2",
    "IssuePullRequest",
    "IssuesAssignedPayload",
    "IssuesClosedPayload",
    "IssuesDeletedPayload",
    "IssuesDeletedPayloadIssue",
    "IssuesDeletedPayloadIssueLabel",
    "IssuesDeletedPayloadIssuePullRequest",
    "IssuesDeletedPayloadIssueReactions",
    "IssuesDemilestonedPayload",
    "IssuesDemilestonedPayloadIssue",
    "IssuesDemilestonedPayloadIssuePullRequest",
    "IssuesDemilestonedPayloadIssueReactions",
    "IssuesEditedPayload",
    "IssuesEditedPayloadChanges",
    "IssuesEditedPayloadChangesBody",
    "IssuesEditedPayloadChangesTitle",
    "IssuesEditedPayloadIssue",
    "IssuesEditedPayloadIssueLabel",
    "IssuesEditedPayloadIssuePullRequest",
    "IssuesEditedPayloadIssueReactions",
    "IssuesLabeledPayload",
    "IssuesLabeledPayloadIssue",
    "IssuesLabeledPayloadIssueLabel",
    "IssuesLabeledPayloadIssuePullRequest",
    "IssuesLabeledPayloadIssueReactions",
    "IssuesLockedPayload",
    "IssuesLockedPayloadIssue",
    "IssuesLockedPayloadIssuePullRequest",
    "IssuesLockedPayloadIssueReactions",
    "IssuesMilestonedPayload",
    "IssuesMilestonedPayloadIssue",
    "IssuesMilestonedPayloadIssuePullRequest",
    "IssuesMilestonedPayloadIssueReactions",
    "IssuesOpenedPayload",
    "IssuesOpenedPayloadChanges",
    "IssuesOpenedPayloadChangesOldRepository",
    "IssuesOpenedPayloadChangesOldRepositoryPermissions",
    "IssuesOpenedPayloadIssue",
    "IssuesOpenedPayloadIssueLabel",
    "IssuesOpenedPayloadIssuePullRequest",
    "IssuesOpenedPayloadIssueReactions",
    "IssuesPinnedPayload",
    "IssuesReopenedPayload",
    "IssuesReopenedPayloadIssue",
    "IssuesReopenedPayloadIssuePullRequest",
    "IssuesReopenedPayloadIssueReactions",
    "IssuesTransferredPayload",
    "IssuesTransferredPayloadChanges",
    "IssuesTransferredPayloadChangesNewIssue",
    "IssuesTransferredPayloadChangesNewIssueLabel",
    "IssuesTransferredPayloadChangesNewIssuePullRequest",
    "IssuesTransferredPayloadChangesNewIssueReactions",
    "IssuesTransferredPayloadChangesNewRepository",
    "IssuesTransferredPayloadChangesNewRepositoryPermissions",
    "IssuesTypedPayload",
    "IssuesUnassignedPayload",
    "IssuesUnlabeledPayload",
    "IssuesUnlockedPayload",
    "IssuesUnlockedPayloadIssue",
    "IssuesUnlockedPayloadIssuePullRequest",
    "IssuesUnlockedPayloadIssueReactions",
    "IssuesUnpinnedPayload",
    "IssuesUntypedPayload",
    "Label",
    "LabelCreatedPayload",
    "LabelDeletedPayload",
    "LabelEditedPayload",
    "LabelEditedPayloadChanges",
    "LabelEditedPayloadChangesColor",
    "LabelEditedPayloadChangesDescription",
    "LabelEditedPayloadChangesName",
    "LicenseSimple",
    "Link",
    "MarketplacePurchaseCancelledPayload",
    "MarketplacePurchaseChangedPayload",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchase",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccount",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlan",
    "MarketplacePurchasePendingChangeCancelledPayload",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchase",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccount",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlan",
    "MarketplacePurchasePendingChangePayload",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchase",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccount",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlan",
    "MarketplacePurchasePurchasedPayload",
    "MemberAddedPayload",
    "MemberAddedPayloadChanges",
    "MemberAddedPayloadChangesPermission",
    "MemberAddedPayloadChangesRoleName",
    "MemberEditedPayload",
    "MemberEditedPayloadChanges",
    "MemberEditedPayloadChangesOldPermission",
    "MemberEditedPayloadChangesPermission",
    "MemberRemovedPayload",
    "MembershipAddedPayload",
    "MembershipRemovedPayload",
    "MergeGroup",
    "MergeGroupChecksRequestedPayload",
    "MergeGroupDestroyedPayload",
    "MetaDeletedPayload",
    "MetaDeletedPayloadHook",
    "MetaDeletedPayloadHookConfig",
    "Milestone",
    "MilestoneClosedPayload",
    "MilestoneClosedPayloadMilestone",
    "MilestoneCreatedPayload",
    "MilestoneCreatedPayloadMilestone",
    "MilestoneDeletedPayload",
    "MilestoneEditedPayload",
    "MilestoneEditedPayloadChanges",
    "MilestoneEditedPayloadChangesDescription",
    "MilestoneEditedPayloadChangesDueOn",
    "MilestoneEditedPayloadChangesTitle",
    "MilestoneOpenedPayload",
    "MilestoneOpenedPayloadMilestone",
    "MinimalRepository",
    "MinimalRepositoryPermissions",
    "OrgBlockBlockedPayload",
    "OrgBlockUnblockedPayload",
    "Organization",
    "OrganizationDeletedPayload",
    "OrganizationMemberAddedPayload",
    "OrganizationMemberInvitedPayload",
    "OrganizationMemberInvitedPayloadInvitation",
    "OrganizationMemberRemovedPayload",
    "OrganizationRenamedPayload",
    "OrganizationRenamedPayloadChanges",
    "OrganizationRenamedPayloadChangesLogin",
    "PackagePublishedPayload",
    "PackagePublishedPayloadPackage",
    "PackageUpdatedPayload",
    "PackageUpdatedPayloadPackage",
    "PackageUpdatedPayloadPackagePackageVersion",
    "PackageUpdatedPayloadPackagePackageVersionDockerMetadata",
    "PackageUpdatedPayloadPackagePackageVersionPackageFile",
    "PackageUpdatedPayloadPackagePackageVersionRelease",
    "PageBuildPayload",
    "PageBuildPayloadBuild",
    "PageBuildPayloadBuildError",
    "PersonalAccessTokenRequest",
    "PersonalAccessTokenRequestApprovedPayload",
    "PersonalAccessTokenRequestCancelledPayload",
    "PersonalAccessTokenRequestCreatedPayload",
    "PersonalAccessTokenRequestDeniedPayload",
    "PersonalAccessTokenRequestPermissionsAdded",
    "PersonalAccessTokenRequestPermissionsResult",
    "PersonalAccessTokenRequestPermissionsUpgraded",
    "PingPayload",
    "PingPayloadHook",
    "PingPayloadHookConfig",
    "ProjectCardConvertedPayload",
    "ProjectCardConvertedPayloadChanges",
    "ProjectCardConvertedPayloadChangesNote",
    "ProjectCardCreatedPayload",
    "ProjectCardDeletedPayload",
    "ProjectCardDeletedPayloadProjectCard",
    "ProjectCardEditedPayload",
    "ProjectCardEditedPayloadChanges",
    "ProjectCardEditedPayloadChangesNote",
    "ProjectCardMovedPayload",
    "ProjectCardMovedPayloadChanges",
    "ProjectCardMovedPayloadChangesColumnId",
    "ProjectClosedPayload",
    "ProjectColumnCreatedPayload",
    "ProjectColumnDeletedPayload",
    "ProjectColumnEditedPayload",
    "ProjectColumnEditedPayloadChanges",
    "ProjectColumnEditedPayloadChangesName",
    "ProjectColumnMovedPayload",
    "ProjectCreatedPayload",
    "ProjectDeletedPayload",
    "ProjectEditedPayload",
    "ProjectEditedPayloadChanges",
    "ProjectEditedPayloadChangesBody",
    "ProjectEditedPayloadChangesName",
    "ProjectReopenedPayload",
    "ProjectsV2",
    "ProjectsV2ClosedPayload",
    "ProjectsV2CreatedPayload",
    "ProjectsV2DeletedPayload",
    "ProjectsV2EditedPayload",
    "ProjectsV2EditedPayloadChanges",
    "ProjectsV2EditedPayloadChangesDescription",
    "ProjectsV2EditedPayloadChangesPublic",
    "ProjectsV2EditedPayloadChangesShortDescription",
    "ProjectsV2EditedPayloadChangesTitle",
    "ProjectsV2Item",
    "ProjectsV2ItemArchivedPayload",
    "ProjectsV2ItemConvertedPayload",
    "ProjectsV2ItemConvertedPayloadChanges",
    "ProjectsV2ItemConvertedPayloadChangesContentType",
    "ProjectsV2ItemCreatedPayload",
    "ProjectsV2ItemDeletedPayload",
    "ProjectsV2ItemEditedPayload",
    "ProjectsV2ItemEditedPayloadChangesOption1",
    "ProjectsV2ItemEditedPayloadChangesOption1FieldValue",
    "ProjectsV2ItemEditedPayloadChangesOption2",
    "ProjectsV2ItemEditedPayloadChangesOption2Body",
    "ProjectsV2ItemReorderedPayload",
    "ProjectsV2ItemReorderedPayloadChanges",
    "ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeId",
    "ProjectsV2ItemRestoredPayload",
    "ProjectsV2IterationSetting",
    "ProjectsV2ReopenedPayload",
    "ProjectsV2SingleSelectOption",
    "ProjectsV2StatusUpdate",
    "ProjectsV2StatusUpdateCreatedPayload",
    "ProjectsV2StatusUpdateDeletedPayload",
    "ProjectsV2StatusUpdateEditedPayload",
    "ProjectsV2StatusUpdateEditedPayloadChanges",
    "ProjectsV2StatusUpdateEditedPayloadChangesBody",
    "ProjectsV2StatusUpdateEditedPayloadChangesStartDate",
    "ProjectsV2StatusUpdateEditedPayloadChangesStatus",
    "ProjectsV2StatusUpdateEditedPayloadChangesTargetDate",
    "PublicPayload",
    "PullRequest",
    "PullRequestAssignedPayload",
    "PullRequestAssignedPayloadPullRequest",
    "PullRequestAssignedPayloadPullRequestBase",
    "PullRequestAssignedPayloadPullRequestBaseRepo",
    "PullRequestAssignedPayloadPullRequestBaseRepoPermissions",
    "PullRequestAssignedPayloadPullRequestHead",
    "PullRequestAssignedPayloadPullRequestLabel",
    "PullRequestAssignedPayloadPullRequestLinks",
    "PullRequestAssignedPayloadPullRequestLinksComments",
    "PullRequestAssignedPayloadPullRequestLinksCommits",
    "PullRequestAssignedPayloadPullRequestLinksHtml",
    "PullRequestAssignedPayloadPullRequestLinksIssue",
    "PullRequestAssignedPayloadPullRequestLinksReviewComment",
    "PullRequestAssignedPayloadPullRequestLinksReviewComments",
    "PullRequestAssignedPayloadPullRequestLinksSelf",
    "PullRequestAssignedPayloadPullRequestLinksStatuses",
    "PullRequestAssignedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestAssignedPayloadPullRequestRequestedTeam",
    "PullRequestAutoMergeDisabledPayload",
    "PullRequestAutoMergeDisabledPayloadPullRequest",
    "PullRequestAutoMergeDisabledPayloadPullRequestBase",
    "PullRequestAutoMergeDisabledPayloadPullRequestBaseRepo",
    "PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissions",
    "PullRequestAutoMergeDisabledPayloadPullRequestHead",
    "PullRequestAutoMergeDisabledPayloadPullRequestHeadRepo",
    "PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissions",
    "PullRequestAutoMergeDisabledPayloadPullRequestLabel",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinks",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksComments",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksCommits",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksHtml",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksIssue",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComment",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComments",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksSelf",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksStatuses",
    "PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2",
    "PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeam",
    "PullRequestAutoMergeEnabledPayload",
    "PullRequestAutoMergeEnabledPayloadPullRequest",
    "PullRequestAutoMergeEnabledPayloadPullRequestBase",
    "PullRequestAutoMergeEnabledPayloadPullRequestBaseRepo",
    "PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissions",
    "PullRequestAutoMergeEnabledPayloadPullRequestHead",
    "PullRequestAutoMergeEnabledPayloadPullRequestHeadRepo",
    "PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissions",
    "PullRequestAutoMergeEnabledPayloadPullRequestLabel",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinks",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksComments",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksCommits",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksHtml",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksIssue",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComment",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComments",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksSelf",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksStatuses",
    "PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2",
    "PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeam",
    "PullRequestBase",
    "PullRequestClosedPayload",
    "PullRequestConvertedToDraftPayload",
    "PullRequestDemilestonedPayload",
    "PullRequestDequeuedPayload",
    "PullRequestDequeuedPayloadPullRequest",
    "PullRequestDequeuedPayloadPullRequestBase",
    "PullRequestDequeuedPayloadPullRequestBaseRepo",
    "PullRequestDequeuedPayloadPullRequestBaseRepoPermissions",
    "PullRequestDequeuedPayloadPullRequestHead",
    "PullRequestDequeuedPayloadPullRequestHeadRepo",
    "PullRequestDequeuedPayloadPullRequestHeadRepoPermissions",
    "PullRequestDequeuedPayloadPullRequestLabel",
    "PullRequestDequeuedPayloadPullRequestLinks",
    "PullRequestDequeuedPayloadPullRequestLinksComments",
    "PullRequestDequeuedPayloadPullRequestLinksCommits",
    "PullRequestDequeuedPayloadPullRequestLinksHtml",
    "PullRequestDequeuedPayloadPullRequestLinksIssue",
    "PullRequestDequeuedPayloadPullRequestLinksReviewComment",
    "PullRequestDequeuedPayloadPullRequestLinksReviewComments",
    "PullRequestDequeuedPayloadPullRequestLinksSelf",
    "PullRequestDequeuedPayloadPullRequestLinksStatuses",
    "PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestDequeuedPayloadPullRequestRequestedTeam",
    "PullRequestEditedPayload",
    "PullRequestEditedPayloadChanges",
    "PullRequestEditedPayloadChangesBase",
    "PullRequestEditedPayloadChangesBaseRef",
    "PullRequestEditedPayloadChangesBaseSha",
    "PullRequestEditedPayloadChangesBody",
    "PullRequestEditedPayloadChangesTitle",
    "PullRequestEnqueuedPayload",
    "PullRequestEnqueuedPayloadPullRequest",
    "PullRequestEnqueuedPayloadPullRequestBase",
    "PullRequestEnqueuedPayloadPullRequestBaseRepo",
    "PullRequestEnqueuedPayloadPullRequestBaseRepoPermissions",
    "PullRequestEnqueuedPayloadPullRequestHead",
    "PullRequestEnqueuedPayloadPullRequestHeadRepo",
    "PullRequestEnqueuedPayloadPullRequestHeadRepoPermissions",
    "PullRequestEnqueuedPayloadPullRequestLabel",
    "PullRequestEnqueuedPayloadPullRequestLinks",
    "PullRequestEnqueuedPayloadPullRequestLinksComments",
    "PullRequestEnqueuedPayloadPullRequestLinksCommits",
    "PullRequestEnqueuedPayloadPullRequestLinksHtml",
    "PullRequestEnqueuedPayloadPullRequestLinksIssue",
    "PullRequestEnqueuedPayloadPullRequestLinksReviewComment",
    "PullRequestEnqueuedPayloadPullRequestLinksReviewComments",
    "PullRequestEnqueuedPayloadPullRequestLinksSelf",
    "PullRequestEnqueuedPayloadPullRequestLinksStatuses",
    "PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestEnqueuedPayloadPullRequestRequestedTeam",
    "PullRequestHead",
    "PullRequestLabel",
    "PullRequestLabeledPayload",
    "PullRequestLabeledPayloadPullRequest",
    "PullRequestLabeledPayloadPullRequestBase",
    "PullRequestLabeledPayloadPullRequestBaseRepo",
    "PullRequestLabeledPayloadPullRequestBaseRepoPermissions",
    "PullRequestLabeledPayloadPullRequestHead",
    "PullRequestLabeledPayloadPullRequestLabel",
    "PullRequestLabeledPayloadPullRequestLinks",
    "PullRequestLabeledPayloadPullRequestLinksComments",
    "PullRequestLabeledPayloadPullRequestLinksCommits",
    "PullRequestLabeledPayloadPullRequestLinksHtml",
    "PullRequestLabeledPayloadPullRequestLinksIssue",
    "PullRequestLabeledPayloadPullRequestLinksReviewComment",
    "PullRequestLabeledPayloadPullRequestLinksReviewComments",
    "PullRequestLabeledPayloadPullRequestLinksSelf",
    "PullRequestLabeledPayloadPullRequestLinksStatuses",
    "PullRequestLabeledPayloadPullRequestRequestedReviewerOption2",
    "PullRequestLabeledPayloadPullRequestRequestedTeam",
    "PullRequestLinks",
    "PullRequestLockedPayload",
    "PullRequestLockedPayloadPullRequest",
    "PullRequestLockedPayloadPullRequestBase",
    "PullRequestLockedPayloadPullRequestBaseRepo",
    "PullRequestLockedPayloadPullRequestBaseRepoPermissions",
    "PullRequestLockedPayloadPullRequestHead",
    "PullRequestLockedPayloadPullRequestLabel",
    "PullRequestLockedPayloadPullRequestLinks",
    "PullRequestLockedPayloadPullRequestLinksComments",
    "PullRequestLockedPayloadPullRequestLinksCommits",
    "PullRequestLockedPayloadPullRequestLinksHtml",
    "PullRequestLockedPayloadPullRequestLinksIssue",
    "PullRequestLockedPayloadPullRequestLinksReviewComment",
    "PullRequestLockedPayloadPullRequestLinksReviewComments",
    "PullRequestLockedPayloadPullRequestLinksSelf",
    "PullRequestLockedPayloadPullRequestLinksStatuses",
    "PullRequestLockedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestLockedPayloadPullRequestRequestedTeam",
    "PullRequestMilestonedPayload",
    "PullRequestMinimal",
    "PullRequestMinimalBase",
    "PullRequestMinimalBaseRepo",
    "PullRequestMinimalHead",
    "PullRequestMinimalHeadRepo",
    "PullRequestOpenedPayload",
    "PullRequestPayload",
    "PullRequestPayload2",
    "PullRequestReadyForReviewPayload",
    "PullRequestReopenedPayload",
    "PullRequestReviewCommentCreatedPayload",
    "PullRequestReviewCommentCreatedPayloadComment",
    "PullRequestReviewCommentCreatedPayloadCommentLinks",
    "PullRequestReviewCommentCreatedPayloadCommentLinksHtml",
    "PullRequestReviewCommentCreatedPayloadCommentLinksPullRequest",
    "PullRequestReviewCommentCreatedPayloadCommentLinksSelf",
    "PullRequestReviewCommentCreatedPayloadCommentReactions",
    "PullRequestReviewCommentCreatedPayloadPullRequest",
    "PullRequestReviewCommentCreatedPayloadPullRequestBase",
    "PullRequestReviewCommentCreatedPayloadPullRequestBaseRepo",
    "PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewCommentCreatedPayloadPullRequestHead",
    "PullRequestReviewCommentCreatedPayloadPullRequestLabel",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinks",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksComments",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksCommits",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksHtml",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksIssue",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksSelf",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksStatuses",
    "PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeam",
    "PullRequestReviewCommentDeletedPayload",
    "PullRequestReviewCommentDeletedPayloadPullRequest",
    "PullRequestReviewCommentDeletedPayloadPullRequestBase",
    "PullRequestReviewCommentDeletedPayloadPullRequestBaseRepo",
    "PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewCommentDeletedPayloadPullRequestHead",
    "PullRequestReviewCommentDeletedPayloadPullRequestLabel",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinks",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksComments",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksCommits",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksHtml",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksIssue",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksSelf",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksStatuses",
    "PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeam",
    "PullRequestReviewCommentEditedPayload",
    "PullRequestReviewCommentEditedPayloadPullRequest",
    "PullRequestReviewCommentEditedPayloadPullRequestBase",
    "PullRequestReviewCommentEditedPayloadPullRequestBaseRepo",
    "PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewCommentEditedPayloadPullRequestHead",
    "PullRequestReviewCommentEditedPayloadPullRequestLabel",
    "PullRequestReviewCommentEditedPayloadPullRequestLinks",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksComments",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksCommits",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksHtml",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksIssue",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksSelf",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksStatuses",
    "PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewCommentEditedPayloadPullRequestRequestedTeam",
    "PullRequestReviewDismissedPayload",
    "PullRequestReviewDismissedPayloadPullRequest",
    "PullRequestReviewDismissedPayloadPullRequestBase",
    "PullRequestReviewDismissedPayloadPullRequestBaseRepo",
    "PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewDismissedPayloadPullRequestHead",
    "PullRequestReviewDismissedPayloadPullRequestLabel",
    "PullRequestReviewDismissedPayloadPullRequestLinks",
    "PullRequestReviewDismissedPayloadPullRequestLinksComments",
    "PullRequestReviewDismissedPayloadPullRequestLinksCommits",
    "PullRequestReviewDismissedPayloadPullRequestLinksHtml",
    "PullRequestReviewDismissedPayloadPullRequestLinksIssue",
    "PullRequestReviewDismissedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewDismissedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewDismissedPayloadPullRequestLinksSelf",
    "PullRequestReviewDismissedPayloadPullRequestLinksStatuses",
    "PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewDismissedPayloadPullRequestRequestedTeam",
    "PullRequestReviewDismissedPayloadReview",
    "PullRequestReviewDismissedPayloadReviewLinks",
    "PullRequestReviewDismissedPayloadReviewLinksHtml",
    "PullRequestReviewDismissedPayloadReviewLinksPullRequest",
    "PullRequestReviewEditedPayload",
    "PullRequestReviewEditedPayloadChanges",
    "PullRequestReviewEditedPayloadChangesBody",
    "PullRequestReviewEditedPayloadPullRequest",
    "PullRequestReviewEditedPayloadPullRequestBase",
    "PullRequestReviewEditedPayloadPullRequestBaseRepo",
    "PullRequestReviewEditedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewEditedPayloadPullRequestHead",
    "PullRequestReviewEditedPayloadPullRequestLabel",
    "PullRequestReviewEditedPayloadPullRequestLinks",
    "PullRequestReviewEditedPayloadPullRequestLinksComments",
    "PullRequestReviewEditedPayloadPullRequestLinksCommits",
    "PullRequestReviewEditedPayloadPullRequestLinksHtml",
    "PullRequestReviewEditedPayloadPullRequestLinksIssue",
    "PullRequestReviewEditedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewEditedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewEditedPayloadPullRequestLinksSelf",
    "PullRequestReviewEditedPayloadPullRequestLinksStatuses",
    "PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewEditedPayloadPullRequestRequestedTeam",
    "PullRequestReviewSubmittedPayload",
    "PullRequestReviewSubmittedPayloadPullRequest",
    "PullRequestReviewSubmittedPayloadPullRequestBase",
    "PullRequestReviewSubmittedPayloadPullRequestBaseRepo",
    "PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewSubmittedPayloadPullRequestHead",
    "PullRequestReviewSubmittedPayloadPullRequestLabel",
    "PullRequestReviewSubmittedPayloadPullRequestLinks",
    "PullRequestReviewSubmittedPayloadPullRequestLinksComments",
    "PullRequestReviewSubmittedPayloadPullRequestLinksCommits",
    "PullRequestReviewSubmittedPayloadPullRequestLinksHtml",
    "PullRequestReviewSubmittedPayloadPullRequestLinksIssue",
    "PullRequestReviewSubmittedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewSubmittedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewSubmittedPayloadPullRequestLinksSelf",
    "PullRequestReviewSubmittedPayloadPullRequestLinksStatuses",
    "PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewSubmittedPayloadPullRequestRequestedTeam",
    "PullRequestReviewThreadResolvedPayload",
    "PullRequestReviewThreadResolvedPayloadPullRequest",
    "PullRequestReviewThreadResolvedPayloadPullRequestBase",
    "PullRequestReviewThreadResolvedPayloadPullRequestBaseRepo",
    "PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewThreadResolvedPayloadPullRequestHead",
    "PullRequestReviewThreadResolvedPayloadPullRequestLabel",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinks",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksComments",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksCommits",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksHtml",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksIssue",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksSelf",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksStatuses",
    "PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeam",
    "PullRequestReviewThreadResolvedPayloadThread",
    "PullRequestReviewThreadResolvedPayloadThreadComment",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinks",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtml",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequest",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelf",
    "PullRequestReviewThreadResolvedPayloadThreadCommentReactions",
    "PullRequestReviewThreadUnresolvedPayload",
    "PullRequestReviewThreadUnresolvedPayloadPullRequest",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBase",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepo",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissions",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHead",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepo",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissions",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLabel",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinks",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksComments",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommits",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtml",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssue",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComment",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComments",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelf",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatuses",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeam",
    "PullRequestReviewThreadUnresolvedPayloadThread",
    "PullRequestReviewThreadUnresolvedPayloadThreadComment",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinks",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtml",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequest",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelf",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentReactions",
    "PullRequestSynchronizePayload",
    "PullRequestSynchronizePayloadPullRequest",
    "PullRequestSynchronizePayloadPullRequestBase",
    "PullRequestSynchronizePayloadPullRequestBaseRepo",
    "PullRequestSynchronizePayloadPullRequestBaseRepoPermissions",
    "PullRequestSynchronizePayloadPullRequestHead",
    "PullRequestSynchronizePayloadPullRequestHeadRepo",
    "PullRequestSynchronizePayloadPullRequestHeadRepoPermissions",
    "PullRequestSynchronizePayloadPullRequestLabel",
    "PullRequestSynchronizePayloadPullRequestLinks",
    "PullRequestSynchronizePayloadPullRequestLinksComments",
    "PullRequestSynchronizePayloadPullRequestLinksCommits",
    "PullRequestSynchronizePayloadPullRequestLinksHtml",
    "PullRequestSynchronizePayloadPullRequestLinksIssue",
    "PullRequestSynchronizePayloadPullRequestLinksReviewComment",
    "PullRequestSynchronizePayloadPullRequestLinksReviewComments",
    "PullRequestSynchronizePayloadPullRequestLinksSelf",
    "PullRequestSynchronizePayloadPullRequestLinksStatuses",
    "PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2",
    "PullRequestSynchronizePayloadPullRequestRequestedTeam",
    "PullRequestUnassignedPayload",
    "PullRequestUnassignedPayloadPullRequest",
    "PullRequestUnassignedPayloadPullRequestBase",
    "PullRequestUnassignedPayloadPullRequestBaseRepo",
    "PullRequestUnassignedPayloadPullRequestBaseRepoPermissions",
    "PullRequestUnassignedPayloadPullRequestHead",
    "PullRequestUnassignedPayloadPullRequestLabel",
    "PullRequestUnassignedPayloadPullRequestLinks",
    "PullRequestUnassignedPayloadPullRequestLinksComments",
    "PullRequestUnassignedPayloadPullRequestLinksCommits",
    "PullRequestUnassignedPayloadPullRequestLinksHtml",
    "PullRequestUnassignedPayloadPullRequestLinksIssue",
    "PullRequestUnassignedPayloadPullRequestLinksReviewComment",
    "PullRequestUnassignedPayloadPullRequestLinksReviewComments",
    "PullRequestUnassignedPayloadPullRequestLinksSelf",
    "PullRequestUnassignedPayloadPullRequestLinksStatuses",
    "PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestUnassignedPayloadPullRequestRequestedTeam",
    "PullRequestUnlabeledPayload",
    "PullRequestUnlabeledPayloadPullRequest",
    "PullRequestUnlabeledPayloadPullRequestBase",
    "PullRequestUnlabeledPayloadPullRequestBaseRepo",
    "PullRequestUnlabeledPayloadPullRequestBaseRepoPermissions",
    "PullRequestUnlabeledPayloadPullRequestHead",
    "PullRequestUnlabeledPayloadPullRequestLabel",
    "PullRequestUnlabeledPayloadPullRequestLinks",
    "PullRequestUnlabeledPayloadPullRequestLinksComments",
    "PullRequestUnlabeledPayloadPullRequestLinksCommits",
    "PullRequestUnlabeledPayloadPullRequestLinksHtml",
    "PullRequestUnlabeledPayloadPullRequestLinksIssue",
    "PullRequestUnlabeledPayloadPullRequestLinksReviewComment",
    "PullRequestUnlabeledPayloadPullRequestLinksReviewComments",
    "PullRequestUnlabeledPayloadPullRequestLinksSelf",
    "PullRequestUnlabeledPayloadPullRequestLinksStatuses",
    "PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2",
    "PullRequestUnlabeledPayloadPullRequestRequestedTeam",
    "PullRequestUnlockedPayload",
    "PullRequestUnlockedPayloadPullRequest",
    "PullRequestUnlockedPayloadPullRequestBase",
    "PullRequestUnlockedPayloadPullRequestBaseRepo",
    "PullRequestUnlockedPayloadPullRequestBaseRepoPermissions",
    "PullRequestUnlockedPayloadPullRequestHead",
    "PullRequestUnlockedPayloadPullRequestLabel",
    "PullRequestUnlockedPayloadPullRequestLinks",
    "PullRequestUnlockedPayloadPullRequestLinksComments",
    "PullRequestUnlockedPayloadPullRequestLinksCommits",
    "PullRequestUnlockedPayloadPullRequestLinksHtml",
    "PullRequestUnlockedPayloadPullRequestLinksIssue",
    "PullRequestUnlockedPayloadPullRequestLinksReviewComment",
    "PullRequestUnlockedPayloadPullRequestLinksReviewComments",
    "PullRequestUnlockedPayloadPullRequestLinksSelf",
    "PullRequestUnlockedPayloadPullRequestLinksStatuses",
    "PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2",
    "PullRequestUnlockedPayloadPullRequestRequestedTeam",
    "PushPayload",
    "PushPayloadCommit",
    "PushPayloadCommitAuthor",
    "PushPayloadCommitCommitter",
    "PushPayloadPusher",
    "PushPayloadRepository",
    "PushPayloadRepositoryPermissions",
    "ReactionRollup",
    "RegistryPackagePublishedPayload",
    "RegistryPackagePublishedPayloadRegistryPackage",
    "RegistryPackagePublishedPayloadRegistryPackageOwner",
    "RegistryPackageUpdatedPayload",
    "RegistryPackageUpdatedPayloadRegistryPackage",
    "RegistryPackageUpdatedPayloadRegistryPackageOwner",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersion",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthor",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFile",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionRelease",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthor",
    "ReleaseCreatedPayload",
    "ReleaseDeletedPayload",
    "ReleaseEditedPayload",
    "ReleaseEditedPayloadChanges",
    "ReleaseEditedPayloadChangesBody",
    "ReleaseEditedPayloadChangesMakeLatest",
    "ReleaseEditedPayloadChangesName",
    "ReleaseEditedPayloadChangesTagName",
    "ReleasePrereleasedPayload",
    "ReleasePrereleasedPayloadRelease",
    "ReleasePrereleasedPayloadReleaseReactions",
    "ReleasePublishedPayload",
    "ReleaseReleasedPayload",
    "ReleaseUnpublishedPayload",
    "Repository",
    "Repository2",
    "Repository2CodeSearchIndexStatus",
    "Repository2Permissions",
    "RepositoryAdvisory",
    "RepositoryAdvisoryIdentifier",
    "RepositoryAdvisoryPublishedPayload",
    "RepositoryAdvisoryReportedPayload",
    "RepositoryArchivedPayload",
    "RepositoryCreatedPayload",
    "RepositoryDeletedPayload",
    "RepositoryDispatchPayload",
    "RepositoryEditedPayload",
    "RepositoryEditedPayloadChanges",
    "RepositoryEditedPayloadChangesDefaultBranch",
    "RepositoryEditedPayloadChangesDescription",
    "RepositoryEditedPayloadChangesHomepage",
    "RepositoryEditedPayloadChangesTopics",
    "RepositoryImportPayload",
    "RepositoryPermissions",
    "RepositoryPrivatizedPayload",
    "RepositoryPublicizedPayload",
    "RepositoryRenamedPayload",
    "RepositoryRenamedPayloadChanges",
    "RepositoryRenamedPayloadChangesRepository",
    "RepositoryRenamedPayloadChangesRepositoryName",
    "RepositoryRuleBranchNamePattern",
    "RepositoryRuleBranchNamePatternParameters",
    "RepositoryRuleCodeScanning",
    "RepositoryRuleCodeScanningParameters",
    "RepositoryRuleCommitAuthorEmailPattern",
    "RepositoryRuleCommitAuthorEmailPatternParameters",
    "RepositoryRuleCommitMessagePattern",
    "RepositoryRuleCommitMessagePatternParameters",
    "RepositoryRuleCommitterEmailPattern",
    "RepositoryRuleCommitterEmailPatternParameters",
    "RepositoryRuleCopilotCodeReview",
    "RepositoryRuleCopilotCodeReviewParameters",
    "RepositoryRuleCreation",
    "RepositoryRuleDeletion",
    "RepositoryRuleFileExtensionRestriction",
    "RepositoryRuleFileExtensionRestrictionParameters",
    "RepositoryRuleFilePathRestriction",
    "RepositoryRuleFilePathRestrictionParameters",
    "RepositoryRuleMaxFilePathLength",
    "RepositoryRuleMaxFilePathLengthParameters",
    "RepositoryRuleMaxFileSize",
    "RepositoryRuleMaxFileSizeParameters",
    "RepositoryRuleMergeQueue",
    "RepositoryRuleMergeQueueParameters",
    "RepositoryRuleNonFastForward",
    "RepositoryRuleParamsCodeScanningTool",
    "RepositoryRuleParamsRequiredReviewerConfiguration",
    "RepositoryRuleParamsReviewer",
    "RepositoryRuleParamsStatusCheckConfiguration",
    "RepositoryRuleParamsWorkflowFileReference",
    "RepositoryRulePullRequest",
    "RepositoryRulePullRequestParameters",
    "RepositoryRuleRequiredDeployments",
    "RepositoryRuleRequiredDeploymentsParameters",
    "RepositoryRuleRequiredLinearHistory",
    "RepositoryRuleRequiredSignatures",
    "RepositoryRuleRequiredStatusChecks",
    "RepositoryRuleRequiredStatusChecksParameters",
    "RepositoryRuleTagNamePattern",
    "RepositoryRuleTagNamePatternParameters",
    "RepositoryRuleUpdate",
    "RepositoryRuleUpdateParameters",
    "RepositoryRuleWorkflows",
    "RepositoryRuleWorkflowsParameters",
    "RepositoryRuleset",
    "RepositoryRulesetBypassActor",
    "RepositoryRulesetConditions",
    "RepositoryRulesetConditionsRefName",
    "RepositoryRulesetCreatedPayload",
    "RepositoryRulesetDeletedPayload",
    "RepositoryRulesetEditedPayload",
    "RepositoryRulesetEditedPayloadChanges",
    "RepositoryRulesetEditedPayloadChangesConditions",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdated",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChanges",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionType",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExclude",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesInclude",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTarget",
    "RepositoryRulesetEditedPayloadChangesEnforcement",
    "RepositoryRulesetEditedPayloadChangesName",
    "RepositoryRulesetEditedPayloadChangesRules",
    "RepositoryRulesetEditedPayloadChangesRulesUpdated",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChanges",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfiguration",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPattern",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleType",
    "RepositoryRulesetLinks",
    "RepositoryRulesetLinksSelf",
    "RepositoryTransferredPayload",
    "RepositoryTransferredPayloadChanges",
    "RepositoryTransferredPayloadChangesOwner",
    "RepositoryTransferredPayloadChangesOwnerFrom",
    "RepositoryTransferredPayloadChangesOwnerFromOrganization",
    "RepositoryUnarchivedPayload",
    "RepositoryVulnerabilityAlertCreatePayload",
    "RepositoryVulnerabilityAlertDismissPayload",
    "RepositoryVulnerabilityAlertDismissPayloadAlert",
    "RepositoryVulnerabilityAlertReopenPayload",
    "RepositoryVulnerabilityAlertResolvePayload",
    "RepositoryVulnerabilityAlertResolvePayloadAlert",
    "SecretScanningAlertAssignedPayload",
    "SecretScanningAlertCreatedPayload",
    "SecretScanningAlertLocationCreatedPayload",
    "SecretScanningAlertPubliclyLeakedPayload",
    "SecretScanningAlertReopenedPayload",
    "SecretScanningAlertResolvedPayload",
    "SecretScanningAlertUnassignedPayload",
    "SecretScanningAlertValidatedPayload",
    "SecretScanningAlertWebhook",
    "SecretScanningLocation",
    "SecretScanningLocationCommit",
    "SecretScanningLocationDiscussionBody",
    "SecretScanningLocationDiscussionComment",
    "SecretScanningLocationDiscussionTitle",
    "SecretScanningLocationIssueBody",
    "SecretScanningLocationIssueComment",
    "SecretScanningLocationIssueTitle",
    "SecretScanningLocationPullRequestBody",
    "SecretScanningLocationPullRequestComment",
    "SecretScanningLocationPullRequestReview",
    "SecretScanningLocationPullRequestReviewComment",
    "SecretScanningLocationPullRequestTitle",
    "SecretScanningLocationWikiCommit",
    "SecretScanningScanCompletedPayload",
    "SecurityAdvisoryPublishedPayload",
    "SecurityAdvisoryUpdatedPayload",
    "SecurityAdvisoryWithdrawnPayload",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisory",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvss",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCwe",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifier",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReference",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerability",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackage",
    "SecurityAndAnalysisPayload",
    "SecurityAndAnalysisPayloadChanges",
    "SecurityAndAnalysisPayloadChangesFrom",
    "SimpleCheckSuite",
    "SimpleCommit",
    "SponsorshipCancelledPayload",
    "SponsorshipCreatedPayload",
    "SponsorshipEditedPayload",
    "SponsorshipEditedPayloadChanges",
    "SponsorshipEditedPayloadChangesPrivacyLevel",
    "SponsorshipPendingCancellationPayload",
    "SponsorshipPendingTierChangePayload",
    "SponsorshipTierChangedPayload",
    "StarCreatedPayload",
    "StarDeletedPayload",
    "StatusPayload",
    "StatusPayloadBranche",
    "StatusPayloadBrancheCommit",
    "StatusPayloadCommit",
    "StatusPayloadCommitCommit",
    "StatusPayloadCommitCommitTree",
    "StatusPayloadCommitCommitVerification",
    "StatusPayloadCommitParent",
    "SubIssuesParentIssueAddedPayload",
    "SubIssuesParentIssueRemovedPayload",
    "SubIssuesSubIssueAddedPayload",
    "SubIssuesSubIssueRemovedPayload",
    "SubIssuesSummary",
    "TeamAddPayload",
    "TeamAddedToRepositoryPayload",
    "TeamAddedToRepositoryPayloadRepository",
    "TeamAddedToRepositoryPayloadRepositoryPermissions",
    "TeamCreatedPayload",
    "TeamCreatedPayloadRepository",
    "TeamCreatedPayloadRepositoryPermissions",
    "TeamDeletedPayload",
    "TeamDeletedPayloadRepository",
    "TeamDeletedPayloadRepositoryPermissions",
    "TeamEditedPayload",
    "TeamEditedPayloadChanges",
    "TeamEditedPayloadChangesDescription",
    "TeamEditedPayloadChangesName",
    "TeamEditedPayloadChangesNotificationSetting",
    "TeamEditedPayloadChangesPrivacy",
    "TeamEditedPayloadChangesRepository",
    "TeamEditedPayloadChangesRepositoryPermissions",
    "TeamEditedPayloadChangesRepositoryPermissionsFrom",
    "TeamEditedPayloadRepository",
    "TeamEditedPayloadRepositoryPermissions",
    "TeamRemovedFromRepositoryPayload",
    "TeamRemovedFromRepositoryPayloadRepository",
    "TeamRemovedFromRepositoryPayloadRepositoryPermissions",
    "User",
    "WatchStartedPayload",
    "WebhookPayloadModel",
    "WebhookRubygemsMetadata",
    "WebhookRubygemsMetadataVersionInfo",
    "WebhooksAlert",
    "WebhooksAnswer",
    "WebhooksAnswerReactions",
    "WebhooksApprover",
    "WebhooksChanges",
    "WebhooksChanges8",
    "WebhooksChanges8Tier",
    "WebhooksChanges8TierFrom",
    "WebhooksChangesBody",
    "WebhooksComment",
    "WebhooksCommentReactions",
    "WebhooksDeployKey",
    "WebhooksIssue",
    "WebhooksIssue2",
    "WebhooksIssue2Label",
    "WebhooksIssue2PullRequest",
    "WebhooksIssue2Reactions",
    "WebhooksIssueComment",
    "WebhooksIssueCommentReactions",
    "WebhooksIssueLabel",
    "WebhooksIssuePullRequest",
    "WebhooksIssueReactions",
    "WebhooksLabel",
    "WebhooksMarketplacePurchase",
    "WebhooksMarketplacePurchaseAccount",
    "WebhooksMarketplacePurchasePlan",
    "WebhooksMembership",
    "WebhooksMilestone",
    "WebhooksPreviousMarketplacePurchase",
    "WebhooksPreviousMarketplacePurchaseAccount",
    "WebhooksPreviousMarketplacePurchasePlan",
    "WebhooksProject",
    "WebhooksProjectCard",
    "WebhooksProjectChanges",
    "WebhooksProjectChangesArchivedAt",
    "WebhooksProjectColumn",
    "WebhooksPullRequest5",
    "WebhooksPullRequest5Base",
    "WebhooksPullRequest5BaseRepo",
    "WebhooksPullRequest5BaseRepoPermissions",
    "WebhooksPullRequest5Head",
    "WebhooksPullRequest5HeadRepo",
    "WebhooksPullRequest5HeadRepoPermissions",
    "WebhooksPullRequest5Label",
    "WebhooksPullRequest5Links",
    "WebhooksPullRequest5LinksComments",
    "WebhooksPullRequest5LinksCommits",
    "WebhooksPullRequest5LinksHtml",
    "WebhooksPullRequest5LinksIssue",
    "WebhooksPullRequest5LinksReviewComment",
    "WebhooksPullRequest5LinksReviewComments",
    "WebhooksPullRequest5LinksSelf",
    "WebhooksPullRequest5LinksStatuses",
    "WebhooksPullRequest5RequestedReviewerOption2",
    "WebhooksPullRequest5RequestedTeam",
    "WebhooksRelease",
    "WebhooksRelease1",
    "WebhooksRelease1Reactions",
    "WebhooksReleaseAsset",
    "WebhooksReleaseReactions",
    "WebhooksReview",
    "WebhooksReviewComment",
    "WebhooksReviewCommentLinks",
    "WebhooksReviewCommentLinksHtml",
    "WebhooksReviewCommentLinksPullRequest",
    "WebhooksReviewCommentLinksSelf",
    "WebhooksReviewCommentReactions",
    "WebhooksReviewLinks",
    "WebhooksReviewLinksHtml",
    "WebhooksReviewLinksPullRequest",
    "WebhooksRule",
    "WebhooksSecurityAdvisory",
    "WebhooksSecurityAdvisoryCvss",
    "WebhooksSecurityAdvisoryCwe",
    "WebhooksSecurityAdvisoryIdentifier",
    "WebhooksSecurityAdvisoryReference",
    "WebhooksSecurityAdvisoryVulnerability",
    "WebhooksSecurityAdvisoryVulnerabilityPackage",
    "WebhooksSponsorship",
    "WebhooksSponsorshipMaintainer",
    "WebhooksSponsorshipTier",
    "WebhooksTeam",
    "WebhooksTeam1",
    "WebhooksWorkflowJobRun",
    "WorkflowDispatchPayload",
    "WorkflowJobCompletedPayload",
    "WorkflowJobInProgressPayload",
    "WorkflowJobQueuedPayload",
    "WorkflowJobQueuedPayloadWorkflowJob",
    "WorkflowJobQueuedPayloadWorkflowJobStep",
    "WorkflowJobWaitingPayload",
    "WorkflowJobWaitingPayloadWorkflowJob",
    "WorkflowJobWaitingPayloadWorkflowJobStep",
    "WorkflowRunCompletedPayload",
    "WorkflowRunCompletedPayloadWorkflowRun",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommit",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthor",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitter",
    "WorkflowRunCompletedPayloadWorkflowRunHeadRepository",
    "WorkflowRunCompletedPayloadWorkflowRunRepository",
    "WorkflowRunInProgressPayload",
    "WorkflowRunInProgressPayloadWorkflowRun",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommit",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthor",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitter",
    "WorkflowRunInProgressPayloadWorkflowRunHeadRepository",
    "WorkflowRunInProgressPayloadWorkflowRunRepository",
    "WorkflowRunRequestedPayload",
    "WorkflowRunRequestedPayloadWorkflowRun",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommit",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthor",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitter",
    "WorkflowRunRequestedPayloadWorkflowRunHeadRepository",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequest",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestBase",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepo",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestHead",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepo",
    "WorkflowRunRequestedPayloadWorkflowRunRepository",
]


class BranchProtectionRuleEditedPayloadChangesAdminEnforced(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesAdminEnforced."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | bool = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesAuthorizedActorNames(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesAuthorizedActorNames."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: list[str] = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnly(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnly."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | bool = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnly(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnly."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | bool = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevel(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesLockAllowsForkSync(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesLockAllowsForkSync."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | bool = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevel(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevel(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesRequireLastPushApproval(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesRequireLastPushApproval."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | bool = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesRequiredStatusChecks(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesRequiredStatusChecks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: list[str] = Field(alias="from")


class BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevel(BaseModel):
    """BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class CheckRunRequestedActionPayloadRequestedAction(BaseModel):
    """The action requested by the user."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    identifier: str | None = None


class CheckRunWithSimpleCheckSuiteOutput(BaseModel):
    """CheckRunWithSimpleCheckSuiteOutput."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    annotations_count: int
    annotations_url: str
    summary: None | str
    text: None | str
    title: None | str


class CheckSuiteCompletedPayloadCheckSuiteAppPermissions(BaseModel):
    """The set of permissions for the GitHub app."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actions: Literal["read", "write"] | None = None
    administration: Literal["read", "write"] | None = None
    checks: Literal["read", "write"] | None = None
    content_references: Literal["read", "write"] | None = None
    contents: Literal["read", "write"] | None = None
    deployments: Literal["read", "write"] | None = None
    discussions: Literal["read", "write"] | None = None
    emails: Literal["read", "write"] | None = None
    environments: Literal["read", "write"] | None = None
    issues: Literal["read", "write"] | None = None
    keys: Literal["read", "write"] | None = None
    members: Literal["read", "write"] | None = None
    metadata: Literal["read", "write"] | None = None
    organization_administration: Literal["read", "write"] | None = None
    organization_hooks: Literal["read", "write"] | None = None
    organization_packages: Literal["read", "write"] | None = None
    organization_plan: Literal["read", "write"] | None = None
    organization_projects: Literal["read", "write", "admin"] | None = None
    organization_secrets: Literal["read", "write"] | None = None
    organization_self_hosted_runners: Literal["read", "write"] | None = None
    organization_user_blocking: Literal["read", "write"] | None = None
    packages: Literal["read", "write"] | None = None
    pages: Literal["read", "write"] | None = None
    pull_requests: Literal["read", "write"] | None = None
    repository_hooks: Literal["read", "write"] | None = None
    repository_projects: Literal["read", "write", "admin"] | None = None
    secret_scanning_alerts: Literal["read", "write"] | None = None
    secrets: Literal["read", "write"] | None = None
    security_events: Literal["read", "write"] | None = None
    security_scanning_alert: Literal["read", "write"] | None = None
    single_file: Literal["read", "write"] | None = None
    statuses: Literal["read", "write"] | None = None
    team_discussions: Literal["read", "write"] | None = None
    vulnerability_alerts: Literal["read", "write"] | None = None
    workflows: Literal["read", "write"] | None = None


class CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CheckSuiteRequestedPayloadCheckSuiteAppPermissions(BaseModel):
    """The set of permissions for the GitHub app."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actions: Literal["read", "write"] | None = None
    administration: Literal["read", "write"] | None = None
    artifact_metadata: Literal["read", "write"] | None = None
    attestations: Literal["read", "write"] | None = None
    checks: Literal["read", "write"] | None = None
    content_references: Literal["read", "write"] | None = None
    contents: Literal["read", "write"] | None = None
    copilot_requests: Literal["write"] | None = None
    deployments: Literal["read", "write"] | None = None
    discussions: Literal["read", "write"] | None = None
    emails: Literal["read", "write"] | None = None
    environments: Literal["read", "write"] | None = None
    issues: Literal["read", "write"] | None = None
    keys: Literal["read", "write"] | None = None
    members: Literal["read", "write"] | None = None
    merge_queues: Literal["read", "write"] | None = None
    metadata: Literal["read", "write"] | None = None
    models: Literal["read", "write"] | None = None
    organization_administration: Literal["read", "write"] | None = None
    organization_hooks: Literal["read", "write"] | None = None
    organization_packages: Literal["read", "write"] | None = None
    organization_plan: Literal["read", "write"] | None = None
    organization_projects: Literal["read", "write", "admin"] | None = None
    organization_secrets: Literal["read", "write"] | None = None
    organization_self_hosted_runners: Literal["read", "write"] | None = None
    organization_user_blocking: Literal["read", "write"] | None = None
    packages: Literal["read", "write"] | None = None
    pages: Literal["read", "write"] | None = None
    pull_requests: Literal["read", "write"] | None = None
    repository_hooks: Literal["read", "write"] | None = None
    repository_projects: Literal["read", "write", "admin"] | None = None
    secret_scanning_alerts: Literal["read", "write"] | None = None
    secrets: Literal["read", "write"] | None = None
    security_events: Literal["read", "write"] | None = None
    security_scanning_alert: Literal["read", "write"] | None = None
    single_file: Literal["read", "write"] | None = None
    statuses: Literal["read", "write"] | None = None
    team_discussions: Literal["read", "write"] | None = None
    vulnerability_alerts: Literal["read", "write"] | None = None
    workflows: Literal["read", "write"] | None = None


class CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CheckSuiteRerequestedPayloadCheckSuiteAppPermissions(BaseModel):
    """The set of permissions for the GitHub app."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actions: Literal["read", "write"] | None = None
    administration: Literal["read", "write"] | None = None
    artifact_metadata: Literal["read", "write"] | None = None
    attestations: Literal["read", "write"] | None = None
    checks: Literal["read", "write"] | None = None
    content_references: Literal["read", "write"] | None = None
    contents: Literal["read", "write"] | None = None
    copilot_requests: Literal["write"] | None = None
    deployments: Literal["read", "write"] | None = None
    discussions: Literal["read", "write"] | None = None
    emails: Literal["read", "write"] | None = None
    environments: Literal["read", "write"] | None = None
    issues: Literal["read", "write"] | None = None
    keys: Literal["read", "write"] | None = None
    members: Literal["read", "write"] | None = None
    merge_queues: Literal["read", "write"] | None = None
    metadata: Literal["read", "write"] | None = None
    models: Literal["read", "write"] | None = None
    organization_administration: Literal["read", "write"] | None = None
    organization_hooks: Literal["read", "write"] | None = None
    organization_packages: Literal["read", "write"] | None = None
    organization_plan: Literal["read", "write"] | None = None
    organization_projects: Literal["read", "write", "admin"] | None = None
    organization_secrets: Literal["read", "write"] | None = None
    organization_self_hosted_runners: Literal["read", "write"] | None = None
    organization_user_blocking: Literal["read", "write"] | None = None
    packages: Literal["read", "write"] | None = None
    pages: Literal["read", "write"] | None = None
    pull_requests: Literal["read", "write"] | None = None
    repository_hooks: Literal["read", "write"] | None = None
    repository_projects: Literal["read", "write", "admin"] | None = None
    secret_scanning_alerts: Literal["read", "write"] | None = None
    secrets: Literal["read", "write"] | None = None
    security_events: Literal["read", "write"] | None = None
    security_scanning_alert: Literal["read", "write"] | None = None
    single_file: Literal["read", "write"] | None = None
    statuses: Literal["read", "write"] | None = None
    team_discussions: Literal["read", "write"] | None = None
    vulnerability_alerts: Literal["read", "write"] | None = None
    workflows: Literal["read", "write"] | None = None


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class CodeScanningAlertAppearedInBranchPayloadAlertRule(BaseModel):
    """CodeScanningAlertAppearedInBranchPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    id: str
    severity: Literal["none", "note", "warning", "error"] | None


class CodeScanningAlertAppearedInBranchPayloadAlertTool(BaseModel):
    """CodeScanningAlertAppearedInBranchPayloadAlertTool."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    version: None | str


class CodeScanningAlertClosedByUserPayloadAlertRule(BaseModel):
    """CodeScanningAlertClosedByUserPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    full_description: str | None = None
    help: None | str = None
    help_uri: None | str = None
    id: str
    name: str | None = None
    severity: Literal["none", "note", "warning", "error"] | None
    tags: Any | None = None


class CodeScanningAlertClosedByUserPayloadAlertTool(BaseModel):
    """CodeScanningAlertClosedByUserPayloadAlertTool."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    guid: None | str = None
    name: str
    version: None | str


class CodeScanningAlertCreatedPayloadAlertRule(BaseModel):
    """CodeScanningAlertCreatedPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    full_description: str | None = None
    help: None | str = None
    help_uri: None | str = None
    id: str
    name: str | None = None
    severity: Literal["none", "note", "warning", "error"] | None
    tags: Any | None = None


class CodeScanningAlertFixedPayloadAlertRule(BaseModel):
    """CodeScanningAlertFixedPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    full_description: str | None = None
    help: None | str = None
    help_uri: None | str = None
    id: str
    name: str | None = None
    severity: Literal["none", "note", "warning", "error"] | None
    tags: Any | None = None


class CodeScanningAlertFixedPayloadAlertTool(BaseModel):
    """CodeScanningAlertFixedPayloadAlertTool."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    guid: None | str = None
    name: str
    version: None | str


class CodeScanningAlertReopenedByUserPayloadAlertRule(BaseModel):
    """CodeScanningAlertReopenedByUserPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    id: str
    severity: Literal["none", "note", "warning", "error"] | None


class CodeScanningAlertReopenedByUserPayloadAlertTool(BaseModel):
    """CodeScanningAlertReopenedByUserPayloadAlertTool."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    version: None | str


class CodeScanningAlertReopenedPayloadAlertRule(BaseModel):
    """CodeScanningAlertReopenedPayloadAlertRule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str
    full_description: str | None = None
    help: None | str = None
    help_uri: None | str = None
    id: str
    name: str | None = None
    severity: Literal["none", "note", "warning", "error"] | None
    tags: Any | None = None


class CodeScanningAlertReopenedPayloadAlertTool(BaseModel):
    """CodeScanningAlertReopenedPayloadAlertTool."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    guid: None | str = None
    name: str
    version: None | str


class CommitCommentCreatedPayloadCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class CustomPropertyDeletedPayloadDefinition(BaseModel):
    """CustomPropertyDeletedPayloadDefinition."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    property_name: str


class DependabotAlertSecurityAdvisoryCvss(BaseModel):
    """Details for the advisory pertaining to the Common Vulnerability Scoring System."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    score: float
    vector_string: None | str


class DependabotAlertSecurityAdvisoryCwe(BaseModel):
    """A CWE weakness assigned to the advisory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cwe_id: str
    name: str


class DependabotAlertSecurityAdvisoryIdentifier(BaseModel):
    """An advisory identifier."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["CVE", "GHSA"]
    value: str


class DependabotAlertSecurityAdvisoryReference(BaseModel):
    """A link to additional advisory information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str


class DeploymentCreatedPayloadDeployment(BaseModel):
    """The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    creator: Any | None
    description: None | str
    environment: str
    id: int
    node_id: str
    original_environment: str
    payload: dict[str, Any] | str
    performed_via_github_app: Any | None = None
    production_environment: bool | None = None
    ref: str
    repository_url: str
    sha: str
    statuses_url: str
    task: str
    transient_environment: bool | None = None
    updated_at: str
    url: str


class DeploymentReviewApprovedPayloadReviewer(BaseModel):
    """DeploymentReviewApprovedPayloadReviewer."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reviewer: Any | None = None
    type: Literal["User"] | None = None


class DeploymentReviewApprovedPayloadWorkflowJobRun(BaseModel):
    """DeploymentReviewApprovedPayloadWorkflowJobRun."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conclusion: None = None
    created_at: str | None = None
    environment: str | None = None
    html_url: str | None = None
    id: int | None = None
    name: None | str = None
    status: str | None = None
    updated_at: str | None = None


class DeploymentReviewRejectedPayloadReviewer(BaseModel):
    """DeploymentReviewRejectedPayloadReviewer."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reviewer: Any | None = None
    type: Literal["User"] | None = None


class DeploymentReviewRejectedPayloadWorkflowJobRun(BaseModel):
    """DeploymentReviewRejectedPayloadWorkflowJobRun."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conclusion: None | str = None
    created_at: str | None = None
    environment: str | None = None
    html_url: str | None = None
    id: int | None = None
    name: None | str = None
    status: str | None = None
    updated_at: str | None = None


class DeploymentReviewRequestedPayloadReviewer(BaseModel):
    """DeploymentReviewRequestedPayloadReviewer."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reviewer: Any | None = None
    type: Literal["User", "Team"] | None = None


class DeploymentReviewRequestedPayloadWorkflowJobRun(BaseModel):
    """DeploymentReviewRequestedPayloadWorkflowJobRun."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conclusion: None
    created_at: str
    environment: str
    html_url: str
    id: int
    name: None | str
    status: str
    updated_at: str


class DeploymentStatusCreatedPayloadDeployment(BaseModel):
    """The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    creator: Any | None
    description: None | str
    environment: str
    id: int
    node_id: str
    original_environment: str
    payload: dict[str, Any] | str
    performed_via_github_app: Any | None = None
    production_environment: bool | None = None
    ref: str
    repository_url: str
    sha: str
    statuses_url: str
    task: str
    transient_environment: bool | None = None
    updated_at: str
    url: str


class DeploymentStatusCreatedPayloadDeploymentStatus(BaseModel):
    """The [deployment status](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    creator: Any | None
    deployment_url: str
    description: str
    environment: str
    environment_url: str | None = None
    id: int
    log_url: str | None = None
    node_id: str
    performed_via_github_app: Any | None = None
    repository_url: str
    state: str
    target_url: str
    updated_at: str
    url: str


class DiscussionCategory(BaseModel):
    """DiscussionCategory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: str | None = None
    repository_id: int
    slug: str
    updated_at: str


class DiscussionReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class DiscussionCategoryChangedPayloadChangesCategoryFrom(BaseModel):
    """DiscussionCategoryChangedPayloadChangesCategoryFrom."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: str | None = None
    repository_id: int
    slug: str
    updated_at: str


class DiscussionCommentEditedPayloadChangesBody(BaseModel):
    """DiscussionCommentEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class DiscussionEditedPayloadChangesBody(BaseModel):
    """DiscussionEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class DiscussionEditedPayloadChangesTitle(BaseModel):
    """DiscussionEditedPayloadChangesTitle."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class FullRepositoryPermissions(BaseModel):
    """FullRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    push: bool
    triage: bool | None = None
    pull: bool


class GollumPayloadPage(BaseModel):
    """GollumPayloadPage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created", "edited"]
    html_url: str
    page_name: str
    sha: str
    summary: None | str
    title: str


class InstallationCreatedPayloadRepository(BaseModel):
    """InstallationCreatedPayloadRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationDeletedPayloadRepository(BaseModel):
    """InstallationDeletedPayloadRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationNewPermissionsAcceptedPayloadRepository(BaseModel):
    """InstallationNewPermissionsAcceptedPayloadRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationRepositoriesAddedPayloadRepositoriesAdded(BaseModel):
    """InstallationRepositoriesAddedPayloadRepositoriesAdded."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationRepositoriesAddedPayloadRepositoriesRemoved(BaseModel):
    """InstallationRepositoriesAddedPayloadRepositoriesRemoved."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str | None = None
    id: int | None = None
    name: str | None = None
    node_id: str | None = None
    private: bool | None = None


class InstallationRepositoriesRemovedPayloadRepositoriesAdded(BaseModel):
    """InstallationRepositoriesRemovedPayloadRepositoriesAdded."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationRepositoriesRemovedPayloadRepositoriesRemoved(BaseModel):
    """InstallationRepositoriesRemovedPayloadRepositoriesRemoved."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationSuspendPayloadRepository(BaseModel):
    """InstallationSuspendPayloadRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class InstallationTargetRenamedPayloadAccount(BaseModel):
    """InstallationTargetRenamedPayloadAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived_at: None | str = None
    avatar_url: str
    created_at: str | None = None
    description: None = None
    events_url: str | None = None
    followers: int | None = None
    followers_url: str | None = None
    following: int | None = None
    following_url: str | None = None
    gists_url: str | None = None
    gravatar_id: str | None = None
    has_organization_projects: bool | None = None
    has_repository_projects: bool | None = None
    hooks_url: str | None = None
    html_url: str
    id: int
    is_verified: bool | None = None
    issues_url: str | None = None
    login: str | None = None
    members_url: str | None = None
    name: str | None = None
    node_id: str
    organizations_url: str | None = None
    public_gists: int | None = None
    public_members_url: str | None = None
    public_repos: int | None = None
    received_events_url: str | None = None
    repos_url: str | None = None
    site_admin: bool | None = None
    slug: str | None = None
    starred_url: str | None = None
    subscriptions_url: str | None = None
    type: str | None = None
    updated_at: str | None = None
    url: str | None = None
    website_url: None = None
    user_view_type: str | None = None


class InstallationTargetRenamedPayloadChangesLogin(BaseModel):
    """InstallationTargetRenamedPayloadChangesLogin."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class InstallationTargetRenamedPayloadChangesSlug(BaseModel):
    """InstallationTargetRenamedPayloadChangesSlug."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class InstallationUnsuspendPayloadRepository(BaseModel):
    """InstallationUnsuspendPayloadRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class IssueLabelOption2(BaseModel):
    """IssueLabelOption2."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = None
    node_id: str | None = None
    url: str | None = None
    name: str | None = None
    description: None | str = None
    color: None | str = None
    default: bool | None = None


class IssuePullRequest(BaseModel):
    """IssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    merged_at: None | str = None
    diff_url: None | str
    html_url: None | str
    patch_url: None | str
    url: None | str


class IssueCommentCreatedPayloadCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesDeletedPayloadIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class IssuesDeletedPayloadIssuePullRequest(BaseModel):
    """IssuesDeletedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesDeletedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesDemilestonedPayloadIssuePullRequest(BaseModel):
    """IssuesDemilestonedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesDemilestonedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesEditedPayloadChangesBody(BaseModel):
    """IssuesEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class IssuesEditedPayloadChangesTitle(BaseModel):
    """IssuesEditedPayloadChangesTitle."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class IssuesEditedPayloadIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class IssuesEditedPayloadIssuePullRequest(BaseModel):
    """IssuesEditedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesEditedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesLabeledPayloadIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class IssuesLabeledPayloadIssuePullRequest(BaseModel):
    """IssuesLabeledPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesLabeledPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesLockedPayloadIssuePullRequest(BaseModel):
    """IssuesLockedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesLockedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesMilestonedPayloadIssuePullRequest(BaseModel):
    """IssuesMilestonedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesMilestonedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesOpenedPayloadChangesOldRepositoryPermissions(BaseModel):
    """IssuesOpenedPayloadChangesOldRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class IssuesOpenedPayloadIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class IssuesOpenedPayloadIssuePullRequest(BaseModel):
    """IssuesOpenedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesOpenedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesReopenedPayloadIssuePullRequest(BaseModel):
    """IssuesReopenedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesReopenedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesTransferredPayloadChangesNewIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class IssuesTransferredPayloadChangesNewIssuePullRequest(BaseModel):
    """IssuesTransferredPayloadChangesNewIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesTransferredPayloadChangesNewIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class IssuesTransferredPayloadChangesNewRepositoryPermissions(BaseModel):
    """IssuesTransferredPayloadChangesNewRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class IssuesUnlockedPayloadIssuePullRequest(BaseModel):
    """IssuesUnlockedPayloadIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class IssuesUnlockedPayloadIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class LabelEditedPayloadChangesColor(BaseModel):
    """LabelEditedPayloadChangesColor."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class LabelEditedPayloadChangesDescription(BaseModel):
    """LabelEditedPayloadChangesDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class LabelEditedPayloadChangesName(BaseModel):
    """LabelEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccount(BaseModel):
    """MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    login: str
    node_id: str
    organization_billing_email: None | str
    type: str


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlan(BaseModel):
    """MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlan."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bullets: list[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: None | str
    yearly_price_in_cents: int


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccount(BaseModel):
    """MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    login: str
    node_id: str
    organization_billing_email: None | str
    type: str


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlan(BaseModel):
    """MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlan."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bullets: list[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: None | str
    yearly_price_in_cents: int


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccount(BaseModel):
    """MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    login: str
    node_id: str
    organization_billing_email: None | str
    type: str


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlan(BaseModel):
    """MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlan."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bullets: list[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: None | str
    yearly_price_in_cents: int


class MemberAddedPayloadChangesPermission(BaseModel):
    """This field is included for legacy purposes; use the `role_name` field instead. The `maintain` role is mapped to `write` and the `triage` role is mapped to `read`. To determine the role assigned to the collaborator, use the `role_name` field instead, which will provide the full role name, including custom roles."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: Literal["write", "admin", "read"]


class MemberAddedPayloadChangesRoleName(BaseModel):
    """The role assigned to the collaborator."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: str


class MemberEditedPayloadChangesOldPermission(BaseModel):
    """MemberEditedPayloadChangesOldPermission."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class MemberEditedPayloadChangesPermission(BaseModel):
    """MemberEditedPayloadChangesPermission."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class MetaDeletedPayloadHookConfig(BaseModel):
    """MetaDeletedPayloadHookConfig."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_type: Literal["json", "form"]
    insecure_ssl: str
    secret: str | None = None
    url: str


class MilestoneClosedPayloadMilestone(BaseModel):
    """A collection of related issues and pull requests."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: str
    closed_issues: int
    created_at: str
    creator: Any | None
    description: None | str
    due_on: None | str
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["closed"]
    title: str
    updated_at: str
    url: str


class MilestoneCreatedPayloadMilestone(BaseModel):
    """A collection of related issues and pull requests."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: None
    closed_issues: int
    created_at: str
    creator: Any | None
    description: None | str
    due_on: None | str
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open"]
    title: str
    updated_at: str
    url: str


class MilestoneEditedPayloadChangesDescription(BaseModel):
    """MilestoneEditedPayloadChangesDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class MilestoneEditedPayloadChangesDueOn(BaseModel):
    """MilestoneEditedPayloadChangesDueOn."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class MilestoneEditedPayloadChangesTitle(BaseModel):
    """MilestoneEditedPayloadChangesTitle."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class MilestoneOpenedPayloadMilestone(BaseModel):
    """A collection of related issues and pull requests."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: None
    closed_issues: int
    created_at: str
    creator: Any | None
    description: None | str
    due_on: None | str
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open"]
    title: str
    updated_at: str
    url: str


class MinimalRepositoryPermissions(BaseModel):
    """MinimalRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool | None = None
    maintain: bool | None = None
    push: bool | None = None
    triage: bool | None = None
    pull: bool | None = None


class OrganizationMemberInvitedPayloadInvitation(BaseModel):
    """The invitation for the user or email if the action is `member_invited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    email: None | str
    failed_at: None | str
    failed_reason: None | str
    id: float
    invitation_teams_url: str
    inviter: Any | None
    login: None | str
    node_id: str
    role: str
    team_count: float
    invitation_source: str | None = None


class OrganizationRenamedPayloadChangesLogin(BaseModel):
    """OrganizationRenamedPayloadChangesLogin."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class PackagePublishedPayloadPackage(BaseModel):
    """Information about the package."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    description: None | str
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Any | None
    package_type: str
    package_version: Any | None
    registry: Any | None
    updated_at: None | str


class PackageUpdatedPayloadPackagePackageVersionDockerMetadata(BaseModel):
    """PackageUpdatedPayloadPackagePackageVersionDockerMetadata."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tags: list[str] | None = None


class PackageUpdatedPayloadPackagePackageVersionPackageFile(BaseModel):
    """PackageUpdatedPayloadPackagePackageVersionPackageFile."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_type: str
    created_at: str
    download_url: str
    id: int
    md5: None | str
    name: str
    sha1: None | str
    sha256: str
    size: int
    state: str
    updated_at: str


class PackageUpdatedPayloadPackagePackageVersionRelease(BaseModel):
    """PackageUpdatedPayloadPackagePackageVersionRelease."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: Any | None
    created_at: str
    draft: bool
    html_url: str
    id: int
    name: str
    prerelease: bool
    published_at: str
    tag_name: str
    target_commitish: str
    url: str


class PageBuildPayloadBuildError(BaseModel):
    """PageBuildPayloadBuildError."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: None | str


class PersonalAccessTokenRequestPermissionsAdded(BaseModel):
    """New requested permissions, categorized by type of permission."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    organization: dict[str, Any] | None = None
    repository: dict[str, Any] | None = None
    other: dict[str, Any] | None = None


class PersonalAccessTokenRequestPermissionsResult(BaseModel):
    """Permissions requested, categorized by type of permission. This field incorporates `permissions_added` and `permissions_upgraded`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    organization: dict[str, Any] | None = None
    repository: dict[str, Any] | None = None
    other: dict[str, Any] | None = None


class PersonalAccessTokenRequestPermissionsUpgraded(BaseModel):
    """Requested permissions that elevate access for a previously approved request for access, categorized by type of permission."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    organization: dict[str, Any] | None = None
    repository: dict[str, Any] | None = None
    other: dict[str, Any] | None = None


class PingPayloadHookConfig(BaseModel):
    """PingPayloadHookConfig."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_type: str | None = None
    insecure_ssl: float | str | None = None
    secret: str | None = None
    url: str | None = None


class ProjectCardConvertedPayloadChangesNote(BaseModel):
    """ProjectCardConvertedPayloadChangesNote."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ProjectCardDeletedPayloadProjectCard(BaseModel):
    """Project Card."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after_id: None | int = None
    archived: bool
    column_id: None | int
    column_url: str
    content_url: str | None = None
    created_at: str
    creator: Any | None
    id: int
    node_id: str
    note: None | str
    project_url: str
    updated_at: str
    url: str


class ProjectCardEditedPayloadChangesNote(BaseModel):
    """ProjectCardEditedPayloadChangesNote."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(alias="from")


class ProjectCardMovedPayloadChangesColumnId(BaseModel):
    """ProjectCardMovedPayloadChangesColumnId."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: int = Field(alias="from")


class ProjectColumnEditedPayloadChangesName(BaseModel):
    """ProjectColumnEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ProjectEditedPayloadChangesBody(BaseModel):
    """ProjectEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ProjectEditedPayloadChangesName(BaseModel):
    """ProjectEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ProjectsV2EditedPayloadChangesDescription(BaseModel):
    """ProjectsV2EditedPayloadChangesDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2EditedPayloadChangesPublic(BaseModel):
    """ProjectsV2EditedPayloadChangesPublic."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: bool | None = Field(default=None, alias="from")
    to: bool | None = None


class ProjectsV2EditedPayloadChangesShortDescription(BaseModel):
    """ProjectsV2EditedPayloadChangesShortDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2EditedPayloadChangesTitle(BaseModel):
    """ProjectsV2EditedPayloadChangesTitle."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")
    to: str | None = None


class ProjectsV2ItemConvertedPayloadChangesContentType(BaseModel):
    """ProjectsV2ItemConvertedPayloadChangesContentType."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: str | None = None


class ProjectsV2ItemEditedPayloadChangesOption2Body(BaseModel):
    """ProjectsV2ItemEditedPayloadChangesOption2Body."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeId(BaseModel):
    """ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeId."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2StatusUpdateEditedPayloadChangesBody(BaseModel):
    """ProjectsV2StatusUpdateEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2StatusUpdateEditedPayloadChangesStartDate(BaseModel):
    """ProjectsV2StatusUpdateEditedPayloadChangesStartDate."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class ProjectsV2StatusUpdateEditedPayloadChangesStatus(BaseModel):
    """ProjectsV2StatusUpdateEditedPayloadChangesStatus."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None = Field(
        default=None, alias="from"
    )
    to: Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None = None


class ProjectsV2StatusUpdateEditedPayloadChangesTargetDate(BaseModel):
    """ProjectsV2StatusUpdateEditedPayloadChangesTargetDate."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class PullRequestLabel(BaseModel):
    """PullRequestLabel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    url: str
    name: str
    description: None | str
    color: str
    default: bool


class PullRequestAssignedPayloadPullRequestHead(BaseModel):
    """PullRequestAssignedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestAssignedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestAssignedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestAssignedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestAssignedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestAssignedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestAssignedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAssignedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestAutoMergeDisabledPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeDisabledPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestAutoMergeEnabledPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestAutoMergeEnabledPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestDequeuedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestDequeuedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestDequeuedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestDequeuedPayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestDequeuedPayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestDequeuedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestDequeuedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEditedPayloadChangesBody(BaseModel):
    """PullRequestEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class PullRequestEditedPayloadChangesTitle(BaseModel):
    """PullRequestEditedPayloadChangesTitle."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class PullRequestEditedPayloadChangesBaseRef(BaseModel):
    """PullRequestEditedPayloadChangesBaseRef."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class PullRequestEditedPayloadChangesBaseSha(BaseModel):
    """PullRequestEditedPayloadChangesBaseSha."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class PullRequestEnqueuedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestEnqueuedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestEnqueuedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestEnqueuedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestEnqueuedPayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestEnqueuedPayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestEnqueuedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestEnqueuedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestHead(BaseModel):
    """PullRequestLabeledPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestLabeledPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestLabeledPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestLabeledPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestLabeledPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestLabeledPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestLabeledPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLabeledPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestHead(BaseModel):
    """PullRequestLockedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestLockedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestLockedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestLockedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestLockedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestLockedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestLockedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestLockedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestMinimalBaseRepo(BaseModel):
    """PullRequestMinimalBaseRepo."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    url: str
    name: str


class PullRequestMinimalHeadRepo(BaseModel):
    """PullRequestMinimalHeadRepo."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    url: str
    name: str


class PullRequestReviewCommentCreatedPayloadCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class PullRequestReviewCommentCreatedPayloadCommentLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadCommentLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadCommentLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewCommentCreatedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewCommentCreatedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewCommentCreatedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentCreatedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewCommentDeletedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewCommentDeletedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewCommentDeletedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentDeletedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewCommentEditedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewCommentEditedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewCommentEditedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewCommentEditedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewCommentEditedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewDismissedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewDismissedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestReviewDismissedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewDismissedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadReviewLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewDismissedPayloadReviewLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadChangesBody(BaseModel):
    """PullRequestReviewEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class PullRequestReviewEditedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewEditedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewEditedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestReviewEditedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewEditedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewEditedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewEditedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewEditedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewSubmittedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewSubmittedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestReviewSubmittedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewSubmittedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewSubmittedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewThreadResolvedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestReviewThreadResolvedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewThreadResolvedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadThreadCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadThreadCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestSynchronizePayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestSynchronizePayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestSynchronizePayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestSynchronizePayloadPullRequestHeadRepoPermissions(BaseModel):
    """PullRequestSynchronizePayloadPullRequestHeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestSynchronizePayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestSynchronizePayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestHead(BaseModel):
    """PullRequestUnassignedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestUnassignedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestUnassignedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestUnassignedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestUnassignedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestUnassignedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnassignedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestHead(BaseModel):
    """PullRequestUnlabeledPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestUnlabeledPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: Any | None = None
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class PullRequestUnlabeledPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestUnlabeledPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestUnlabeledPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestUnlabeledPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlabeledPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestHead(BaseModel):
    """PullRequestUnlockedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Any | None
    sha: str
    user: Any | None


class PullRequestUnlockedPayloadPullRequestLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestUnlockedPayloadPullRequestRequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class PullRequestUnlockedPayloadPullRequestBaseRepoPermissions(BaseModel):
    """PullRequestUnlockedPayloadPullRequestBaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class PullRequestUnlockedPayloadPullRequestLinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PullRequestUnlockedPayloadPullRequestLinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class PushPayloadPusher(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str = None
    name: str
    username: str | None = None


class PushPayloadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class PushPayloadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class PushPayloadRepositoryPermissions(BaseModel):
    """PushPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class RegistryPackagePublishedPayloadRegistryPackageOwner(BaseModel):
    """RegistryPackagePublishedPayloadRegistryPackageOwner."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: str | None = None


class RegistryPackageUpdatedPayloadRegistryPackageOwner(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackageOwner."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: str | None = None


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthor(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthor."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: str | None = None


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFile(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFile."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_type: str | None = None
    created_at: str | None = None
    download_url: str | None = None
    id: int | None = None
    md5: None | str = None
    name: str | None = None
    sha1: None | str = None
    sha256: str | None = None
    size: int | None = None
    state: str | None = None
    updated_at: str | None = None


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthor(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthor."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: str | None = None


class ReleaseEditedPayloadChangesBody(BaseModel):
    """ReleaseEditedPayloadChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ReleaseEditedPayloadChangesMakeLatest(BaseModel):
    """ReleaseEditedPayloadChangesMakeLatest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: bool


class ReleaseEditedPayloadChangesName(BaseModel):
    """ReleaseEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ReleaseEditedPayloadChangesTagName(BaseModel):
    """ReleaseEditedPayloadChangesTagName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class ReleasePrereleasedPayloadReleaseReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class Repository2CodeSearchIndexStatus(BaseModel):
    """The status of the code search index for this repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    lexical_search_ok: bool | None = None
    lexical_commit_sha: str | None = None


class Repository2Permissions(BaseModel):
    """Repository2Permissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    pull: bool
    triage: bool | None = None
    push: bool
    maintain: bool | None = None


class RepositoryPermissions(BaseModel):
    """RepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    pull: bool
    triage: bool | None = None
    push: bool
    maintain: bool | None = None


class RepositoryAdvisoryIdentifier(BaseModel):
    """RepositoryAdvisoryIdentifier."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["CVE", "GHSA"]
    value: str


class RepositoryEditedPayloadChangesDefaultBranch(BaseModel):
    """RepositoryEditedPayloadChangesDefaultBranch."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class RepositoryEditedPayloadChangesDescription(BaseModel):
    """RepositoryEditedPayloadChangesDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(alias="from")


class RepositoryEditedPayloadChangesHomepage(BaseModel):
    """RepositoryEditedPayloadChangesHomepage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(alias="from")


class RepositoryEditedPayloadChangesTopics(BaseModel):
    """RepositoryEditedPayloadChangesTopics."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Any | None = Field(default=None, alias="from")


class RepositoryRenamedPayloadChangesRepositoryName(BaseModel):
    """RepositoryRenamedPayloadChangesRepositoryName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class RepositoryRuleBranchNamePatternParameters(BaseModel):
    """RepositoryRuleBranchNamePatternParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    negate: bool | None = None
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


class RepositoryRuleCommitAuthorEmailPatternParameters(BaseModel):
    """RepositoryRuleCommitAuthorEmailPatternParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    negate: bool | None = None
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


class RepositoryRuleCommitMessagePatternParameters(BaseModel):
    """RepositoryRuleCommitMessagePatternParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    negate: bool | None = None
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


class RepositoryRuleCommitterEmailPatternParameters(BaseModel):
    """RepositoryRuleCommitterEmailPatternParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    negate: bool | None = None
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


class RepositoryRuleCopilotCodeReviewParameters(BaseModel):
    """RepositoryRuleCopilotCodeReviewParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    review_draft_pull_requests: bool | None = None
    review_on_push: bool | None = None


class RepositoryRuleFileExtensionRestrictionParameters(BaseModel):
    """RepositoryRuleFileExtensionRestrictionParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    restricted_file_extensions: list[str]


class RepositoryRuleFilePathRestrictionParameters(BaseModel):
    """RepositoryRuleFilePathRestrictionParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    restricted_file_paths: list[str]


class RepositoryRuleMaxFilePathLengthParameters(BaseModel):
    """RepositoryRuleMaxFilePathLengthParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    max_file_path_length: int


class RepositoryRuleMaxFileSizeParameters(BaseModel):
    """RepositoryRuleMaxFileSizeParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    max_file_size: int


class RepositoryRuleMergeQueueParameters(BaseModel):
    """RepositoryRuleMergeQueueParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    check_response_timeout_minutes: int
    grouping_strategy: Literal["ALLGREEN", "HEADGREEN"]
    max_entries_to_build: int
    max_entries_to_merge: int
    merge_method: Literal["MERGE", "SQUASH", "REBASE"]
    min_entries_to_merge: int
    min_entries_to_merge_wait_minutes: int


class RepositoryRuleRequiredDeploymentsParameters(BaseModel):
    """RepositoryRuleRequiredDeploymentsParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    required_deployment_environments: list[str]


class RepositoryRuleTagNamePatternParameters(BaseModel):
    """RepositoryRuleTagNamePatternParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    negate: bool | None = None
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


class RepositoryRuleUpdateParameters(BaseModel):
    """RepositoryRuleUpdateParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    update_allows_fetch_and_merge: bool


class RepositoryRulesetConditionsRefName(BaseModel):
    """RepositoryRulesetConditionsRefName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    include: list[str] | None = None
    exclude: list[str] | None = None


class RepositoryRulesetEditedPayloadChangesEnforcement(BaseModel):
    """RepositoryRulesetEditedPayloadChangesEnforcement."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesName(BaseModel):
    """RepositoryRulesetEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionType(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionType."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExclude(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExclude."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: list[str] | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesInclude(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesInclude."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: list[str] | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTarget(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTarget."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfiguration(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfiguration."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPattern(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPattern."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleType(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleType."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")


class RepositoryRulesetLinksSelf(BaseModel):
    """RepositoryRulesetLinksSelf."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = None


class RepositoryTransferredPayloadChangesOwnerFromOrganization(BaseModel):
    """Organization."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str
    description: None | str
    events_url: str
    hooks_url: str
    html_url: str | None = None
    id: int
    issues_url: str
    login: str
    members_url: str
    node_id: str
    public_members_url: str
    repos_url: str
    url: str


class RepositoryVulnerabilityAlertDismissPayloadAlert(BaseModel):
    """The security alert of the vulnerable dependency."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_comment: None | str = None
    dismiss_reason: str
    dismissed_at: str
    dismisser: Any | None
    external_identifier: str
    external_reference: None | str
    fix_reason: str | None = None
    fixed_at: str | None = None
    fixed_in: str | None = None
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["dismissed"]


class RepositoryVulnerabilityAlertResolvePayloadAlert(BaseModel):
    """The security alert of the vulnerable dependency."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_reason: str | None = None
    dismissed_at: str | None = None
    dismisser: Any | None = None
    external_identifier: str
    external_reference: None | str
    fix_reason: str | None = None
    fixed_at: str | None = None
    fixed_in: str | None = None
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["fixed", "open"]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvss(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvss."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    score: float
    vector_string: None | str


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCwe(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCwe."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cwe_id: str
    name: str


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifier(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifier."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: str
    value: str


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReference(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReference."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackage(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecosystem: str
    name: str


class SecurityAndAnalysisPayloadChangesFrom(BaseModel):
    """SecurityAndAnalysisPayloadChangesFrom."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    security_and_analysis: Any | None = None


class SponsorshipEditedPayloadChangesPrivacyLevel(BaseModel):
    """SponsorshipEditedPayloadChangesPrivacyLevel."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class StatusPayloadBrancheCommit(BaseModel):
    """StatusPayloadBrancheCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sha: None | str
    url: None | str


class StatusPayloadCommitParent(BaseModel):
    """StatusPayloadCommitParent."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html_url: str
    sha: str
    url: str


class StatusPayloadCommitCommitTree(BaseModel):
    """StatusPayloadCommitCommitTree."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sha: str
    url: str


class StatusPayloadCommitCommitVerification(BaseModel):
    """StatusPayloadCommitCommitVerification."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: None | str
    reason: Literal[
        "expired_key",
        "not_signing_key",
        "gpgverify_error",
        "gpgverify_unavailable",
        "unsigned",
        "unknown_signature_type",
        "no_user",
        "unverified_email",
        "bad_email",
        "unknown_key",
        "malformed_signature",
        "invalid",
        "valid",
        "bad_cert",
        "ocsp_pending",
    ]
    signature: None | str
    verified: bool
    verified_at: None | str


class TeamAddedToRepositoryPayloadRepositoryPermissions(BaseModel):
    """TeamAddedToRepositoryPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class TeamCreatedPayloadRepositoryPermissions(BaseModel):
    """TeamCreatedPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class TeamDeletedPayloadRepositoryPermissions(BaseModel):
    """TeamDeletedPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class TeamEditedPayloadChangesDescription(BaseModel):
    """TeamEditedPayloadChangesDescription."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class TeamEditedPayloadChangesName(BaseModel):
    """TeamEditedPayloadChangesName."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class TeamEditedPayloadChangesNotificationSetting(BaseModel):
    """TeamEditedPayloadChangesNotificationSetting."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class TeamEditedPayloadChangesPrivacy(BaseModel):
    """TeamEditedPayloadChangesPrivacy."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class TeamEditedPayloadChangesRepositoryPermissionsFrom(BaseModel):
    """TeamEditedPayloadChangesRepositoryPermissionsFrom."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool | None = None
    pull: bool | None = None
    push: bool | None = None


class TeamEditedPayloadRepositoryPermissions(BaseModel):
    """TeamEditedPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class TeamRemovedFromRepositoryPayloadRepositoryPermissions(BaseModel):
    """TeamRemovedFromRepositoryPayloadRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class WebhookRubygemsMetadataVersionInfo(BaseModel):
    """WebhookRubygemsMetadataVersionInfo."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version: str | None = None


class WebhooksAnswerReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksChanges8TierFrom(BaseModel):
    """The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: str
    is_custom_ammount: bool | None = None
    is_custom_amount: bool | None = None
    is_one_time: bool
    monthly_price_in_cents: int
    monthly_price_in_dollars: int
    name: str
    node_id: str


class WebhooksChangesBody(BaseModel):
    """WebhooksChangesBody."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str = Field(alias="from")


class WebhooksCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksIssue2Label(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class WebhooksIssue2PullRequest(BaseModel):
    """WebhooksIssue2PullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class WebhooksIssue2Reactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksIssueLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class WebhooksIssuePullRequest(BaseModel):
    """WebhooksIssuePullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    diff_url: str | None = None
    html_url: str | None = None
    merged_at: None | str = None
    patch_url: str | None = None
    url: str | None = None


class WebhooksIssueReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksIssueCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksMarketplacePurchaseAccount(BaseModel):
    """WebhooksMarketplacePurchaseAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    login: str
    node_id: str
    organization_billing_email: None | str
    type: str


class WebhooksMarketplacePurchasePlan(BaseModel):
    """WebhooksMarketplacePurchasePlan."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bullets: list[None | str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: None | str
    yearly_price_in_cents: int


class WebhooksPreviousMarketplacePurchaseAccount(BaseModel):
    """WebhooksPreviousMarketplacePurchaseAccount."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    login: str
    node_id: str
    organization_billing_email: None | str
    type: str


class WebhooksPreviousMarketplacePurchasePlan(BaseModel):
    """WebhooksPreviousMarketplacePurchasePlan."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bullets: list[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: None | str
    yearly_price_in_cents: int


class WebhooksProjectChangesArchivedAt(BaseModel):
    """WebhooksProjectChangesArchivedAt."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: None | str = Field(default=None, alias="from")
    to: None | str = None


class WebhooksPullRequest5Label(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class WebhooksPullRequest5RequestedReviewerOption2(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class WebhooksPullRequest5RequestedTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None


class WebhooksPullRequest5BaseRepoPermissions(BaseModel):
    """WebhooksPullRequest5BaseRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class WebhooksPullRequest5HeadRepoPermissions(BaseModel):
    """WebhooksPullRequest5HeadRepoPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool
    maintain: bool | None = None
    pull: bool
    push: bool
    triage: bool | None = None


class WebhooksPullRequest5LinksComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksCommits(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksIssue(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksReviewComment(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksReviewComments(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksPullRequest5LinksStatuses(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksRelease1Reactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksReleaseAsset(BaseModel):
    """Data related to a release."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    browser_download_url: str
    content_type: str
    created_at: str
    download_count: int
    id: int
    label: None | str
    name: str
    node_id: str
    size: int
    digest: None | str
    state: Literal["uploaded"]
    updated_at: str
    uploader: Any | None = None
    url: str


class WebhooksReleaseReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksReviewCommentReactions(BaseModel):
    """Reactions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhooksReviewCommentLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksReviewCommentLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksReviewCommentLinksSelf(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksReviewLinksHtml(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksReviewLinksPullRequest(BaseModel):
    """Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class WebhooksSecurityAdvisoryCvss(BaseModel):
    """WebhooksSecurityAdvisoryCvss."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    score: float
    vector_string: None | str


class WebhooksSecurityAdvisoryCwe(BaseModel):
    """WebhooksSecurityAdvisoryCwe."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cwe_id: str
    name: str


class WebhooksSecurityAdvisoryIdentifier(BaseModel):
    """WebhooksSecurityAdvisoryIdentifier."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: str
    value: str


class WebhooksSecurityAdvisoryReference(BaseModel):
    """WebhooksSecurityAdvisoryReference."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str


class WebhooksSecurityAdvisoryVulnerabilityPackage(BaseModel):
    """WebhooksSecurityAdvisoryVulnerabilityPackage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecosystem: str
    name: str


class WebhooksSponsorshipMaintainer(BaseModel):
    """WebhooksSponsorshipMaintainer."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str | None = None
    events_url: str | None = None
    followers_url: str | None = None
    following_url: str | None = None
    gists_url: str | None = None
    gravatar_id: str | None = None
    html_url: str | None = None
    id: int | None = None
    login: str | None = None
    node_id: str | None = None
    organizations_url: str | None = None
    received_events_url: str | None = None
    repos_url: str | None = None
    site_admin: bool | None = None
    starred_url: str | None = None
    subscriptions_url: str | None = None
    type: str | None = None
    url: str | None = None
    user_view_type: str | None = None


class WebhooksSponsorshipTier(BaseModel):
    """The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: str
    is_custom_ammount: bool | None = None
    is_custom_amount: bool | None = None
    is_one_time: bool
    monthly_price_in_cents: int
    monthly_price_in_dollars: int
    name: str
    node_id: str


class WorkflowJobQueuedPayloadWorkflowJobStep(BaseModel):
    """Workflow Step."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    completed_at: None | str
    conclusion: Literal["failure", "skipped", "success", "cancelled"] | None
    name: str
    number: int
    started_at: None | str
    status: Literal["completed", "in_progress", "queued", "pending"]


class WorkflowJobWaitingPayloadWorkflowJobStep(BaseModel):
    """Workflow Step."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    completed_at: None | str
    conclusion: Literal["failure", "skipped", "success", "cancelled"] | None
    name: str
    number: int
    started_at: None | str
    status: Literal["completed", "in_progress", "queued", "pending", "waiting"]


class WorkflowRunCompletedPayloadWorkflowRunHeadRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunCompletedPayloadWorkflowRunRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunInProgressPayloadWorkflowRunHeadRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: None | str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunInProgressPayloadWorkflowRunRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunRequestedPayloadWorkflowRunHeadRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunRequestedPayloadWorkflowRunRepository(BaseModel):
    """Repository Lite."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: None | str
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Any | None
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthor(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitter(BaseModel):
    """Metaproperties for Git author/committer information."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: None | str
    name: str
    username: str | None = None


class WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepo(BaseModel):
    """Repo Ref."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    url: str


class AppPermissions(BaseModel):
    """The permissions granted to the user access token."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actions: Literal["read", "write"] | None = None
    administration: Literal["read", "write"] | None = None
    artifact_metadata: Literal["read", "write"] | None = None
    attestations: Literal["read", "write"] | None = None
    checks: Literal["read", "write"] | None = None
    codespaces: Literal["read", "write"] | None = None
    contents: Literal["read", "write"] | None = None
    dependabot_secrets: Literal["read", "write"] | None = None
    deployments: Literal["read", "write"] | None = None
    discussions: Literal["read", "write"] | None = None
    environments: Literal["read", "write"] | None = None
    issues: Literal["read", "write"] | None = None
    merge_queues: Literal["read", "write"] | None = None
    metadata: Literal["read", "write"] | None = None
    packages: Literal["read", "write"] | None = None
    pages: Literal["read", "write"] | None = None
    pull_requests: Literal["read", "write"] | None = None
    repository_custom_properties: Literal["read", "write"] | None = None
    repository_hooks: Literal["read", "write"] | None = None
    repository_projects: Literal["read", "write", "admin"] | None = None
    secret_scanning_alerts: Literal["read", "write"] | None = None
    secrets: Literal["read", "write"] | None = None
    security_events: Literal["read", "write"] | None = None
    single_file: Literal["read", "write"] | None = None
    statuses: Literal["read", "write"] | None = None
    vulnerability_alerts: Literal["read", "write"] | None = None
    workflows: Literal["write"] | None = None
    custom_properties_for_organizations: Literal["read", "write"] | None = None
    members: Literal["read", "write"] | None = None
    organization_administration: Literal["read", "write"] | None = None
    organization_custom_roles: Literal["read", "write"] | None = None
    organization_custom_org_roles: Literal["read", "write"] | None = None
    organization_custom_properties: Literal["read", "write", "admin"] | None = None
    organization_copilot_seat_management: Literal["write"] | None = None
    organization_announcement_banners: Literal["read", "write"] | None = None
    organization_events: Literal["read"] | None = None
    organization_hooks: Literal["read", "write"] | None = None
    organization_personal_access_tokens: Literal["read", "write"] | None = None
    organization_personal_access_token_requests: Literal["read", "write"] | None = None
    organization_plan: Literal["read"] | None = None
    organization_projects: Literal["read", "write", "admin"] | None = None
    organization_packages: Literal["read", "write"] | None = None
    organization_secrets: Literal["read", "write"] | None = None
    organization_self_hosted_runners: Literal["read", "write"] | None = None
    organization_user_blocking: Literal["read", "write"] | None = None
    team_discussions: Literal["read", "write"] | None = None
    email_addresses: Literal["read", "write"] | None = None
    followers: Literal["read", "write"] | None = None
    git_ssh_keys: Literal["read", "write"] | None = None
    gpg_keys: Literal["read", "write"] | None = None
    interaction_limits: Literal["read", "write"] | None = None
    profile: Literal["write"] | None = None
    starring: Literal["read", "write"] | None = None
    enterprise_custom_properties_for_organizations: Literal["read", "write", "admin"] | None = None


class CodeOfConduct(BaseModel):
    """Code Of Conduct."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str
    name: str
    url: str
    body: str | None = None
    html_url: None | str


class CodeOfConductSimple(BaseModel):
    """Code of Conduct Simple."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    key: str
    name: str
    html_url: None | str


class CustomProperty(BaseModel):
    """Custom property defined on an organization."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    property_name: str
    url: str | None = None
    source_type: Literal["organization", "enterprise"] | None = None
    value_type: Literal["string", "single_select", "multi_select", "true_false"]
    required: bool | None = None
    default_value: list[str] | str | None = None
    description: None | str = None
    allowed_values: Any | None = None
    values_editable_by: Literal["org_actors", "org_and_repo_actors"] | None = None


class CustomPropertyValue(BaseModel):
    """Custom property name and associated value."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    property_name: str
    value: list[str] | str


class DependabotAlertPackage(BaseModel):
    """Details for the vulnerable package."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecosystem: str
    name: str


class DeploymentSimple(BaseModel):
    """A deployment created as the result of an Actions check run from a workflow that references an environment."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    id: int
    node_id: str
    task: str
    original_environment: str | None = None
    environment: str
    description: None | str
    created_at: str
    updated_at: str
    statuses_url: str
    repository_url: str
    transient_environment: bool | None = None
    production_environment: bool | None = None
    performed_via_github_app: Any | None = None


class Enterprise2(BaseModel):
    """An enterprise on GitHub."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: None | str = None
    html_url: str
    website_url: None | str = None
    id: int
    node_id: str
    name: str
    slug: str
    created_at: None | str
    updated_at: None | str
    avatar_url: str


class Enterprise(BaseModel):
    """An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured on an enterprise account or an organization that's part of an enterprise account. For more information, see "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: None | str = None
    html_url: str
    website_url: None | str = None
    id: int
    node_id: str
    name: str
    slug: str
    created_at: None | str
    updated_at: None | str
    avatar_url: str


class HookResponse(BaseModel):
    """Hook Response."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: None | int
    status: None | str
    message: None | str


class IssueDependenciesSummary(BaseModel):
    """Issue Dependencies Summary."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blocked_by: int
    blocking: int
    total_blocked_by: int
    total_blocking: int


class IssueFieldValue(BaseModel):
    """A value assigned to an issue field."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_field_id: int
    node_id: str
    data_type: Literal["text", "single_select", "number", "date"]
    value: float | int | str
    single_select_option: Any | None = None


class Label(BaseModel):
    """Color-coded labels help you categorize and filter your issues (just like labels in Gmail)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    url: str
    name: str
    description: None | str
    color: str
    default: bool


class LicenseSimple(BaseModel):
    """License Simple."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str
    name: str
    url: None | str
    spdx_id: None | str
    node_id: str
    html_url: str | None = None


class Link(BaseModel):
    """Hypermedia Link."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str


class Organization(BaseModel):
    """A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an organization, or when the event occurs from activity in a repository owned by an organization."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: None | str


class ProjectsV2IterationSetting(BaseModel):
    """An iteration setting for an iteration field."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str
    title_html: str | None = None
    duration: None | float = None
    start_date: None | str = None
    completed: bool | None = None


class ProjectsV2SingleSelectOption(BaseModel):
    """An option for a single select field."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    color: None | str = None
    description: None | str = None


class ReactionRollup(BaseModel):
    """Reaction Rollup."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    total_count: int
    plus1: int = Field(alias="+1")
    minus1: int = Field(alias="-1")
    laugh: int
    confused: int
    heart: int
    hooray: int
    eyes: int
    rocket: int


class RepositoryRuleCreation(BaseModel):
    """Only allow users with bypass permission to create matching refs."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["creation"]


class RepositoryRuleDeletion(BaseModel):
    """Only allow users with bypass permissions to delete matching refs."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["deletion"]


class RepositoryRuleNonFastForward(BaseModel):
    """Prevent users with push access from force pushing to refs."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["non_fast_forward"]


class RepositoryRuleParamsCodeScanningTool(BaseModel):
    """A tool that must provide code scanning results for this rule to pass."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    alerts_threshold: Literal["none", "errors", "errors_and_warnings", "all"]
    security_alerts_threshold: Literal["none", "critical", "high_or_higher", "medium_or_higher", "all"]
    tool: str


class RepositoryRuleParamsReviewer(BaseModel):
    """A required reviewing team."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    type: Literal["Team"]


class RepositoryRuleParamsStatusCheckConfiguration(BaseModel):
    """Required status check."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    context: str
    integration_id: int | None = None


class RepositoryRuleParamsWorkflowFileReference(BaseModel):
    """A workflow that must run for this rule to pass."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    path: str
    ref: str | None = None
    repository_id: int
    sha: str | None = None


class RepositoryRuleRequiredLinearHistory(BaseModel):
    """Prevent merge commits from being pushed to matching refs."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["required_linear_history"]


class RepositoryRuleRequiredSignatures(BaseModel):
    """Commits pushed to matching refs must have verified signatures."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["required_signatures"]


class RepositoryRulesetBypassActor(BaseModel):
    """An actor that can bypass rules in a ruleset."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor_id: None | int = None
    actor_type: Literal["Integration", "OrganizationAdmin", "RepositoryRole", "Team", "DeployKey"]
    bypass_mode: Literal["always", "pull_request", "exempt"] | None = None


class SecretScanningLocationCommit(BaseModel):
    """Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    path: str
    start_line: float
    end_line: float
    start_column: float
    end_column: float
    blob_sha: str
    blob_url: str
    commit_sha: str
    commit_url: str


class SecretScanningLocationDiscussionBody(BaseModel):
    """Represents a 'discussion_body' secret scanning location type. This location type shows that a secret was detected in the body of a discussion."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discussion_body_url: str


class SecretScanningLocationDiscussionComment(BaseModel):
    """Represents a 'discussion_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a discussion."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discussion_comment_url: str


class SecretScanningLocationDiscussionTitle(BaseModel):
    """Represents a 'discussion_title' secret scanning location type. This location type shows that a secret was detected in the title of a discussion."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discussion_title_url: str


class SecretScanningLocationIssueBody(BaseModel):
    """Represents an 'issue_body' secret scanning location type. This location type shows that a secret was detected in the body of an issue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_body_url: str


class SecretScanningLocationIssueComment(BaseModel):
    """Represents an 'issue_comment' secret scanning location type. This location type shows that a secret was detected in a comment on an issue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_comment_url: str


class SecretScanningLocationIssueTitle(BaseModel):
    """Represents an 'issue_title' secret scanning location type. This location type shows that a secret was detected in the title of an issue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_title_url: str


class SecretScanningLocationPullRequestBody(BaseModel):
    """Represents a 'pull_request_body' secret scanning location type. This location type shows that a secret was detected in the body of a pull request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pull_request_body_url: str


class SecretScanningLocationPullRequestComment(BaseModel):
    """Represents a 'pull_request_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a pull request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pull_request_comment_url: str


class SecretScanningLocationPullRequestReview(BaseModel):
    """Represents a 'pull_request_review' secret scanning location type. This location type shows that a secret was detected in a review on a pull request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pull_request_review_url: str


class SecretScanningLocationPullRequestReviewComment(BaseModel):
    """Represents a 'pull_request_review_comment' secret scanning location type. This location type shows that a secret was detected in a review comment on a pull request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pull_request_review_comment_url: str


class SecretScanningLocationPullRequestTitle(BaseModel):
    """Represents a 'pull_request_title' secret scanning location type. This location type shows that a secret was detected in the title of a pull request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pull_request_title_url: str


class SecretScanningLocationWikiCommit(BaseModel):
    """Represents a 'wiki_commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository wiki."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    path: str
    start_line: float
    end_line: float
    start_column: float
    end_column: float
    blob_sha: str
    page_url: str
    commit_sha: str
    commit_url: str


class SimpleCommit(BaseModel):
    """A commit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    tree_id: str
    message: str
    timestamp: str
    author: Any | None
    committer: Any | None


class Installation(BaseModel):
    """The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured for and sent to a GitHub App. For more information, see "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str


class User(BaseModel):
    """A GitHub user."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: None | str = None
    email: None | str = None
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: None | str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    starred_at: str | None = None
    user_view_type: str | None = None


class SubIssuesSummary(BaseModel):
    """Sub-issues Summary."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int
    completed: int
    percent_completed: int


class PullRequestPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PullRequestPayload2(BaseModel):
    """Payload for the GitHub `pull_request` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class WebhooksAlert(BaseModel):
    """The security alert of the vulnerable dependency."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_reason: str | None = None
    dismissed_at: str | None = None
    dismisser: Any | None = None
    external_identifier: str
    external_reference: None | str
    fix_reason: str | None = None
    fixed_at: str | None = None
    fixed_in: str | None = None
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["open"]


class WebhooksApprover(BaseModel):
    """WebhooksApprover."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str | None = None
    events_url: str | None = None
    followers_url: str | None = None
    following_url: str | None = None
    gists_url: str | None = None
    gravatar_id: str | None = None
    html_url: str | None = None
    id: int | None = None
    login: str | None = None
    node_id: str | None = None
    organizations_url: str | None = None
    received_events_url: str | None = None
    repos_url: str | None = None
    site_admin: bool | None = None
    starred_url: str | None = None
    subscriptions_url: str | None = None
    type: str | None = None
    url: str | None = None
    user_view_type: str | None = None


class WebhooksDeployKey(BaseModel):
    """The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) resource."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    added_by: None | str = None
    created_at: str
    id: int
    key: str
    last_used: None | str = None
    read_only: bool
    title: str
    url: str
    verified: bool
    enabled: bool | None = None


class WebhooksLabel(BaseModel):
    """Label."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    default: bool
    description: None | str
    id: int
    name: str
    node_id: str
    url: str


class WebhooksMembership(BaseModel):
    """The membership between the user and the organization. Not present when the action is `member_invited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    organization_url: str
    role: str
    direct_membership: bool | None = None
    enterprise_teams_providing_indirect_membership: list[str] | None = None
    state: str
    url: str
    user: Any | None


class WebhooksMilestone(BaseModel):
    """A collection of related issues and pull requests."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: None | str
    closed_issues: int
    created_at: str
    creator: Any | None
    description: None | str
    due_on: None | str
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: str
    url: str


class WebhooksProject(BaseModel):
    """Project."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: None | str
    columns_url: str
    created_at: str
    creator: Any | None
    html_url: str
    id: int
    name: str
    node_id: str
    number: int
    owner_url: str
    state: Literal["open", "closed"]
    updated_at: str
    url: str


class WebhooksProjectCard(BaseModel):
    """Project Card."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after_id: None | int = None
    archived: bool
    column_id: int
    column_url: str
    content_url: str | None = None
    created_at: str
    creator: Any | None
    id: int
    node_id: str
    note: None | str
    project_url: str
    updated_at: str
    url: str


class WebhooksProjectColumn(BaseModel):
    """Project Column."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after_id: None | int = None
    cards_url: str
    created_at: str
    id: int
    name: str
    node_id: str
    project_url: str
    updated_at: str
    url: str


class WebhooksRule(BaseModel):
    """The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin_enforced: bool
    allow_deletions_enforcement_level: Literal["off", "non_admins", "everyone"]
    allow_force_pushes_enforcement_level: Literal["off", "non_admins", "everyone"]
    authorized_actor_names: list[str]
    authorized_actors_only: bool
    authorized_dismissal_actors_only: bool
    create_protected: bool | None = None
    created_at: str
    dismiss_stale_reviews_on_push: bool
    id: int
    ignore_approvals_from_contributors: bool
    linear_history_requirement_enforcement_level: Literal["off", "non_admins", "everyone"]
    lock_branch_enforcement_level: Literal["off", "non_admins", "everyone"]
    lock_allows_fork_sync: bool | None = None
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"]
    name: str
    pull_request_reviews_enforcement_level: Literal["off", "non_admins", "everyone"]
    repository_id: int
    require_code_owner_review: bool
    require_last_push_approval: bool | None = None
    required_approving_review_count: int
    required_conversation_resolution_level: Literal["off", "non_admins", "everyone"]
    required_deployments_enforcement_level: Literal["off", "non_admins", "everyone"]
    required_status_checks: list[str]
    required_status_checks_enforcement_level: Literal["off", "non_admins", "everyone"]
    signature_requirement_enforcement_level: Literal["off", "non_admins", "everyone"]
    strict_required_status_checks_policy: bool
    updated_at: str


class WebhooksTeam(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    notification_setting: Literal["notifications_enabled", "notifications_disabled"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None
    type: Literal["enterprise", "organization"] | None = None
    organization_id: int | None = None
    enterprise_id: int | None = None


class WebhooksTeam1(BaseModel):
    """Groups of organization members that gives permissions on specified repositories."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted: bool | None = None
    description: None | str = None
    html_url: str | None = None
    id: int
    members_url: str | None = None
    name: str
    node_id: str | None = None
    parent: Any | None = None
    permission: str | None = None
    privacy: Literal["open", "closed", "secret"] | None = None
    notification_setting: Literal["notifications_enabled", "notifications_disabled"] | None = None
    repositories_url: str | None = None
    slug: str | None = None
    url: str | None = None
    type: Literal["enterprise", "organization"] | None = None
    organization_id: int | None = None
    enterprise_id: int | None = None


class WebhooksWorkflowJobRun(BaseModel):
    """WebhooksWorkflowJobRun."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conclusion: None
    created_at: str
    environment: str
    html_url: str
    id: int
    name: None
    status: str
    updated_at: str


class BranchProtectionRuleEditedPayloadChanges(BaseModel):
    """If the action was `edited`, the changes to the rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin_enforced: BranchProtectionRuleEditedPayloadChangesAdminEnforced | None = None
    authorized_actor_names: BranchProtectionRuleEditedPayloadChangesAuthorizedActorNames | None = None
    authorized_actors_only: BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnly | None = None
    authorized_dismissal_actors_only: BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnly | None = (
        None
    )
    linear_history_requirement_enforcement_level: (
        BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevel | None
    ) = None
    lock_branch_enforcement_level: BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevel | None = None
    lock_allows_fork_sync: BranchProtectionRuleEditedPayloadChangesLockAllowsForkSync | None = None
    pull_request_reviews_enforcement_level: (
        BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevel | None
    ) = None
    require_last_push_approval: BranchProtectionRuleEditedPayloadChangesRequireLastPushApproval | None = None
    required_status_checks: BranchProtectionRuleEditedPayloadChangesRequiredStatusChecks | None = None
    required_status_checks_enforcement_level: (
        BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevel | None
    ) = None


class CheckSuiteCompletedPayloadCheckSuiteApp(BaseModel):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    description: None | str
    events: list[str] | None = None
    external_url: None | str
    html_url: str
    id: None | int
    client_id: None | str = None
    name: str
    node_id: str
    owner: Any | None
    permissions: CheckSuiteCompletedPayloadCheckSuiteAppPermissions | None = None
    slug: str | None = None
    updated_at: None | str


class CheckSuiteCompletedPayloadCheckSuiteHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthor
    committer: CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class CheckSuiteCompletedPayloadCheckSuitePullRequestBase(BaseModel):
    """CheckSuiteCompletedPayloadCheckSuitePullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepo
    sha: str


class CheckSuiteCompletedPayloadCheckSuitePullRequestHead(BaseModel):
    """CheckSuiteCompletedPayloadCheckSuitePullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepo
    sha: str


class CheckSuiteRequestedPayloadCheckSuiteApp(BaseModel):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    description: None | str
    events: list[str] | None = None
    external_url: None | str
    html_url: str
    id: None | int
    client_id: None | str = None
    name: str
    node_id: str
    owner: Any | None
    permissions: CheckSuiteRequestedPayloadCheckSuiteAppPermissions | None = None
    slug: str | None = None
    updated_at: None | str


class CheckSuiteRequestedPayloadCheckSuiteHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthor
    committer: CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class CheckSuiteRequestedPayloadCheckSuitePullRequestBase(BaseModel):
    """CheckSuiteRequestedPayloadCheckSuitePullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepo
    sha: str


class CheckSuiteRequestedPayloadCheckSuitePullRequestHead(BaseModel):
    """CheckSuiteRequestedPayloadCheckSuitePullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepo
    sha: str


class CheckSuiteRerequestedPayloadCheckSuiteApp(BaseModel):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    description: None | str
    events: list[str] | None = None
    external_url: None | str
    html_url: str
    id: None | int
    client_id: None | str = None
    name: str
    node_id: str
    owner: Any | None
    permissions: CheckSuiteRerequestedPayloadCheckSuiteAppPermissions | None = None
    slug: str | None = None
    updated_at: None | str


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthor
    committer: CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class CheckSuiteRerequestedPayloadCheckSuitePullRequestBase(BaseModel):
    """CheckSuiteRerequestedPayloadCheckSuitePullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepo
    sha: str


class CheckSuiteRerequestedPayloadCheckSuitePullRequestHead(BaseModel):
    """CheckSuiteRerequestedPayloadCheckSuitePullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepo
    sha: str


class CommitCommentCreatedPayloadComment(BaseModel):
    """The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    commit_id: str
    created_at: str
    html_url: str
    id: int
    line: None | int
    node_id: str
    path: None | str
    position: None | int
    reactions: CommitCommentCreatedPayloadCommentReactions | None = None
    updated_at: str
    url: str
    user: Any | None


class DiscussionCategoryChangedPayloadChangesCategory(BaseModel):
    """DiscussionCategoryChangedPayloadChangesCategory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: DiscussionCategoryChangedPayloadChangesCategoryFrom = Field(alias="from")


class DiscussionCommentEditedPayloadChanges(BaseModel):
    """DiscussionCommentEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: DiscussionCommentEditedPayloadChangesBody


class DiscussionEditedPayloadChanges(BaseModel):
    """DiscussionEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: DiscussionEditedPayloadChangesBody | None = None
    title: DiscussionEditedPayloadChangesTitle | None = None


class InstallationTargetRenamedPayloadChanges(BaseModel):
    """InstallationTargetRenamedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: InstallationTargetRenamedPayloadChangesLogin | None = None
    slug: InstallationTargetRenamedPayloadChangesSlug | None = None


class IssueCommentCreatedPayloadComment(BaseModel):
    """The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    created_at: str
    html_url: str
    id: int
    issue_url: str
    node_id: str
    performed_via_github_app: Any | None
    reactions: IssueCommentCreatedPayloadCommentReactions
    updated_at: str
    url: str
    user: Any | None


class IssuesEditedPayloadChanges(BaseModel):
    """The changes to the issue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: IssuesEditedPayloadChangesBody | None = None
    title: IssuesEditedPayloadChangesTitle | None = None


class IssuesOpenedPayloadChangesOldRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_discussions: bool | None = None
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: IssuesOpenedPayloadChangesOldRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class IssuesTransferredPayloadChangesNewRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: IssuesTransferredPayloadChangesNewRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class LabelEditedPayloadChanges(BaseModel):
    """The changes to the label if the action was `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: LabelEditedPayloadChangesColor | None = None
    description: LabelEditedPayloadChangesDescription | None = None
    name: LabelEditedPayloadChangesName | None = None


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchase(BaseModel):
    """Marketplace Purchase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccount
    billing_cycle: str
    free_trial_ends_on: None | str
    next_billing_date: None | str = None
    on_free_trial: None | bool
    plan: MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlan
    unit_count: int


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchase(BaseModel):
    """Marketplace Purchase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccount
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: None | str
    on_free_trial: bool
    plan: MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlan
    unit_count: int


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchase(BaseModel):
    """Marketplace Purchase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccount
    billing_cycle: str
    free_trial_ends_on: None | str
    next_billing_date: None | str = None
    on_free_trial: bool
    plan: MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlan
    unit_count: int


class MemberAddedPayloadChanges(BaseModel):
    """MemberAddedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permission: MemberAddedPayloadChangesPermission | None = None
    role_name: MemberAddedPayloadChangesRoleName | None = None


class MemberEditedPayloadChanges(BaseModel):
    """The changes to the collaborator permissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    old_permission: MemberEditedPayloadChangesOldPermission | None = None
    permission: MemberEditedPayloadChangesPermission | None = None


class MetaDeletedPayloadHook(BaseModel):
    """The deleted webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool
    config: MetaDeletedPayloadHookConfig
    created_at: str
    events: list[str]
    id: int
    name: str
    type: str
    updated_at: str


class MilestoneEditedPayloadChanges(BaseModel):
    """The changes to the milestone if the action was `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: MilestoneEditedPayloadChangesDescription | None = None
    due_on: MilestoneEditedPayloadChangesDueOn | None = None
    title: MilestoneEditedPayloadChangesTitle | None = None


class OrganizationRenamedPayloadChanges(BaseModel):
    """OrganizationRenamedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: OrganizationRenamedPayloadChangesLogin | None = None


class PageBuildPayloadBuild(BaseModel):
    """The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-github-pages-builds) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: None | str
    created_at: str
    duration: int
    error: PageBuildPayloadBuildError
    pusher: Any | None
    status: str
    updated_at: str
    url: str


class ProjectCardConvertedPayloadChanges(BaseModel):
    """ProjectCardConvertedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    note: ProjectCardConvertedPayloadChangesNote


class ProjectCardEditedPayloadChanges(BaseModel):
    """ProjectCardEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    note: ProjectCardEditedPayloadChangesNote


class ProjectCardMovedPayloadChanges(BaseModel):
    """ProjectCardMovedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    column_id: ProjectCardMovedPayloadChangesColumnId


class ProjectColumnEditedPayloadChanges(BaseModel):
    """ProjectColumnEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: ProjectColumnEditedPayloadChangesName | None = None


class ProjectEditedPayloadChanges(BaseModel):
    """The changes to the project if the action was `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: ProjectEditedPayloadChangesBody | None = None
    name: ProjectEditedPayloadChangesName | None = None


class ProjectsV2EditedPayloadChanges(BaseModel):
    """ProjectsV2EditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: ProjectsV2EditedPayloadChangesDescription | None = None
    public: ProjectsV2EditedPayloadChangesPublic | None = None
    short_description: ProjectsV2EditedPayloadChangesShortDescription | None = None
    title: ProjectsV2EditedPayloadChangesTitle | None = None


class ProjectsV2ItemConvertedPayloadChanges(BaseModel):
    """ProjectsV2ItemConvertedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_type: ProjectsV2ItemConvertedPayloadChangesContentType | None = None


class ProjectsV2ItemEditedPayloadChangesOption2(BaseModel):
    """ProjectsV2ItemEditedPayloadChangesOption2."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: ProjectsV2ItemEditedPayloadChangesOption2Body


class ProjectsV2ItemReorderedPayloadChanges(BaseModel):
    """ProjectsV2ItemReorderedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    previous_projects_v2_item_node_id: ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeId | None = None


class ProjectsV2StatusUpdateEditedPayloadChanges(BaseModel):
    """ProjectsV2StatusUpdateEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: ProjectsV2StatusUpdateEditedPayloadChangesBody | None = None
    status: ProjectsV2StatusUpdateEditedPayloadChangesStatus | None = None
    start_date: ProjectsV2StatusUpdateEditedPayloadChangesStartDate | None = None
    target_date: ProjectsV2StatusUpdateEditedPayloadChangesTargetDate | None = None


class PullRequestAssignedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestAssignedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestAssignedPayloadPullRequestLinks(BaseModel):
    """PullRequestAssignedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestAssignedPayloadPullRequestLinksComments
    commits: PullRequestAssignedPayloadPullRequestLinksCommits
    html: PullRequestAssignedPayloadPullRequestLinksHtml
    issue: PullRequestAssignedPayloadPullRequestLinksIssue
    review_comment: PullRequestAssignedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestAssignedPayloadPullRequestLinksReviewComments
    self: PullRequestAssignedPayloadPullRequestLinksSelf
    statuses: PullRequestAssignedPayloadPullRequestLinksStatuses


class PullRequestAutoMergeDisabledPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_discussions: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestAutoMergeDisabledPayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestAutoMergeDisabledPayloadPullRequestLinks(BaseModel):
    """PullRequestAutoMergeDisabledPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestAutoMergeDisabledPayloadPullRequestLinksComments
    commits: PullRequestAutoMergeDisabledPayloadPullRequestLinksCommits
    html: PullRequestAutoMergeDisabledPayloadPullRequestLinksHtml
    issue: PullRequestAutoMergeDisabledPayloadPullRequestLinksIssue
    review_comment: PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComment
    review_comments: PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewComments
    self: PullRequestAutoMergeDisabledPayloadPullRequestLinksSelf
    statuses: PullRequestAutoMergeDisabledPayloadPullRequestLinksStatuses


class PullRequestAutoMergeEnabledPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestAutoMergeEnabledPayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestAutoMergeEnabledPayloadPullRequestLinks(BaseModel):
    """PullRequestAutoMergeEnabledPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestAutoMergeEnabledPayloadPullRequestLinksComments
    commits: PullRequestAutoMergeEnabledPayloadPullRequestLinksCommits
    html: PullRequestAutoMergeEnabledPayloadPullRequestLinksHtml
    issue: PullRequestAutoMergeEnabledPayloadPullRequestLinksIssue
    review_comment: PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComment
    review_comments: PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewComments
    self: PullRequestAutoMergeEnabledPayloadPullRequestLinksSelf
    statuses: PullRequestAutoMergeEnabledPayloadPullRequestLinksStatuses


class PullRequestDequeuedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestDequeuedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestDequeuedPayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestDequeuedPayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestDequeuedPayloadPullRequestLinks(BaseModel):
    """PullRequestDequeuedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestDequeuedPayloadPullRequestLinksComments
    commits: PullRequestDequeuedPayloadPullRequestLinksCommits
    html: PullRequestDequeuedPayloadPullRequestLinksHtml
    issue: PullRequestDequeuedPayloadPullRequestLinksIssue
    review_comment: PullRequestDequeuedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestDequeuedPayloadPullRequestLinksReviewComments
    self: PullRequestDequeuedPayloadPullRequestLinksSelf
    statuses: PullRequestDequeuedPayloadPullRequestLinksStatuses


class PullRequestEditedPayloadChangesBase(BaseModel):
    """PullRequestEditedPayloadChangesBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: PullRequestEditedPayloadChangesBaseRef
    sha: PullRequestEditedPayloadChangesBaseSha


class PullRequestEnqueuedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestEnqueuedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestEnqueuedPayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestEnqueuedPayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestEnqueuedPayloadPullRequestLinks(BaseModel):
    """PullRequestEnqueuedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestEnqueuedPayloadPullRequestLinksComments
    commits: PullRequestEnqueuedPayloadPullRequestLinksCommits
    html: PullRequestEnqueuedPayloadPullRequestLinksHtml
    issue: PullRequestEnqueuedPayloadPullRequestLinksIssue
    review_comment: PullRequestEnqueuedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestEnqueuedPayloadPullRequestLinksReviewComments
    self: PullRequestEnqueuedPayloadPullRequestLinksSelf
    statuses: PullRequestEnqueuedPayloadPullRequestLinksStatuses


class PullRequestLabeledPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestLabeledPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestLabeledPayloadPullRequestLinks(BaseModel):
    """PullRequestLabeledPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestLabeledPayloadPullRequestLinksComments
    commits: PullRequestLabeledPayloadPullRequestLinksCommits
    html: PullRequestLabeledPayloadPullRequestLinksHtml
    issue: PullRequestLabeledPayloadPullRequestLinksIssue
    review_comment: PullRequestLabeledPayloadPullRequestLinksReviewComment
    review_comments: PullRequestLabeledPayloadPullRequestLinksReviewComments
    self: PullRequestLabeledPayloadPullRequestLinksSelf
    statuses: PullRequestLabeledPayloadPullRequestLinksStatuses


class PullRequestLockedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestLockedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestLockedPayloadPullRequestLinks(BaseModel):
    """PullRequestLockedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestLockedPayloadPullRequestLinksComments
    commits: PullRequestLockedPayloadPullRequestLinksCommits
    html: PullRequestLockedPayloadPullRequestLinksHtml
    issue: PullRequestLockedPayloadPullRequestLinksIssue
    review_comment: PullRequestLockedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestLockedPayloadPullRequestLinksReviewComments
    self: PullRequestLockedPayloadPullRequestLinksSelf
    statuses: PullRequestLockedPayloadPullRequestLinksStatuses


class PullRequestMinimalBase(BaseModel):
    """PullRequestMinimalBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    sha: str
    repo: PullRequestMinimalBaseRepo


class PullRequestMinimalHead(BaseModel):
    """PullRequestMinimalHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    sha: str
    repo: PullRequestMinimalHeadRepo


class PullRequestReviewCommentCreatedPayloadCommentLinks(BaseModel):
    """PullRequestReviewCommentCreatedPayloadCommentLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: PullRequestReviewCommentCreatedPayloadCommentLinksHtml
    pull_request: PullRequestReviewCommentCreatedPayloadCommentLinksPullRequest
    self: PullRequestReviewCommentCreatedPayloadCommentLinksSelf


class PullRequestReviewCommentCreatedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewCommentCreatedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewCommentCreatedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewCommentCreatedPayloadPullRequestLinksComments
    commits: PullRequestReviewCommentCreatedPayloadPullRequestLinksCommits
    html: PullRequestReviewCommentCreatedPayloadPullRequestLinksHtml
    issue: PullRequestReviewCommentCreatedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewCommentCreatedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewCommentCreatedPayloadPullRequestLinksStatuses


class PullRequestReviewCommentDeletedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewCommentDeletedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewCommentDeletedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewCommentDeletedPayloadPullRequestLinksComments
    commits: PullRequestReviewCommentDeletedPayloadPullRequestLinksCommits
    html: PullRequestReviewCommentDeletedPayloadPullRequestLinksHtml
    issue: PullRequestReviewCommentDeletedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewCommentDeletedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewCommentDeletedPayloadPullRequestLinksStatuses


class PullRequestReviewCommentEditedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewCommentEditedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewCommentEditedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewCommentEditedPayloadPullRequestLinksComments
    commits: PullRequestReviewCommentEditedPayloadPullRequestLinksCommits
    html: PullRequestReviewCommentEditedPayloadPullRequestLinksHtml
    issue: PullRequestReviewCommentEditedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewCommentEditedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewCommentEditedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewCommentEditedPayloadPullRequestLinksStatuses


class PullRequestReviewDismissedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewDismissedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewDismissedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewDismissedPayloadPullRequestLinksComments
    commits: PullRequestReviewDismissedPayloadPullRequestLinksCommits
    html: PullRequestReviewDismissedPayloadPullRequestLinksHtml
    issue: PullRequestReviewDismissedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewDismissedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewDismissedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewDismissedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewDismissedPayloadPullRequestLinksStatuses


class PullRequestReviewDismissedPayloadReviewLinks(BaseModel):
    """PullRequestReviewDismissedPayloadReviewLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: PullRequestReviewDismissedPayloadReviewLinksHtml
    pull_request: PullRequestReviewDismissedPayloadReviewLinksPullRequest


class PullRequestReviewEditedPayloadChanges(BaseModel):
    """PullRequestReviewEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: PullRequestReviewEditedPayloadChangesBody | None = None


class PullRequestReviewEditedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewEditedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class PullRequestReviewEditedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewEditedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewEditedPayloadPullRequestLinksComments
    commits: PullRequestReviewEditedPayloadPullRequestLinksCommits
    html: PullRequestReviewEditedPayloadPullRequestLinksHtml
    issue: PullRequestReviewEditedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewEditedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewEditedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewEditedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewEditedPayloadPullRequestLinksStatuses


class PullRequestReviewSubmittedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewSubmittedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewSubmittedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewSubmittedPayloadPullRequestLinksComments
    commits: PullRequestReviewSubmittedPayloadPullRequestLinksCommits
    html: PullRequestReviewSubmittedPayloadPullRequestLinksHtml
    issue: PullRequestReviewSubmittedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewSubmittedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewSubmittedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewSubmittedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewSubmittedPayloadPullRequestLinksStatuses


class PullRequestReviewThreadResolvedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewThreadResolvedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewThreadResolvedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewThreadResolvedPayloadPullRequestLinksComments
    commits: PullRequestReviewThreadResolvedPayloadPullRequestLinksCommits
    html: PullRequestReviewThreadResolvedPayloadPullRequestLinksHtml
    issue: PullRequestReviewThreadResolvedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewThreadResolvedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewThreadResolvedPayloadPullRequestLinksStatuses


class PullRequestReviewThreadResolvedPayloadThreadCommentLinks(BaseModel):
    """PullRequestReviewThreadResolvedPayloadThreadCommentLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtml
    pull_request: PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequest
    self: PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelf


class PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinks(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksComments
    commits: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommits
    html: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtml
    issue: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssue
    review_comment: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewComments
    self: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelf
    statuses: PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatuses


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinks(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadThreadCommentLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtml
    pull_request: PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequest
    self: PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelf


class PullRequestSynchronizePayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestSynchronizePayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestSynchronizePayloadPullRequestHeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestSynchronizePayloadPullRequestHeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestSynchronizePayloadPullRequestLinks(BaseModel):
    """PullRequestSynchronizePayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestSynchronizePayloadPullRequestLinksComments
    commits: PullRequestSynchronizePayloadPullRequestLinksCommits
    html: PullRequestSynchronizePayloadPullRequestLinksHtml
    issue: PullRequestSynchronizePayloadPullRequestLinksIssue
    review_comment: PullRequestSynchronizePayloadPullRequestLinksReviewComment
    review_comments: PullRequestSynchronizePayloadPullRequestLinksReviewComments
    self: PullRequestSynchronizePayloadPullRequestLinksSelf
    statuses: PullRequestSynchronizePayloadPullRequestLinksStatuses


class PullRequestUnassignedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestUnassignedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestUnassignedPayloadPullRequestLinks(BaseModel):
    """PullRequestUnassignedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestUnassignedPayloadPullRequestLinksComments
    commits: PullRequestUnassignedPayloadPullRequestLinksCommits
    html: PullRequestUnassignedPayloadPullRequestLinksHtml
    issue: PullRequestUnassignedPayloadPullRequestLinksIssue
    review_comment: PullRequestUnassignedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestUnassignedPayloadPullRequestLinksReviewComments
    self: PullRequestUnassignedPayloadPullRequestLinksSelf
    statuses: PullRequestUnassignedPayloadPullRequestLinksStatuses


class PullRequestUnlabeledPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestUnlabeledPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestUnlabeledPayloadPullRequestLinks(BaseModel):
    """PullRequestUnlabeledPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestUnlabeledPayloadPullRequestLinksComments
    commits: PullRequestUnlabeledPayloadPullRequestLinksCommits
    html: PullRequestUnlabeledPayloadPullRequestLinksHtml
    issue: PullRequestUnlabeledPayloadPullRequestLinksIssue
    review_comment: PullRequestUnlabeledPayloadPullRequestLinksReviewComment
    review_comments: PullRequestUnlabeledPayloadPullRequestLinksReviewComments
    self: PullRequestUnlabeledPayloadPullRequestLinksSelf
    statuses: PullRequestUnlabeledPayloadPullRequestLinksStatuses


class PullRequestUnlockedPayloadPullRequestBaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PullRequestUnlockedPayloadPullRequestBaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class PullRequestUnlockedPayloadPullRequestLinks(BaseModel):
    """PullRequestUnlockedPayloadPullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: PullRequestUnlockedPayloadPullRequestLinksComments
    commits: PullRequestUnlockedPayloadPullRequestLinksCommits
    html: PullRequestUnlockedPayloadPullRequestLinksHtml
    issue: PullRequestUnlockedPayloadPullRequestLinksIssue
    review_comment: PullRequestUnlockedPayloadPullRequestLinksReviewComment
    review_comments: PullRequestUnlockedPayloadPullRequestLinksReviewComments
    self: PullRequestUnlockedPayloadPullRequestLinksSelf
    statuses: PullRequestUnlockedPayloadPullRequestLinksStatuses


class PushPayloadCommit(BaseModel):
    """Commit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    added: list[str] | None = None
    author: PushPayloadCommitAuthor
    committer: PushPayloadCommitCommitter
    distinct: bool
    id: str
    message: str
    modified: list[str] | None = None
    removed: list[str] | None = None
    timestamp: str
    tree_id: str
    url: str


class PushPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool | None = None
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: PushPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str] | None = None
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"] | None = None
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class RegistryPackagePublishedPayloadRegistryPackage(BaseModel):
    """RegistryPackagePublishedPayloadRegistryPackage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    description: None | str
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: RegistryPackagePublishedPayloadRegistryPackageOwner
    package_type: str
    package_version: Any | None
    registry: Any | None
    updated_at: None | str


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionRelease(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionRelease."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthor
    created_at: str
    draft: bool
    html_url: str
    id: int
    name: str
    prerelease: bool
    published_at: str
    tag_name: str
    target_commitish: str
    url: str


class ReleaseEditedPayloadChanges(BaseModel):
    """ReleaseEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: ReleaseEditedPayloadChangesBody | None = None
    name: ReleaseEditedPayloadChangesName | None = None
    tag_name: ReleaseEditedPayloadChangesTagName | None = None
    make_latest: ReleaseEditedPayloadChangesMakeLatest | None = None


class ReleasePrereleasedPayloadRelease(BaseModel):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: list[Any | None]
    assets_url: str
    author: Any | None
    body: None | str
    created_at: None | str
    discussion_url: str | None = None
    draft: bool
    html_url: str
    id: int
    immutable: bool
    name: None | str
    node_id: str
    prerelease: Literal[True]
    published_at: None | str
    reactions: ReleasePrereleasedPayloadReleaseReactions | None = None
    tag_name: str
    tarball_url: None | str
    target_commitish: str
    upload_url: str
    updated_at: None | str
    url: str
    zipball_url: None | str


class RepositoryAdvisory(BaseModel):
    """A repository security advisory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ghsa_id: str
    cve_id: None | str
    url: str
    html_url: str
    summary: str
    description: None | str
    severity: Literal["critical", "high", "medium", "low"] | None
    author: None
    publisher: None
    identifiers: list[RepositoryAdvisoryIdentifier]
    state: Literal["published", "closed", "withdrawn", "draft", "triage"]
    created_at: None | str
    updated_at: None | str
    published_at: None | str
    closed_at: None | str
    withdrawn_at: None | str
    submission: Any | None
    vulnerabilities: Any | None
    cvss: Any | None
    cvss_severities: Any | None = None
    cwes: Any | None
    cwe_ids: Any | None
    credits: Any | None
    credits_detailed: Any | None
    collaborating_users: Any | None
    collaborating_teams: Any | None
    private_fork: None


class RepositoryEditedPayloadChanges(BaseModel):
    """RepositoryEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    default_branch: RepositoryEditedPayloadChangesDefaultBranch | None = None
    description: RepositoryEditedPayloadChangesDescription | None = None
    homepage: RepositoryEditedPayloadChangesHomepage | None = None
    topics: RepositoryEditedPayloadChangesTopics | None = None


class RepositoryRenamedPayloadChangesRepository(BaseModel):
    """RepositoryRenamedPayloadChangesRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: RepositoryRenamedPayloadChangesRepositoryName


class RepositoryRuleBranchNamePattern(BaseModel):
    """Parameters to be used for the branch_name_pattern rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["branch_name_pattern"]
    parameters: RepositoryRuleBranchNamePatternParameters | None = None


class RepositoryRuleCommitAuthorEmailPattern(BaseModel):
    """Parameters to be used for the commit_author_email_pattern rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["commit_author_email_pattern"]
    parameters: RepositoryRuleCommitAuthorEmailPatternParameters | None = None


class RepositoryRuleCommitMessagePattern(BaseModel):
    """Parameters to be used for the commit_message_pattern rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["commit_message_pattern"]
    parameters: RepositoryRuleCommitMessagePatternParameters | None = None


class RepositoryRuleCommitterEmailPattern(BaseModel):
    """Parameters to be used for the committer_email_pattern rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["committer_email_pattern"]
    parameters: RepositoryRuleCommitterEmailPatternParameters | None = None


class RepositoryRuleCopilotCodeReview(BaseModel):
    """Request Copilot code review for new pull requests automatically if the author has access to Copilot code review and their premium requests quota has not reached the limit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["copilot_code_review"]
    parameters: RepositoryRuleCopilotCodeReviewParameters | None = None


class RepositoryRuleFileExtensionRestriction(BaseModel):
    """Prevent commits that include files with specified file extensions from being pushed to the commit graph."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["file_extension_restriction"]
    parameters: RepositoryRuleFileExtensionRestrictionParameters | None = None


class RepositoryRuleFilePathRestriction(BaseModel):
    """Prevent commits that include changes in specified file and folder paths from being pushed to the commit graph. This includes absolute paths that contain file names."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["file_path_restriction"]
    parameters: RepositoryRuleFilePathRestrictionParameters | None = None


class RepositoryRuleMaxFilePathLength(BaseModel):
    """Prevent commits that include file paths that exceed the specified character limit from being pushed to the commit graph."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["max_file_path_length"]
    parameters: RepositoryRuleMaxFilePathLengthParameters | None = None


class RepositoryRuleMaxFileSize(BaseModel):
    """Prevent commits with individual files that exceed the specified limit from being pushed to the commit graph."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["max_file_size"]
    parameters: RepositoryRuleMaxFileSizeParameters | None = None


class RepositoryRuleMergeQueue(BaseModel):
    """Merges must be performed via a merge queue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["merge_queue"]
    parameters: RepositoryRuleMergeQueueParameters | None = None


class RepositoryRuleRequiredDeployments(BaseModel):
    """Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["required_deployments"]
    parameters: RepositoryRuleRequiredDeploymentsParameters | None = None


class RepositoryRuleTagNamePattern(BaseModel):
    """Parameters to be used for the tag_name_pattern rule."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["tag_name_pattern"]
    parameters: RepositoryRuleTagNamePatternParameters | None = None


class RepositoryRuleUpdate(BaseModel):
    """Only allow users with bypass permission to update matching refs."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["update"]
    parameters: RepositoryRuleUpdateParameters | None = None


class RepositoryRulesetConditions(BaseModel):
    """Parameters for a repository ruleset ref name condition."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref_name: RepositoryRulesetConditionsRefName | None = None


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChanges(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    condition_type: RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionType | None = None
    target: RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTarget | None = None
    include: RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesInclude | None = None
    exclude: RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExclude | None = None


class RepositoryRulesetEditedPayloadChangesRulesUpdatedChanges(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    configuration: RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfiguration | None = None
    rule_type: RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleType | None = None
    pattern: RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPattern | None = None


class RepositoryRulesetLinks(BaseModel):
    """RepositoryRulesetLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: RepositoryRulesetLinksSelf | None = None
    html: Any | None = None


class RepositoryTransferredPayloadChangesOwnerFrom(BaseModel):
    """RepositoryTransferredPayloadChangesOwnerFrom."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    organization: RepositoryTransferredPayloadChangesOwnerFromOrganization | None = None
    user: Any | None = None


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerability(BaseModel):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerability."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_patched_version: Any | None
    package: SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackage
    severity: str
    vulnerable_version_range: str


class SecurityAndAnalysisPayloadChanges(BaseModel):
    """SecurityAndAnalysisPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: SecurityAndAnalysisPayloadChangesFrom | None = Field(default=None, alias="from")


class SponsorshipEditedPayloadChanges(BaseModel):
    """SponsorshipEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    privacy_level: SponsorshipEditedPayloadChangesPrivacyLevel | None = None


class StatusPayloadBranche(BaseModel):
    """StatusPayloadBranche."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: StatusPayloadBrancheCommit
    name: str
    protected: bool


class StatusPayloadCommitCommit(BaseModel):
    """StatusPayloadCommitCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: Any
    comment_count: int
    committer: Any
    message: str
    tree: StatusPayloadCommitCommitTree
    url: str
    verification: StatusPayloadCommitCommitVerification


class TeamAddedToRepositoryPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: TeamAddedToRepositoryPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class TeamCreatedPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: TeamCreatedPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class TeamDeletedPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: TeamDeletedPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class TeamEditedPayloadChangesRepositoryPermissions(BaseModel):
    """TeamEditedPayloadChangesRepositoryPermissions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: TeamEditedPayloadChangesRepositoryPermissionsFrom = Field(alias="from")


class TeamEditedPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: TeamEditedPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class TeamRemovedFromRepositoryPayloadRepository(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    custom_properties: dict[str, Any] | None = None
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: TeamRemovedFromRepositoryPayloadRepositoryPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class WebhookRubygemsMetadata(BaseModel):
    """Ruby Gems metadata."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    description: str | None = None
    readme: str | None = None
    homepage: str | None = None
    version_info: WebhookRubygemsMetadataVersionInfo | None = None
    platform: str | None = None
    metadata: dict[str, Any] | None = None
    repo: str | None = None
    dependencies: list[dict[str, Any]] | None = None
    commit_oid: str | None = None


class WebhooksAnswer(BaseModel):
    """WebhooksAnswer."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    child_comment_count: int
    created_at: str
    discussion_id: int
    html_url: str
    id: int
    node_id: str
    parent_id: None
    reactions: WebhooksAnswerReactions | None = None
    repository_url: str
    updated_at: str
    user: Any | None


class WebhooksChanges8Tier(BaseModel):
    """WebhooksChanges8Tier."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: WebhooksChanges8TierFrom = Field(alias="from")


class WebhooksChanges(BaseModel):
    """The changes to the comment."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: WebhooksChangesBody | None = None


class WebhooksComment(BaseModel):
    """WebhooksComment."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    child_comment_count: int
    created_at: str
    discussion_id: int
    html_url: str
    id: int
    node_id: str
    parent_id: None | int
    reactions: WebhooksCommentReactions
    repository_url: str
    updated_at: str
    user: Any | None


class WebhooksIssueComment(BaseModel):
    """The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    created_at: str
    html_url: str
    id: int
    issue_url: str
    node_id: str
    performed_via_github_app: Any | None
    reactions: WebhooksIssueCommentReactions
    updated_at: str
    url: str
    user: Any | None


class WebhooksMarketplacePurchase(BaseModel):
    """Marketplace Purchase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: WebhooksMarketplacePurchaseAccount
    billing_cycle: str
    free_trial_ends_on: None | str
    next_billing_date: None | str
    on_free_trial: bool
    plan: WebhooksMarketplacePurchasePlan
    unit_count: int


class WebhooksPreviousMarketplacePurchase(BaseModel):
    """Marketplace Purchase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: WebhooksPreviousMarketplacePurchaseAccount
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: None | str = None
    on_free_trial: bool
    plan: WebhooksPreviousMarketplacePurchasePlan
    unit_count: int


class WebhooksProjectChanges(BaseModel):
    """WebhooksProjectChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived_at: WebhooksProjectChangesArchivedAt | None = None


class WebhooksPullRequest5BaseRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: WebhooksPullRequest5BaseRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class WebhooksPullRequest5HeadRepo(BaseModel):
    """A git repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_auto_merge: bool | None = None
    allow_forking: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_squash_merge: bool | None = None
    allow_update_branch: bool | None = None
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: int | str
    default_branch: str
    delete_branch_on_merge: bool | None = None
    deployments_url: str
    description: None | str
    disabled: bool | None = None
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: None | str
    hooks_url: str
    html_url: str
    id: int
    is_template: bool | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: None | str
    languages_url: str
    license: Any | None
    master_branch: str | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merges_url: str
    milestones_url: str
    mirror_url: None | str
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: str | None = None
    owner: Any | None
    permissions: WebhooksPullRequest5HeadRepoPermissions | None = None
    private: bool
    public: bool | None = None
    pulls_url: str
    pushed_at: int | str
    releases_url: str
    role_name: None | str = None
    size: int
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    ssh_url: str
    stargazers: int | None = None
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: str
    url: str
    use_squash_pr_title_as_default: bool | None = None
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: bool | None = None


class WebhooksPullRequest5Links(BaseModel):
    """WebhooksPullRequest5Links."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: WebhooksPullRequest5LinksComments
    commits: WebhooksPullRequest5LinksCommits
    html: WebhooksPullRequest5LinksHtml
    issue: WebhooksPullRequest5LinksIssue
    review_comment: WebhooksPullRequest5LinksReviewComment
    review_comments: WebhooksPullRequest5LinksReviewComments
    self: WebhooksPullRequest5LinksSelf
    statuses: WebhooksPullRequest5LinksStatuses


class WebhooksRelease1(BaseModel):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: list[Any | None]
    assets_url: str
    author: Any | None
    body: None | str
    created_at: None | str
    discussion_url: str | None = None
    draft: bool
    html_url: str
    id: int
    immutable: bool
    name: None | str
    node_id: str
    prerelease: bool
    published_at: None | str
    reactions: WebhooksRelease1Reactions | None = None
    tag_name: str
    tarball_url: None | str
    target_commitish: str
    updated_at: None | str
    upload_url: str
    url: str
    zipball_url: None | str


class WebhooksRelease(BaseModel):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: list[WebhooksReleaseAsset]
    assets_url: str
    author: Any | None
    body: None | str
    created_at: None | str
    updated_at: None | str
    discussion_url: str | None = None
    draft: bool
    html_url: str
    id: int
    immutable: bool
    name: None | str
    node_id: str
    prerelease: bool
    published_at: None | str
    reactions: WebhooksReleaseReactions | None = None
    tag_name: str
    tarball_url: None | str
    target_commitish: str
    upload_url: str
    url: str
    zipball_url: None | str


class WebhooksReviewCommentLinks(BaseModel):
    """WebhooksReviewCommentLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: WebhooksReviewCommentLinksHtml
    pull_request: WebhooksReviewCommentLinksPullRequest
    self: WebhooksReviewCommentLinksSelf


class WebhooksReviewLinks(BaseModel):
    """WebhooksReviewLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html: WebhooksReviewLinksHtml
    pull_request: WebhooksReviewLinksPullRequest


class WebhooksSecurityAdvisoryVulnerability(BaseModel):
    """WebhooksSecurityAdvisoryVulnerability."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_patched_version: Any | None
    package: WebhooksSecurityAdvisoryVulnerabilityPackage
    severity: str
    vulnerable_version_range: str


class WebhooksSponsorship(BaseModel):
    """WebhooksSponsorship."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    maintainer: WebhooksSponsorshipMaintainer | None = None
    node_id: str
    privacy_level: str
    sponsor: Any | None
    sponsorable: Any | None
    tier: WebhooksSponsorshipTier


class WorkflowJobQueuedPayloadWorkflowJob(BaseModel):
    """WorkflowJobQueuedPayloadWorkflowJob."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    check_run_url: str
    completed_at: None | str
    conclusion: None | str
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: list[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: float
    run_url: str
    runner_group_id: None | int
    runner_group_name: None | str
    runner_id: None | int
    runner_name: None | str
    started_at: str
    status: Literal["queued", "in_progress", "completed", "waiting"]
    head_branch: None | str
    workflow_name: None | str
    steps: list[WorkflowJobQueuedPayloadWorkflowJobStep]
    url: str


class WorkflowJobWaitingPayloadWorkflowJob(BaseModel):
    """WorkflowJobWaitingPayloadWorkflowJob."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    check_run_url: str
    completed_at: None | str
    conclusion: None | str
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: list[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: float
    run_url: str
    runner_group_id: None | int
    runner_group_name: None | str
    runner_id: None | int
    runner_name: None | str
    started_at: str
    head_branch: None | str
    workflow_name: None | str
    status: Literal["queued", "in_progress", "completed", "waiting"]
    steps: list[WorkflowJobWaitingPayloadWorkflowJobStep]
    url: str


class WorkflowRunCompletedPayloadWorkflowRunHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthor
    committer: WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class WorkflowRunInProgressPayloadWorkflowRunHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthor
    committer: WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class WorkflowRunRequestedPayloadWorkflowRunHeadCommit(BaseModel):
    """SimpleCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthor
    committer: WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitter
    id: str
    message: str
    timestamp: str
    tree_id: str


class WorkflowRunRequestedPayloadWorkflowRunPullRequestBase(BaseModel):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepo
    sha: str


class WorkflowRunRequestedPayloadWorkflowRunPullRequestHead(BaseModel):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ref: str
    repo: WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepo
    sha: str


class DependabotAlertDependency(BaseModel):
    """Details for the vulnerable dependency."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    package: DependabotAlertPackage | None = None
    manifest_path: str | None = None
    scope: Literal["development", "runtime"] | None = None
    relationship: Literal["unknown", "direct", "transitive"] | None = None


class DependabotAlertSecurityVulnerability(BaseModel):
    """Details pertaining to one vulnerable version range for the advisory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    package: DependabotAlertPackage
    severity: Literal["low", "medium", "high", "critical"]
    vulnerable_version_range: str
    first_patched_version: Any | None


class PingPayloadHook(BaseModel):
    """The webhook that is being pinged."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool
    app_id: int | None = None
    config: PingPayloadHookConfig
    created_at: str
    deliveries_url: str | None = None
    events: list[str]
    id: int
    last_response: HookResponse | None = None
    name: Literal["web"]
    ping_url: str | None = None
    test_url: str | None = None
    type: str
    updated_at: str
    url: str | None = None


class Discussion(BaseModel):
    """A Discussion in a repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: None | str
    answer_chosen_at: None | str
    answer_chosen_by: Any | None
    answer_html_url: None | str
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    category: DiscussionCategory
    comments: int
    created_at: str
    html_url: str
    id: int
    locked: bool
    node_id: str
    number: int
    reactions: DiscussionReactions | None = None
    repository_url: str
    state: Literal["open", "closed", "locked", "converting", "transferring"]
    state_reason: Literal["resolved", "outdated", "duplicate", "reopened"] | None
    timeline_url: str | None = None
    title: str
    updated_at: str
    user: Any | None
    labels: list[Label] | None = None


class PullRequestLinks(BaseModel):
    """PullRequestLinks."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: Link
    commits: Link
    statuses: Link
    html: Link
    issue: Link
    review_comments: Link
    review_comment: Link
    self: Link


class ProjectsV2ItemEditedPayloadChangesOption1FieldValue(BaseModel):
    """ProjectsV2ItemEditedPayloadChangesOption1FieldValue."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_node_id: str | None = None
    field_type: str | None = None
    field_name: str | None = None
    project_number: int | None = None
    from_: ProjectsV2IterationSetting | ProjectsV2SingleSelectOption | int | str | None = Field(
        default=None, alias="from"
    )
    to: ProjectsV2IterationSetting | ProjectsV2SingleSelectOption | int | str | None = None


class RepositoryRuleCodeScanningParameters(BaseModel):
    """RepositoryRuleCodeScanningParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code_scanning_tools: list[RepositoryRuleParamsCodeScanningTool]


class RepositoryRuleParamsRequiredReviewerConfiguration(BaseModel):
    """A reviewing team, and file patterns describing which files they must approve changes to."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    file_patterns: list[str]
    minimum_approvals: int
    reviewer: RepositoryRuleParamsReviewer


class RepositoryRuleRequiredStatusChecksParameters(BaseModel):
    """RepositoryRuleRequiredStatusChecksParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    do_not_enforce_on_create: bool | None = None
    required_status_checks: list[RepositoryRuleParamsStatusCheckConfiguration]
    strict_required_status_checks_policy: bool


class RepositoryRuleWorkflowsParameters(BaseModel):
    """RepositoryRuleWorkflowsParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    do_not_enforce_on_create: bool | None = None
    workflows: list[RepositoryRuleParamsWorkflowFileReference]


class SecretScanningLocation(BaseModel):
    """SecretScanningLocation."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: (
        Literal[
            "commit",
            "wiki_commit",
            "issue_title",
            "issue_body",
            "issue_comment",
            "discussion_title",
            "discussion_body",
            "discussion_comment",
            "pull_request_title",
            "pull_request_body",
            "pull_request_comment",
            "pull_request_review",
            "pull_request_review_comment",
        ]
        | None
    ) = None
    details: (
        SecretScanningLocationCommit
        | SecretScanningLocationDiscussionBody
        | SecretScanningLocationDiscussionComment
        | SecretScanningLocationDiscussionTitle
        | SecretScanningLocationIssueBody
        | SecretScanningLocationIssueComment
        | SecretScanningLocationIssueTitle
        | SecretScanningLocationPullRequestBody
        | SecretScanningLocationPullRequestComment
        | SecretScanningLocationPullRequestReviewComment
        | SecretScanningLocationPullRequestReview
        | SecretScanningLocationPullRequestTitle
        | SecretScanningLocationWikiCommit
        | None
    ) = None


class MergeGroup(BaseModel):
    """A group of pull requests that the merge queue has grouped together to be merged."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    head_sha: str
    head_ref: str
    base_sha: str
    base_ref: str
    head_commit: SimpleCommit


class CodeScanningAlertAppearedInBranchPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignees: list[User] | None = None
    created_at: str
    dismissed_at: None | str
    dismissed_by: Any | None
    dismissed_comment: None | str = None
    dismissed_reason: Literal["false positive", "won't fix", "used in tests"] | None
    fixed_at: None = None
    html_url: str
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertAppearedInBranchPayloadAlertRule
    state: Literal["open", "dismissed", "fixed"] | None
    tool: CodeScanningAlertAppearedInBranchPayloadAlertTool
    url: str


class CodeScanningAlertClosedByUserPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignees: list[User] | None = None
    created_at: str
    dismissed_at: str
    dismissed_by: Any | None
    dismissed_comment: None | str = None
    dismissed_reason: Literal["false positive", "won't fix", "used in tests"] | None
    fixed_at: None = None
    html_url: str
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertClosedByUserPayloadAlertRule
    state: Literal["dismissed", "fixed"]
    tool: CodeScanningAlertClosedByUserPayloadAlertTool
    url: str
    dismissal_approved_by: Any | None = None


class CodeScanningAlertCreatedPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: None | str
    dismissed_at: None
    dismissed_by: None
    dismissed_comment: None | str = None
    dismissed_reason: None
    fixed_at: None = None
    html_url: str
    instances_url: str | None = None
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertCreatedPayloadAlertRule
    state: Literal["open", "dismissed"] | None
    tool: Any | None
    updated_at: None | str = None
    url: str
    dismissal_approved_by: None = None
    assignees: list[User] | None = None


class CodeScanningAlertFixedPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignees: list[User] | None = None
    created_at: str
    dismissed_at: None | str
    dismissed_by: Any | None
    dismissed_comment: None | str = None
    dismissed_reason: Literal["false positive", "won't fix", "used in tests"] | None
    fixed_at: None = None
    html_url: str
    instances_url: str | None = None
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertFixedPayloadAlertRule
    state: Literal["fixed"] | None
    tool: CodeScanningAlertFixedPayloadAlertTool
    url: str


class CodeScanningAlertReopenedByUserPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignees: list[User] | None = None
    created_at: str
    dismissed_at: None
    dismissed_by: None
    dismissed_comment: None | str = None
    dismissed_reason: None
    fixed_at: None = None
    html_url: str
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertReopenedByUserPayloadAlertRule
    state: Literal["open", "fixed"] | None
    tool: CodeScanningAlertReopenedByUserPayloadAlertTool
    url: str


class CodeScanningAlertReopenedPayloadAlert(BaseModel):
    """The code scanning alert involved in the event."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignees: list[User] | None = None
    created_at: str
    dismissed_at: None | str
    dismissed_by: Any | None
    dismissed_comment: None | str = None
    dismissed_reason: None | str
    fixed_at: None = None
    html_url: str
    instances_url: str | None = None
    most_recent_instance: Any | None = None
    number: int
    rule: CodeScanningAlertReopenedPayloadAlertRule
    state: Literal["open", "dismissed", "fixed"] | None
    tool: CodeScanningAlertReopenedPayloadAlertTool
    updated_at: None | str = None
    url: str
    dismissal_approved_by: None = None


class Deployment(BaseModel):
    """A request for a specific ref(branch,sha,tag) to be deployed."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    id: int
    node_id: str
    sha: str
    ref: str
    task: str
    payload: dict[str, Any] | str
    original_environment: str | None = None
    environment: str
    description: None | str
    creator: None | User
    created_at: str
    updated_at: str
    statuses_url: str
    repository_url: str
    transient_environment: bool | None = None
    production_environment: bool | None = None
    performed_via_github_app: Any | None = None


class Installation2(BaseModel):
    """Installation."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    account: Enterprise2 | User
    repository_selection: Literal["all", "selected"]
    access_tokens_url: str
    repositories_url: str
    html_url: str
    app_id: int
    client_id: str | None = None
    target_id: int
    target_type: str
    permissions: AppPermissions
    events: list[str]
    created_at: str
    updated_at: str
    single_file_name: None | str
    has_multiple_single_files: bool | None = None
    single_file_paths: list[str] | None = None
    app_slug: str
    suspended_by: None | User
    suspended_at: None | str
    contact_email: None | str = None


class Milestone(BaseModel):
    """A collection of related issues and pull requests."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    html_url: str
    labels_url: str
    id: int
    node_id: str
    number: int
    state: Literal["open", "closed"]
    title: str
    description: None | str
    creator: None | User
    open_issues: int
    closed_issues: int
    created_at: str
    updated_at: str
    closed_at: None | str
    due_on: None | str


class MinimalRepository(BaseModel):
    """Minimal Repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    name: str
    full_name: str
    owner: User
    private: bool
    html_url: str
    description: None | str
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str | None = None
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str | None = None
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str | None = None
    mirror_url: None | str = None
    hooks_url: str
    svn_url: str | None = None
    homepage: None | str = None
    language: None | str = None
    forks_count: int | None = None
    stargazers_count: int | None = None
    watchers_count: int | None = None
    size: int | None = None
    default_branch: str | None = None
    open_issues_count: int | None = None
    is_template: bool | None = None
    topics: list[str] | None = None
    has_issues: bool | None = None
    has_projects: bool | None = None
    has_wiki: bool | None = None
    has_pages: bool | None = None
    has_downloads: bool | None = None
    has_discussions: bool | None = None
    archived: bool | None = None
    disabled: bool | None = None
    visibility: str | None = None
    pushed_at: None | str = None
    created_at: None | str = None
    updated_at: None | str = None
    permissions: MinimalRepositoryPermissions | None = None
    role_name: str | None = None
    temp_clone_token: str | None = None
    delete_branch_on_merge: bool | None = None
    subscribers_count: int | None = None
    network_count: int | None = None
    code_of_conduct: CodeOfConduct | None = None
    license: Any | None = None
    forks: int | None = None
    open_issues: int | None = None
    watchers: int | None = None
    allow_forking: bool | None = None
    web_commit_signoff_required: bool | None = None
    security_and_analysis: Any | None = None
    custom_properties: dict[str, Any] | None = None


class PersonalAccessTokenRequest(BaseModel):
    """Details of a Personal Access Token Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    owner: User
    permissions_added: PersonalAccessTokenRequestPermissionsAdded
    permissions_upgraded: PersonalAccessTokenRequestPermissionsUpgraded
    permissions_result: PersonalAccessTokenRequestPermissionsResult
    repository_selection: Literal["none", "all", "subset"]
    repository_count: None | int
    repositories: Any | None
    created_at: str
    token_id: int
    token_name: str
    token_expired: bool
    token_expires_at: None | str
    token_last_used_at: None | str


class ProjectsV2Item(BaseModel):
    """An item belonging to a project."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: float
    node_id: str | None = None
    project_node_id: str | None = None
    content_node_id: str
    content_type: Literal["Issue", "PullRequest", "DraftIssue"]
    creator: User | None = None
    created_at: str
    updated_at: str
    archived_at: None | str


class ProjectsV2StatusUpdate(BaseModel):
    """An status update belonging to a project."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: float
    node_id: str
    project_node_id: str | None = None
    creator: User | None = None
    created_at: str
    updated_at: str
    status: Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None = None
    start_date: str | None = None
    target_date: str | None = None
    body: None | str = None


class Repository2(BaseModel):
    """A repository on GitHub."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    name: str
    full_name: str
    license: LicenseSimple | None
    forks: int
    permissions: Repository2Permissions | None = None
    owner: User
    private: bool
    html_url: str
    description: None | str
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: None | str
    hooks_url: str
    svn_url: str
    homepage: None | str
    language: None | str
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: bool | None = None
    topics: list[str] | None = None
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    has_discussions: bool | None = None
    archived: bool
    disabled: bool
    visibility: str | None = None
    pushed_at: None | str
    created_at: None | str
    updated_at: None | str
    allow_rebase_merge: bool | None = None
    temp_clone_token: str | None = None
    allow_squash_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    allow_update_branch: bool | None = None
    use_squash_pr_title_as_default: bool | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    allow_merge_commit: bool | None = None
    allow_forking: bool | None = None
    web_commit_signoff_required: bool | None = None
    open_issues: int
    watchers: int
    master_branch: str | None = None
    starred_at: str | None = None
    anonymous_access_enabled: bool | None = None
    code_search_index_status: Repository2CodeSearchIndexStatus | None = None


class Repository(BaseModel):
    """The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property when the event occurs from activity in a repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    name: str
    full_name: str
    license: LicenseSimple | None
    organization: None | User = None
    forks: int
    permissions: RepositoryPermissions | None = None
    owner: User
    private: bool
    html_url: str
    description: None | str
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: None | str
    hooks_url: str
    svn_url: str
    homepage: None | str
    language: None | str
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: bool | None = None
    topics: list[str] | None = None
    custom_properties: dict[str, Any] | None = None
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    has_discussions: bool | None = None
    archived: bool
    disabled: bool
    visibility: str | None = None
    pushed_at: None | str
    created_at: None | str
    updated_at: None | str
    allow_rebase_merge: bool | None = None
    template_repository: Any | None = None
    temp_clone_token: str | None = None
    allow_squash_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    allow_update_branch: bool | None = None
    use_squash_pr_title_as_default: bool | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    allow_merge_commit: bool | None = None
    allow_forking: bool | None = None
    web_commit_signoff_required: bool | None = None
    subscribers_count: int | None = None
    network_count: int | None = None
    open_issues: int
    watchers: int
    master_branch: str | None = None
    starred_at: str | None = None
    anonymous_access_enabled: bool | None = None


class SecretScanningAlertWebhook(BaseModel):
    """SecretScanningAlertWebhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number: int | None = None
    created_at: str | None = None
    updated_at: None | str = None
    url: str | None = None
    html_url: str | None = None
    locations_url: str | None = None
    resolution: (
        Literal["false_positive", "wont_fix", "revoked", "used_in_tests", "pattern_deleted", "pattern_edited"] | None
    ) = None
    resolved_at: None | str = None
    resolved_by: None | User = None
    resolution_comment: None | str = None
    secret_type: str | None = None
    secret_type_display_name: str | None = None
    validity: Literal["active", "inactive", "unknown"] | None = None
    push_protection_bypassed: None | bool = None
    push_protection_bypassed_by: None | User = None
    push_protection_bypassed_at: None | str = None
    push_protection_bypass_request_reviewer: None | User = None
    push_protection_bypass_request_reviewer_comment: None | str = None
    push_protection_bypass_request_comment: None | str = None
    push_protection_bypass_request_html_url: None | str = None
    publicly_leaked: None | bool = None
    multi_repo: None | bool = None
    assigned_to: None | User = None


class CustomPropertyCreatedPayload(BaseModel):
    """Payload for the GitHub `custom_property` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    definition: CustomProperty
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    sender: User | None = None


class CustomPropertyDeletedPayload(BaseModel):
    """Payload for the GitHub `custom_property` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    definition: CustomPropertyDeletedPayloadDefinition
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    sender: User | None = None


class CustomPropertyPromoteToEnterprisePayload(BaseModel):
    """Payload for the GitHub `custom_property` webhook with action `promote_to_enterprise`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["promote_to_enterprise"]
    definition: CustomProperty
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    sender: User | None = None


class CustomPropertyUpdatedPayload(BaseModel):
    """Payload for the GitHub `custom_property` webhook with action `updated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["updated"]
    definition: CustomProperty
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    sender: User | None = None


class GithubAppAuthorizationRevokedPayload(BaseModel):
    """Payload for the GitHub `github_app_authorization` webhook with action `revoked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["revoked"]
    sender: User


class IssuesDeletedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[IssuesDeletedPayloadIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesDeletedPayloadIssuePullRequest | None = None
    reactions: IssuesDeletedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class IssuesDemilestonedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[Any | None] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesDemilestonedPayloadIssuePullRequest | None = None
    reactions: IssuesDemilestonedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class IssuesEditedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[IssuesEditedPayloadIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesEditedPayloadIssuePullRequest | None = None
    reactions: IssuesEditedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    type: Any | None = None
    title: str
    updated_at: str
    url: str
    user: Any | None


class IssuesLabeledPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[IssuesLabeledPayloadIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesLabeledPayloadIssuePullRequest | None = None
    reactions: IssuesLabeledPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    type: Any | None = None
    title: str
    updated_at: str
    url: str
    user: Any | None


class IssuesLockedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[Any | None] | None = None
    labels_url: str
    locked: Literal[True]
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesLockedPayloadIssuePullRequest | None = None
    reactions: IssuesLockedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    type: Any | None = None
    title: str
    updated_at: str
    url: str
    user: Any | None


class IssuesMilestonedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[Any | None] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesMilestonedPayloadIssuePullRequest | None = None
    reactions: IssuesMilestonedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class IssuesOpenedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[IssuesOpenedPayloadIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesOpenedPayloadIssuePullRequest | None = None
    reactions: IssuesOpenedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class IssuesReopenedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[Any | None] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesReopenedPayloadIssuePullRequest | None = None
    reactions: IssuesReopenedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"]
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    updated_at: str
    url: str
    user: Any | None
    type: Any | None = None


class IssuesTransferredPayloadChangesNewIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[IssuesTransferredPayloadChangesNewIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesTransferredPayloadChangesNewIssuePullRequest | None = None
    reactions: IssuesTransferredPayloadChangesNewIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class IssuesUnlockedPayloadIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[Any | None] | None = None
    labels_url: str
    locked: Literal[False]
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: IssuesUnlockedPayloadIssuePullRequest | None = None
    reactions: IssuesUnlockedPayloadIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class WebhooksIssue(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[WebhooksIssueLabel] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: WebhooksIssuePullRequest | None = None
    reactions: WebhooksIssueReactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class WebhooksIssue2(BaseModel):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None = None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    closed_at: None | str
    comments: int
    comments_url: str
    created_at: str
    draft: bool | None = None
    events_url: str
    html_url: str
    id: int
    labels: list[WebhooksIssue2Label] | None = None
    labels_url: str
    locked: bool | None = None
    milestone: Any | None
    node_id: str
    number: int
    performed_via_github_app: Any | None = None
    pull_request: WebhooksIssue2PullRequest | None = None
    reactions: WebhooksIssue2Reactions
    repository_url: str
    sub_issues_summary: SubIssuesSummary | None = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None
    state: Literal["open", "closed"] | None = None
    state_reason: None | str = None
    timeline_url: str | None = None
    title: str
    type: Any | None = None
    updated_at: str
    url: str
    user: Any | None


class CheckSuiteCompletedPayloadCheckSuitePullRequest(BaseModel):
    """Check Run Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: CheckSuiteCompletedPayloadCheckSuitePullRequestBase
    head: CheckSuiteCompletedPayloadCheckSuitePullRequestHead
    id: int
    number: int
    url: str


class CheckSuiteRequestedPayloadCheckSuitePullRequest(BaseModel):
    """Check Run Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: CheckSuiteRequestedPayloadCheckSuitePullRequestBase
    head: CheckSuiteRequestedPayloadCheckSuitePullRequestHead
    id: int
    number: int
    url: str


class CheckSuiteRerequestedPayloadCheckSuitePullRequest(BaseModel):
    """Check Run Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: CheckSuiteRerequestedPayloadCheckSuitePullRequestBase
    head: CheckSuiteRerequestedPayloadCheckSuitePullRequestHead
    id: int
    number: int
    url: str


class DiscussionCategoryChangedPayloadChanges(BaseModel):
    """DiscussionCategoryChangedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    category: DiscussionCategoryChangedPayloadChangesCategory


class IssuesOpenedPayloadChanges(BaseModel):
    """IssuesOpenedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    old_issue: Any | None
    old_repository: IssuesOpenedPayloadChangesOldRepository


class PullRequestAssignedPayloadPullRequestBase(BaseModel):
    """PullRequestAssignedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestAssignedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestAutoMergeDisabledPayloadPullRequestBase(BaseModel):
    """PullRequestAutoMergeDisabledPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestAutoMergeDisabledPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestAutoMergeDisabledPayloadPullRequestHead(BaseModel):
    """PullRequestAutoMergeDisabledPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestAutoMergeDisabledPayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestAutoMergeEnabledPayloadPullRequestBase(BaseModel):
    """PullRequestAutoMergeEnabledPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestAutoMergeEnabledPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestAutoMergeEnabledPayloadPullRequestHead(BaseModel):
    """PullRequestAutoMergeEnabledPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestAutoMergeEnabledPayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestDequeuedPayloadPullRequestBase(BaseModel):
    """PullRequestDequeuedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestDequeuedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestDequeuedPayloadPullRequestHead(BaseModel):
    """PullRequestDequeuedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestDequeuedPayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestEditedPayloadChanges(BaseModel):
    """The changes to the comment if the action was `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: PullRequestEditedPayloadChangesBase | None = None
    body: PullRequestEditedPayloadChangesBody | None = None
    title: PullRequestEditedPayloadChangesTitle | None = None


class PullRequestEnqueuedPayloadPullRequestBase(BaseModel):
    """PullRequestEnqueuedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestEnqueuedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestEnqueuedPayloadPullRequestHead(BaseModel):
    """PullRequestEnqueuedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestEnqueuedPayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestLabeledPayloadPullRequestBase(BaseModel):
    """PullRequestLabeledPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestLabeledPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestLockedPayloadPullRequestBase(BaseModel):
    """PullRequestLockedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestLockedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestMinimal(BaseModel):
    """Pull Request Minimal."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    number: int
    url: str
    head: PullRequestMinimalHead
    base: PullRequestMinimalBase


class PullRequestReviewCommentCreatedPayloadComment(BaseModel):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewCommentCreatedPayloadCommentLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    commit_id: str
    created_at: str
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: int | None = None
    line: None | int
    node_id: str
    original_commit_id: str
    original_line: None | int
    original_position: int
    original_start_line: None | int
    path: str
    position: None | int
    pull_request_review_id: None | int
    pull_request_url: str
    reactions: PullRequestReviewCommentCreatedPayloadCommentReactions
    side: Literal["LEFT", "RIGHT"]
    start_line: None | int
    start_side: Literal["LEFT", "RIGHT"] | None
    subject_type: Literal["line", "file"] | None = None
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewCommentCreatedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewCommentCreatedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewCommentCreatedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewCommentDeletedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewCommentDeletedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewCommentDeletedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewCommentEditedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewCommentEditedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewCommentEditedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewDismissedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewDismissedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewDismissedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewDismissedPayloadReview(BaseModel):
    """The review that was affected."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewDismissedPayloadReviewLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    commit_id: str
    html_url: str
    id: int
    node_id: str
    pull_request_url: str
    state: Literal["dismissed", "approved", "changes_requested"]
    submitted_at: str
    updated_at: None | str = None
    user: Any | None


class PullRequestReviewEditedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewEditedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewEditedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewSubmittedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewSubmittedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewSubmittedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewThreadResolvedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewThreadResolvedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewThreadResolvedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewThreadResolvedPayloadThreadComment(BaseModel):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewThreadResolvedPayloadThreadCommentLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    commit_id: str
    created_at: str
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: int | None = None
    line: None | int
    node_id: str
    original_commit_id: str
    original_line: None | int
    original_position: int
    original_start_line: None | int
    path: str
    position: None | int
    pull_request_review_id: None | int
    pull_request_url: str
    reactions: PullRequestReviewThreadResolvedPayloadThreadCommentReactions
    side: Literal["LEFT", "RIGHT"]
    start_line: None | int
    start_side: Literal["LEFT", "RIGHT"] | None
    subject_type: Literal["line", "file"] | None = None
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewThreadUnresolvedPayloadPullRequestBase(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestReviewThreadUnresolvedPayloadPullRequestHead(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestReviewThreadUnresolvedPayloadThreadComment(BaseModel):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewThreadUnresolvedPayloadThreadCommentLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    commit_id: str
    created_at: str
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: int | None = None
    line: None | int
    node_id: str
    original_commit_id: str
    original_line: int
    original_position: int
    original_start_line: None | int
    path: str
    position: None | int
    pull_request_review_id: None | int
    pull_request_url: str
    reactions: PullRequestReviewThreadUnresolvedPayloadThreadCommentReactions
    side: Literal["LEFT", "RIGHT"]
    start_line: None | int
    start_side: Literal["LEFT", "RIGHT"] | None
    subject_type: Literal["line", "file"] | None = None
    updated_at: str
    url: str
    user: Any | None


class PullRequestSynchronizePayloadPullRequestBase(BaseModel):
    """PullRequestSynchronizePayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestSynchronizePayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestSynchronizePayloadPullRequestHead(BaseModel):
    """PullRequestSynchronizePayloadPullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestSynchronizePayloadPullRequestHeadRepo
    sha: str
    user: Any | None


class PullRequestUnassignedPayloadPullRequestBase(BaseModel):
    """PullRequestUnassignedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: None | str
    ref: str
    repo: PullRequestUnassignedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestUnlabeledPayloadPullRequestBase(BaseModel):
    """PullRequestUnlabeledPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestUnlabeledPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PullRequestUnlockedPayloadPullRequestBase(BaseModel):
    """PullRequestUnlockedPayloadPullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: PullRequestUnlockedPayloadPullRequestBaseRepo
    sha: str
    user: Any | None


class PushPayload(BaseModel):
    """Payload for the GitHub `push` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: str
    base_ref: None | str
    before: str
    commits: list[PushPayloadCommit]
    compare: str
    created: bool
    deleted: bool
    enterprise: Enterprise | None = None
    forced: bool
    head_commit: Any | None
    installation: Installation | None = None
    organization: Organization | None = None
    pusher: PushPayloadPusher
    ref: str
    repository: PushPayloadRepository
    sender: User | None = None


class RepositoryRenamedPayloadChanges(BaseModel):
    """RepositoryRenamedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    repository: RepositoryRenamedPayloadChangesRepository


class RepositoryRulesetEditedPayloadChangesConditionsUpdated(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdated."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    condition: RepositoryRulesetConditions | None = None
    changes: RepositoryRulesetEditedPayloadChangesConditionsUpdatedChanges | None = None


class RepositoryTransferredPayloadChangesOwner(BaseModel):
    """RepositoryTransferredPayloadChangesOwner."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: RepositoryTransferredPayloadChangesOwnerFrom = Field(alias="from")


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisory(BaseModel):
    """The details of the security advisory, including summary, description, and severity."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cvss: SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvss
    cvss_severities: Any | None = None
    cwes: list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCwe]
    description: str
    ghsa_id: str
    identifiers: list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifier]
    published_at: str
    references: list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReference]
    severity: str
    summary: str
    updated_at: str
    vulnerabilities: list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerability]
    withdrawn_at: str


class StatusPayloadCommit(BaseModel):
    """StatusPayloadCommit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: Any | None
    comments_url: str
    commit: StatusPayloadCommitCommit
    committer: Any | None
    html_url: str
    node_id: str
    parents: list[StatusPayloadCommitParent]
    sha: str
    url: str


class TeamAddedToRepositoryPayload(BaseModel):
    """Payload for the GitHub `team` webhook with action `added_to_repository`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["added_to_repository"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: TeamAddedToRepositoryPayloadRepository | None = None
    sender: User | None = None
    team: WebhooksTeam1


class TeamCreatedPayload(BaseModel):
    """Payload for the GitHub `team` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: TeamCreatedPayloadRepository | None = None
    sender: User
    team: WebhooksTeam1


class TeamDeletedPayload(BaseModel):
    """Payload for the GitHub `team` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: TeamDeletedPayloadRepository | None = None
    sender: User | None = None
    team: WebhooksTeam1


class TeamEditedPayloadChangesRepository(BaseModel):
    """TeamEditedPayloadChangesRepository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permissions: TeamEditedPayloadChangesRepositoryPermissions


class TeamRemovedFromRepositoryPayload(BaseModel):
    """Payload for the GitHub `team` webhook with action `removed_from_repository`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["removed_from_repository"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: TeamRemovedFromRepositoryPayloadRepository | None = None
    sender: User
    team: WebhooksTeam1


class PackageUpdatedPayloadPackagePackageVersion(BaseModel):
    """PackageUpdatedPayloadPackagePackageVersion."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: Any | None
    body: str
    body_html: str
    created_at: str
    description: str
    docker_metadata: list[PackageUpdatedPayloadPackagePackageVersionDockerMetadata] | None = None
    draft: bool | None = None
    html_url: str
    id: int
    installation_command: str
    manifest: str | None = None
    metadata: list[dict[str, Any]]
    name: str
    package_files: list[PackageUpdatedPayloadPackagePackageVersionPackageFile]
    package_url: str | None = None
    prerelease: bool | None = None
    release: PackageUpdatedPayloadPackagePackageVersionRelease | None = None
    rubygems_metadata: list[WebhookRubygemsMetadata] | None = None
    source_url: str | None = None
    summary: str
    tag_name: str | None = None
    target_commitish: str
    target_oid: str
    updated_at: str
    version: str


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersion(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersion."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthor
    body: str
    body_html: str
    created_at: str
    description: str
    docker_metadata: list[Any | None] | None = None
    draft: bool | None = None
    html_url: str
    id: int
    installation_command: str
    manifest: str | None = None
    metadata: list[dict[str, Any]]
    name: str
    package_files: list[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFile]
    package_url: str
    prerelease: bool | None = None
    release: RegistryPackageUpdatedPayloadRegistryPackagePackageVersionRelease | None = None
    rubygems_metadata: list[WebhookRubygemsMetadata] | None = None
    summary: str
    tag_name: str | None = None
    target_commitish: str
    target_oid: str
    updated_at: str
    version: str


class WebhooksChanges8(BaseModel):
    """WebhooksChanges8."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tier: WebhooksChanges8Tier


class WebhooksPullRequest5Base(BaseModel):
    """WebhooksPullRequest5Base."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: WebhooksPullRequest5BaseRepo
    sha: str
    user: Any | None


class WebhooksPullRequest5Head(BaseModel):
    """WebhooksPullRequest5Head."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: WebhooksPullRequest5HeadRepo
    sha: str
    user: Any | None


class WebhooksReviewComment(BaseModel):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: WebhooksReviewCommentLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: str
    commit_id: str
    created_at: str
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: int | None = None
    line: None | int
    node_id: str
    original_commit_id: str
    original_line: int
    original_position: int
    original_start_line: None | int
    path: str
    position: None | int
    pull_request_review_id: None | int
    pull_request_url: str
    reactions: WebhooksReviewCommentReactions
    side: Literal["LEFT", "RIGHT"]
    start_line: None | int
    start_side: Literal["LEFT", "RIGHT"] | None
    subject_type: Literal["line", "file"] | None = None
    updated_at: str
    url: str
    user: Any | None


class WebhooksReview(BaseModel):
    """The review that was affected."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: WebhooksReviewLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    body: None | str
    commit_id: str
    html_url: str
    id: int
    node_id: str
    pull_request_url: str
    state: str
    submitted_at: None | str
    updated_at: None | str = None
    user: Any | None


class WebhooksSecurityAdvisory(BaseModel):
    """The details of the security advisory, including summary, description, and severity."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cvss: WebhooksSecurityAdvisoryCvss
    cvss_severities: Any | None = None
    cwes: list[WebhooksSecurityAdvisoryCwe]
    description: str
    ghsa_id: str
    identifiers: list[WebhooksSecurityAdvisoryIdentifier]
    published_at: str
    references: list[WebhooksSecurityAdvisoryReference]
    severity: str
    summary: str
    updated_at: str
    vulnerabilities: list[WebhooksSecurityAdvisoryVulnerability]
    withdrawn_at: None | str


class WorkflowRunCompletedPayloadWorkflowRun(BaseModel):
    """Workflow Run."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Any | None = None
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: (
        Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
            "startup_failure",
        ]
        | None
    )
    created_at: str
    event: str
    head_branch: None | str
    head_commit: WorkflowRunCompletedPayloadWorkflowRunHeadCommit
    head_repository: WorkflowRunCompletedPayloadWorkflowRunHeadRepository
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: None | str
    node_id: str
    path: str | None = None
    previous_attempt_url: None | str
    pull_requests: list[Any | None]
    referenced_workflows: Any | None = None
    repository: WorkflowRunCompletedPayloadWorkflowRunRepository
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: str
    status: Literal["requested", "in_progress", "completed", "queued", "pending", "waiting"]
    triggering_actor: Any | None = None
    updated_at: str
    url: str
    workflow_id: int
    workflow_url: str
    display_title: str | None = None


class WorkflowRunInProgressPayloadWorkflowRun(BaseModel):
    """Workflow Run."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Any | None = None
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: (
        Literal["action_required", "cancelled", "failure", "neutral", "skipped", "stale", "success", "timed_out"] | None
    )
    created_at: str
    event: str
    head_branch: None | str
    head_commit: WorkflowRunInProgressPayloadWorkflowRunHeadCommit
    head_repository: WorkflowRunInProgressPayloadWorkflowRunHeadRepository
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: None | str
    node_id: str
    path: str | None = None
    previous_attempt_url: None | str
    pull_requests: list[Any | None]
    referenced_workflows: Any | None = None
    repository: WorkflowRunInProgressPayloadWorkflowRunRepository
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: str
    status: Literal["requested", "in_progress", "completed", "queued", "pending"]
    triggering_actor: Any | None = None
    updated_at: str
    url: str
    workflow_id: int
    workflow_url: str


class WorkflowRunRequestedPayloadWorkflowRunPullRequest(BaseModel):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: WorkflowRunRequestedPayloadWorkflowRunPullRequestBase
    head: WorkflowRunRequestedPayloadWorkflowRunPullRequestHead
    id: float
    number: float
    url: str


class DependabotAlertSecurityAdvisory(BaseModel):
    """Details for the GitHub Security Advisory."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ghsa_id: str
    cve_id: None | str
    summary: str
    description: str
    vulnerabilities: list[DependabotAlertSecurityVulnerability]
    severity: Literal["low", "medium", "high", "critical"]
    cvss: DependabotAlertSecurityAdvisoryCvss
    cvss_severities: Any | None = None
    epss: Any | None = None
    cwes: list[DependabotAlertSecurityAdvisoryCwe]
    identifiers: list[DependabotAlertSecurityAdvisoryIdentifier]
    references: list[DependabotAlertSecurityAdvisoryReference]
    published_at: str
    updated_at: str
    withdrawn_at: None | str


class ProjectsV2ItemEditedPayloadChangesOption1(BaseModel):
    """ProjectsV2ItemEditedPayloadChangesOption1."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_value: ProjectsV2ItemEditedPayloadChangesOption1FieldValue


class RepositoryRuleCodeScanning(BaseModel):
    """Choose which tools must provide code scanning results before the reference is updated. When configured, code scanning must be enabled and have results for both the commit and the reference being updated."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["code_scanning"]
    parameters: RepositoryRuleCodeScanningParameters | None = None


class RepositoryRulePullRequestParameters(BaseModel):
    """RepositoryRulePullRequestParameters."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allowed_merge_methods: list[Literal["merge", "squash", "rebase"]] | None = None
    automatic_copilot_code_review_enabled: bool | None = None
    dismiss_stale_reviews_on_push: bool
    require_code_owner_review: bool
    require_last_push_approval: bool
    required_approving_review_count: int
    required_review_thread_resolution: bool
    required_reviewers: list[RepositoryRuleParamsRequiredReviewerConfiguration] | None = None


class RepositoryRuleRequiredStatusChecks(BaseModel):
    """Choose which status checks must pass before the ref is updated. When enabled, commits must first be pushed to another ref where the checks pass."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["required_status_checks"]
    parameters: RepositoryRuleRequiredStatusChecksParameters | None = None


class RepositoryRuleWorkflows(BaseModel):
    """Require all changes made to a targeted branch to pass the specified workflows before they can be merged."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["workflows"]
    parameters: RepositoryRuleWorkflowsParameters | None = None


class PersonalAccessTokenRequestApprovedPayload(BaseModel):
    """Payload for the GitHub `personal_access_token_request` webhook with action `approved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["approved"]
    personal_access_token_request: PersonalAccessTokenRequest
    enterprise: Enterprise | None = None
    organization: Organization
    sender: User
    installation: Installation


class PersonalAccessTokenRequestCancelledPayload(BaseModel):
    """Payload for the GitHub `personal_access_token_request` webhook with action `cancelled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["cancelled"]
    personal_access_token_request: PersonalAccessTokenRequest
    enterprise: Enterprise | None = None
    organization: Organization
    sender: User
    installation: Installation


class PersonalAccessTokenRequestCreatedPayload(BaseModel):
    """Payload for the GitHub `personal_access_token_request` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    personal_access_token_request: PersonalAccessTokenRequest
    enterprise: Enterprise | None = None
    organization: Organization
    sender: User
    installation: Installation | None = None


class PersonalAccessTokenRequestDeniedPayload(BaseModel):
    """Payload for the GitHub `personal_access_token_request` webhook with action `denied`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["denied"]
    personal_access_token_request: PersonalAccessTokenRequest
    organization: Organization
    enterprise: Enterprise | None = None
    sender: User
    installation: Installation


class ProjectsV2ItemArchivedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `archived`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["archived"]
    changes: WebhooksProjectChanges
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2ItemConvertedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `converted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["converted"]
    changes: ProjectsV2ItemConvertedPayloadChanges
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2ItemCreatedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2ItemDeletedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2ItemReorderedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `reordered`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reordered"]
    changes: ProjectsV2ItemReorderedPayloadChanges
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2ItemRestoredPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `restored`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["restored"]
    changes: WebhooksProjectChanges
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class ProjectsV2(BaseModel):
    """A projects v2 project."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: float
    node_id: str
    owner: User
    creator: User
    title: str
    description: None | str
    public: bool
    closed_at: None | str
    created_at: str
    updated_at: str
    number: int
    short_description: None | str
    deleted_at: None | str
    deleted_by: None | User
    state: Literal["open", "closed"] | None = None
    latest_status_update: None | ProjectsV2StatusUpdate = None
    is_template: bool | None = None


class ProjectsV2StatusUpdateCreatedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    installation: Installation | None = None
    organization: Organization
    projects_v2_status_update: ProjectsV2StatusUpdate
    sender: User


class ProjectsV2StatusUpdateDeletedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    installation: Installation | None = None
    organization: Organization
    projects_v2_status_update: ProjectsV2StatusUpdate
    sender: User


class ProjectsV2StatusUpdateEditedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectsV2StatusUpdateEditedPayloadChanges | None = None
    installation: Installation | None = None
    organization: Organization
    projects_v2_status_update: ProjectsV2StatusUpdate
    sender: User


class PullRequestBase(BaseModel):
    """PullRequestBase."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Repository2
    sha: str
    user: User


class PullRequestHead(BaseModel):
    """PullRequestHead."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    ref: str
    repo: Repository2
    sha: str
    user: User


class FullRepository(BaseModel):
    """Full Repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    name: str
    full_name: str
    owner: User
    private: bool
    html_url: str
    description: None | str
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: None | str
    hooks_url: str
    svn_url: str
    homepage: None | str
    language: None | str
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: bool | None = None
    topics: list[str] | None = None
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool | None = None
    has_discussions: bool
    archived: bool
    disabled: bool
    visibility: str | None = None
    pushed_at: str
    created_at: str
    updated_at: str
    permissions: FullRepositoryPermissions | None = None
    allow_rebase_merge: bool | None = None
    template_repository: None | Repository2 = None
    temp_clone_token: None | str = None
    allow_squash_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    allow_merge_commit: bool | None = None
    allow_update_branch: bool | None = None
    use_squash_pr_title_as_default: bool | None = None
    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | None = None
    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | None = None
    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | None = None
    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | None = None
    allow_forking: bool | None = None
    web_commit_signoff_required: bool | None = None
    subscribers_count: int
    network_count: int
    license: LicenseSimple | None
    organization: None | User = None
    parent: Repository2 | None = None
    source: Repository2 | None = None
    forks: int
    master_branch: str | None = None
    open_issues: int
    watchers: int
    anonymous_access_enabled: bool | None = None
    code_of_conduct: CodeOfConductSimple | None = None
    security_and_analysis: Any | None = None
    custom_properties: dict[str, Any] | None = None


class Issue(BaseModel):
    """Issues are a great way to keep track of tasks, enhancements, and bugs for your projects."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    node_id: str
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    number: int
    state: str
    state_reason: Literal["completed", "reopened", "not_planned", "duplicate"] | None = None
    title: str
    body: None | str = None
    user: None | User
    labels: list[IssueLabelOption2 | str]
    assignee: None | User
    assignees: Any | None = None
    milestone: Milestone | None
    locked: bool
    active_lock_reason: None | str = None
    comments: int
    pull_request: IssuePullRequest | None = None
    closed_at: None | str
    created_at: str
    updated_at: str
    draft: bool | None = None
    closed_by: None | User = None
    body_html: str | None = None
    body_text: str | None = None
    timeline_url: str | None = None
    type: Any | None = None
    repository: Repository2 | None = None
    performed_via_github_app: Any | None = None
    author_association: (
        Literal[
            "COLLABORATOR",
            "CONTRIBUTOR",
            "FIRST_TIMER",
            "FIRST_TIME_CONTRIBUTOR",
            "MANNEQUIN",
            "MEMBER",
            "NONE",
            "OWNER",
        ]
        | None
    ) = None
    reactions: ReactionRollup | None = None
    sub_issues_summary: SubIssuesSummary | None = None
    parent_issue_url: None | str = None
    issue_dependencies_summary: IssueDependenciesSummary | None = None
    issue_field_values: list[IssueFieldValue] | None = None


class DiscussionTransferredPayloadChanges(BaseModel):
    """DiscussionTransferredPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_discussion: Discussion
    new_repository: Repository


class BranchProtectionConfigurationDisabledPayload(BaseModel):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `disabled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["disabled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class BranchProtectionConfigurationEnabledPayload(BaseModel):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `enabled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["enabled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class BranchProtectionRuleCreatedPayload(BaseModel):
    """Payload for the GitHub `branch_protection_rule` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    rule: WebhooksRule
    sender: User


class BranchProtectionRuleDeletedPayload(BaseModel):
    """Payload for the GitHub `branch_protection_rule` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    rule: WebhooksRule
    sender: User


class BranchProtectionRuleEditedPayload(BaseModel):
    """Payload for the GitHub `branch_protection_rule` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: BranchProtectionRuleEditedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    rule: WebhooksRule
    sender: User


class CodeScanningAlertAppearedInBranchPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `appeared_in_branch`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["appeared_in_branch"]
    alert: CodeScanningAlertAppearedInBranchPayloadAlert
    commit_oid: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User


class CodeScanningAlertClosedByUserPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `closed_by_user`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed_by_user"]
    alert: CodeScanningAlertClosedByUserPayloadAlert
    commit_oid: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User


class CodeScanningAlertCreatedPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    alert: CodeScanningAlertCreatedPayloadAlert
    commit_oid: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User


class CodeScanningAlertFixedPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `fixed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["fixed"]
    alert: CodeScanningAlertFixedPayloadAlert
    commit_oid: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User


class CodeScanningAlertReopenedPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    alert: CodeScanningAlertReopenedPayloadAlert
    commit_oid: None | str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: None | str
    repository: Repository
    sender: User


class CodeScanningAlertReopenedByUserPayload(BaseModel):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened_by_user`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened_by_user"]
    alert: CodeScanningAlertReopenedByUserPayloadAlert
    commit_oid: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User


class CommitCommentCreatedPayload(BaseModel):
    """Payload for the GitHub `commit_comment` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    comment: CommitCommentCreatedPayloadComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class CreatePayload(BaseModel):
    """Payload for the GitHub `create` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: None | str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    master_branch: str
    organization: Organization | None = None
    pusher_type: str
    ref: str
    ref_type: Literal["tag", "branch"]
    repository: Repository
    sender: User


class CustomPropertyValuesUpdatedPayload(BaseModel):
    """Payload for the GitHub `custom-property-values` webhook with action `updated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["updated"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    repository: Repository
    organization: Organization
    sender: User | None = None
    new_property_values: list[CustomPropertyValue]
    old_property_values: list[CustomPropertyValue]


class DeletePayload(BaseModel):
    """Payload for the GitHub `delete` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pusher_type: str
    ref: str
    ref_type: Literal["tag", "branch"]
    repository: Repository
    sender: User


class DeployKeyCreatedPayload(BaseModel):
    """Payload for the GitHub `deploy_key` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    key: WebhooksDeployKey
    organization: Organization | None = None
    repository: Repository
    sender: User


class DeployKeyDeletedPayload(BaseModel):
    """Payload for the GitHub `deploy_key` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    key: WebhooksDeployKey
    organization: Organization | None = None
    repository: Repository
    sender: User


class DeploymentCreatedPayload(BaseModel):
    """Payload for the GitHub `deployment` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    deployment: DeploymentCreatedPayloadDeployment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow: Any | None
    workflow_run: Any | None


class DeploymentReviewApprovedPayload(BaseModel):
    """Payload for the GitHub `deployment_review` webhook with action `approved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["approved"]
    approver: WebhooksApprover | None = None
    comment: str | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    reviewers: list[DeploymentReviewApprovedPayloadReviewer] | None = None
    sender: User
    since: str
    workflow_job_run: WebhooksWorkflowJobRun | None = None
    workflow_job_runs: list[DeploymentReviewApprovedPayloadWorkflowJobRun] | None = None
    workflow_run: Any | None


class DeploymentReviewRejectedPayload(BaseModel):
    """Payload for the GitHub `deployment_review` webhook with action `rejected`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["rejected"]
    approver: WebhooksApprover | None = None
    comment: str | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    reviewers: list[DeploymentReviewRejectedPayloadReviewer] | None = None
    sender: User
    since: str
    workflow_job_run: WebhooksWorkflowJobRun | None = None
    workflow_job_runs: list[DeploymentReviewRejectedPayloadWorkflowJobRun] | None = None
    workflow_run: Any | None


class DeploymentReviewRequestedPayload(BaseModel):
    """Payload for the GitHub `deployment_review` webhook with action `requested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["requested"]
    enterprise: Enterprise | None = None
    environment: str
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    requestor: Any | None
    reviewers: list[DeploymentReviewRequestedPayloadReviewer]
    sender: User
    since: str
    workflow_job_run: DeploymentReviewRequestedPayloadWorkflowJobRun
    workflow_run: Any | None


class DeploymentStatusCreatedPayload(BaseModel):
    """Payload for the GitHub `deployment_status` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    check_run: Any | None = None
    deployment: DeploymentStatusCreatedPayloadDeployment
    deployment_status: DeploymentStatusCreatedPayloadDeploymentStatus
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow: Any | None = None
    workflow_run: Any | None = None


class DiscussionAnsweredPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `answered`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["answered"]
    answer: WebhooksAnswer
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionClosedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionCommentCreatedPayload(BaseModel):
    """Payload for the GitHub `discussion_comment` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    comment: WebhooksComment
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionCommentDeletedPayload(BaseModel):
    """Payload for the GitHub `discussion_comment` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    comment: WebhooksComment
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionCommentEditedPayload(BaseModel):
    """Payload for the GitHub `discussion_comment` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: DiscussionCommentEditedPayloadChanges
    comment: WebhooksComment
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionCreatedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionDeletedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionEditedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: DiscussionEditedPayloadChanges | None = None
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionLabeledPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `labeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["labeled"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionLockedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `locked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["locked"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionPinnedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `pinned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pinned"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionReopenedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionUnansweredPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `unanswered`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unanswered"]
    discussion: Discussion
    old_answer: WebhooksAnswer
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class DiscussionUnlabeledPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `unlabeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlabeled"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionUnlockedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `unlocked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlocked"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class DiscussionUnpinnedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `unpinned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unpinned"]
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class ForkPayload(BaseModel):
    """Payload for the GitHub `fork` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    forkee: Any
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class GollumPayload(BaseModel):
    """Payload for the GitHub `gollum` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pages: list[GollumPayloadPage]
    repository: Repository
    sender: User


class InstallationCreatedPayload(BaseModel):
    """Payload for the GitHub `installation` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories: list[InstallationCreatedPayloadRepository] | None = None
    repository: Repository | None = None
    requester: Any | None = None
    sender: User


class InstallationDeletedPayload(BaseModel):
    """Payload for the GitHub `installation` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories: list[InstallationDeletedPayloadRepository] | None = None
    repository: Repository | None = None
    requester: None = None
    sender: User


class InstallationNewPermissionsAcceptedPayload(BaseModel):
    """Payload for the GitHub `installation` webhook with action `new_permissions_accepted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["new_permissions_accepted"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories: list[InstallationNewPermissionsAcceptedPayloadRepository] | None = None
    repository: Repository | None = None
    requester: None = None
    sender: User


class InstallationRepositoriesAddedPayload(BaseModel):
    """Payload for the GitHub `installation_repositories` webhook with action `added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["added"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories_added: list[InstallationRepositoriesAddedPayloadRepositoriesAdded]
    repositories_removed: list[InstallationRepositoriesAddedPayloadRepositoriesRemoved]
    repository: Repository | None = None
    repository_selection: Literal["all", "selected"]
    requester: Any | None
    sender: User


class InstallationRepositoriesRemovedPayload(BaseModel):
    """Payload for the GitHub `installation_repositories` webhook with action `removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["removed"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories_added: list[InstallationRepositoriesRemovedPayloadRepositoriesAdded]
    repositories_removed: list[InstallationRepositoriesRemovedPayloadRepositoriesRemoved]
    repository: Repository | None = None
    repository_selection: Literal["all", "selected"]
    requester: Any | None
    sender: User


class InstallationSuspendPayload(BaseModel):
    """Payload for the GitHub `installation` webhook with action `suspend`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["suspend"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories: list[InstallationSuspendPayloadRepository] | None = None
    repository: Repository | None = None
    requester: None = None
    sender: User


class InstallationTargetRenamedPayload(BaseModel):
    """Payload for the GitHub `installation_target` webhook with action `renamed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: InstallationTargetRenamedPayloadAccount
    action: Literal["renamed"]
    changes: InstallationTargetRenamedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None
    target_type: str


class InstallationUnsuspendPayload(BaseModel):
    """Payload for the GitHub `installation` webhook with action `unsuspend`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unsuspend"]
    enterprise: Enterprise | None = None
    installation: Installation2
    organization: Organization | None = None
    repositories: list[InstallationUnsuspendPayloadRepository] | None = None
    repository: Repository | None = None
    requester: None = None
    sender: User


class IssueCommentCreatedPayload(BaseModel):
    """Payload for the GitHub `issue_comment` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    comment: IssueCommentCreatedPayloadComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: Any
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssueCommentDeletedPayload(BaseModel):
    """Payload for the GitHub `issue_comment` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    comment: WebhooksIssueComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: Any
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssueCommentEditedPayload(BaseModel):
    """Payload for the GitHub `issue_comment` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: WebhooksChanges
    comment: WebhooksIssueComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: Any
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesClosedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: Any
    organization: Organization | None = None
    repository: Repository
    sender: User


class LabelCreatedPayload(BaseModel):
    """Payload for the GitHub `label` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class LabelDeletedPayload(BaseModel):
    """Payload for the GitHub `label` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel
    organization: Organization | None = None
    repository: Repository
    sender: User


class LabelEditedPayload(BaseModel):
    """Payload for the GitHub `label` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: LabelEditedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel
    organization: Organization | None = None
    repository: Repository
    sender: User


class MarketplacePurchaseCancelledPayload(BaseModel):
    """Payload for the GitHub `marketplace_purchase` webhook with action `cancelled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["cancelled"]
    effective_date: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    marketplace_purchase: WebhooksMarketplacePurchase
    organization: Organization | None = None
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase | None = None
    repository: Repository | None = None
    sender: User


class MarketplacePurchaseChangedPayload(BaseModel):
    """Payload for the GitHub `marketplace_purchase` webhook with action `changed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["changed"]
    effective_date: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    marketplace_purchase: WebhooksMarketplacePurchase
    organization: Organization | None = None
    previous_marketplace_purchase: MarketplacePurchaseChangedPayloadPreviousMarketplacePurchase | None = None
    repository: Repository | None = None
    sender: User


class MarketplacePurchasePendingChangePayload(BaseModel):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pending_change"]
    effective_date: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    marketplace_purchase: WebhooksMarketplacePurchase
    organization: Organization | None = None
    previous_marketplace_purchase: MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchase | None = None
    repository: Repository | None = None
    sender: User


class MarketplacePurchasePendingChangeCancelledPayload(BaseModel):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change_cancelled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pending_change_cancelled"]
    effective_date: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    marketplace_purchase: MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchase
    organization: Organization | None = None
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase | None = None
    repository: Repository | None = None
    sender: User


class MarketplacePurchasePurchasedPayload(BaseModel):
    """Payload for the GitHub `marketplace_purchase` webhook with action `purchased`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["purchased"]
    effective_date: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    marketplace_purchase: WebhooksMarketplacePurchase
    organization: Organization | None = None
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase | None = None
    repository: Repository | None = None
    sender: User


class MemberAddedPayload(BaseModel):
    """Payload for the GitHub `member` webhook with action `added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["added"]
    changes: MemberAddedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    member: Any | None
    organization: Organization | None = None
    repository: Repository
    sender: User


class MemberEditedPayload(BaseModel):
    """Payload for the GitHub `member` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: MemberEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    member: Any | None
    organization: Organization | None = None
    repository: Repository
    sender: User


class MemberRemovedPayload(BaseModel):
    """Payload for the GitHub `member` webhook with action `removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["removed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    member: Any | None
    organization: Organization | None = None
    repository: Repository
    sender: User


class MembershipAddedPayload(BaseModel):
    """Payload for the GitHub `membership` webhook with action `added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["added"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    member: Any | None
    organization: Organization
    repository: Repository | None = None
    scope: Literal["team"]
    sender: Any | None
    team: WebhooksTeam


class MembershipRemovedPayload(BaseModel):
    """Payload for the GitHub `membership` webhook with action `removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["removed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    member: Any | None
    organization: Organization
    repository: Repository | None = None
    scope: Literal["team", "organization"]
    sender: Any | None
    team: WebhooksTeam


class MergeGroupChecksRequestedPayload(BaseModel):
    """Payload for the GitHub `merge_group` webhook with action `checks_requested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["checks_requested"]
    installation: Installation | None = None
    merge_group: MergeGroup
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class MergeGroupDestroyedPayload(BaseModel):
    """Payload for the GitHub `merge_group` webhook with action `destroyed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["destroyed"]
    reason: Literal["merged", "invalidated", "dequeued"] | None = None
    installation: Installation | None = None
    merge_group: MergeGroup
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class MetaDeletedPayload(BaseModel):
    """Payload for the GitHub `meta` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    hook: MetaDeletedPayloadHook
    hook_id: int
    installation: Installation | None = None
    organization: Organization | None = None
    repository: None | Repository = None
    sender: User | None = None


class MilestoneClosedPayload(BaseModel):
    """Payload for the GitHub `milestone` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    installation: Installation | None = None
    milestone: MilestoneClosedPayloadMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class MilestoneCreatedPayload(BaseModel):
    """Payload for the GitHub `milestone` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    milestone: MilestoneCreatedPayloadMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class MilestoneDeletedPayload(BaseModel):
    """Payload for the GitHub `milestone` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    milestone: WebhooksMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class MilestoneEditedPayload(BaseModel):
    """Payload for the GitHub `milestone` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: MilestoneEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    milestone: WebhooksMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class MilestoneOpenedPayload(BaseModel):
    """Payload for the GitHub `milestone` webhook with action `opened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["opened"]
    installation: Installation | None = None
    milestone: MilestoneOpenedPayloadMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class OrgBlockBlockedPayload(BaseModel):
    """Payload for the GitHub `org_block` webhook with action `blocked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["blocked"]
    blocked_user: Any | None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: Repository | None = None
    sender: User


class OrgBlockUnblockedPayload(BaseModel):
    """Payload for the GitHub `org_block` webhook with action `unblocked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unblocked"]
    blocked_user: Any | None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: Repository | None = None
    sender: User


class OrganizationDeletedPayload(BaseModel):
    """Payload for the GitHub `organization` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    membership: WebhooksMembership | None = None
    organization: Organization
    repository: Repository | None = None
    sender: User


class OrganizationMemberAddedPayload(BaseModel):
    """Payload for the GitHub `organization` webhook with action `member_added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["member_added"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    membership: WebhooksMembership
    organization: Organization
    repository: Repository | None = None
    sender: User


class OrganizationMemberInvitedPayload(BaseModel):
    """Payload for the GitHub `organization` webhook with action `member_invited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["member_invited"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    invitation: OrganizationMemberInvitedPayloadInvitation
    organization: Organization
    repository: Repository | None = None
    sender: User
    user: Any | None = None


class OrganizationMemberRemovedPayload(BaseModel):
    """Payload for the GitHub `organization` webhook with action `member_removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["member_removed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    membership: WebhooksMembership
    organization: Organization
    repository: Repository | None = None
    sender: User


class OrganizationRenamedPayload(BaseModel):
    """Payload for the GitHub `organization` webhook with action `renamed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["renamed"]
    changes: OrganizationRenamedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    membership: WebhooksMembership | None = None
    organization: Organization
    repository: Repository | None = None
    sender: User


class PackagePublishedPayload(BaseModel):
    """Payload for the GitHub `package` webhook with action `published`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["published"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    package: PackagePublishedPayloadPackage
    repository: Repository | None = None
    sender: User


class PageBuildPayload(BaseModel):
    """Payload for the GitHub `page_build` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    build: PageBuildPayloadBuild
    enterprise: Enterprise | None = None
    id: int
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class PingPayload(BaseModel):
    """Payload for the GitHub `ping` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hook: PingPayloadHook | None = None
    hook_id: int | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None
    zen: str | None = None


class ProjectCardConvertedPayload(BaseModel):
    """Payload for the GitHub `project_card` webhook with action `converted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["converted"]
    changes: ProjectCardConvertedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_card: WebhooksProjectCard
    repository: Repository | None = None
    sender: User


class ProjectCardCreatedPayload(BaseModel):
    """Payload for the GitHub `project_card` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_card: WebhooksProjectCard
    repository: Repository | None = None
    sender: User


class ProjectCardDeletedPayload(BaseModel):
    """Payload for the GitHub `project_card` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_card: ProjectCardDeletedPayloadProjectCard
    repository: None | Repository = None
    sender: User


class ProjectCardEditedPayload(BaseModel):
    """Payload for the GitHub `project_card` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectCardEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_card: WebhooksProjectCard
    repository: Repository | None = None
    sender: User


class ProjectCardMovedPayload(BaseModel):
    """Payload for the GitHub `project_card` webhook with action `moved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["moved"]
    changes: ProjectCardMovedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_card: Any
    repository: Repository | None = None
    sender: User


class ProjectClosedPayload(BaseModel):
    """Payload for the GitHub `project` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project: WebhooksProject
    repository: Repository | None = None
    sender: User


class ProjectColumnCreatedPayload(BaseModel):
    """Payload for the GitHub `project_column` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_column: WebhooksProjectColumn
    repository: Repository | None = None
    sender: User | None = None


class ProjectColumnDeletedPayload(BaseModel):
    """Payload for the GitHub `project_column` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_column: WebhooksProjectColumn
    repository: None | Repository = None
    sender: User | None = None


class ProjectColumnEditedPayload(BaseModel):
    """Payload for the GitHub `project_column` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectColumnEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_column: WebhooksProjectColumn
    repository: Repository | None = None
    sender: User | None = None


class ProjectColumnMovedPayload(BaseModel):
    """Payload for the GitHub `project_column` webhook with action `moved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["moved"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project_column: WebhooksProjectColumn
    repository: Repository | None = None
    sender: User


class ProjectCreatedPayload(BaseModel):
    """Payload for the GitHub `project` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project: WebhooksProject
    repository: Repository | None = None
    sender: User


class ProjectDeletedPayload(BaseModel):
    """Payload for the GitHub `project` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project: WebhooksProject
    repository: None | Repository = None
    sender: User | None = None


class ProjectEditedPayload(BaseModel):
    """Payload for the GitHub `project` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectEditedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project: WebhooksProject
    repository: Repository | None = None
    sender: User | None = None


class ProjectReopenedPayload(BaseModel):
    """Payload for the GitHub `project` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    project: WebhooksProject
    repository: Repository | None = None
    sender: User


class PublicPayload(BaseModel):
    """Payload for the GitHub `public` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class PullRequestClosedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User


class PullRequestConvertedToDraftPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `converted_to_draft`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["converted_to_draft"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User


class PullRequestOpenedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `opened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["opened"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User


class PullRequestReadyForReviewPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `ready_for_review`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["ready_for_review"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User


class PullRequestReopenedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User


class RegistryPackagePublishedPayload(BaseModel):
    """Payload for the GitHub `registry_package` webhook with action `published`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["published"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    registry_package: RegistryPackagePublishedPayloadRegistryPackage
    repository: Repository | None = None
    sender: User


class ReleaseCreatedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease
    repository: Repository
    sender: User


class ReleaseDeletedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease
    repository: Repository
    sender: User


class ReleaseEditedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ReleaseEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease
    repository: Repository
    sender: User | None = None


class ReleasePrereleasedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `prereleased`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["prereleased"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: ReleasePrereleasedPayloadRelease
    repository: Repository
    sender: User | None = None


class ReleasePublishedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `published`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["published"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease1
    repository: Repository
    sender: User | None = None


class ReleaseReleasedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `released`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["released"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease
    repository: Repository
    sender: User | None = None


class ReleaseUnpublishedPayload(BaseModel):
    """Payload for the GitHub `release` webhook with action `unpublished`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unpublished"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    release: WebhooksRelease1
    repository: Repository
    sender: User | None = None


class RepositoryAdvisoryPublishedPayload(BaseModel):
    """Payload for the GitHub `repository_advisory` webhook with action `published`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["published"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    repository_advisory: RepositoryAdvisory
    sender: User | None = None


class RepositoryAdvisoryReportedPayload(BaseModel):
    """Payload for the GitHub `repository_advisory` webhook with action `reported`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reported"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    repository_advisory: RepositoryAdvisory
    sender: User | None = None


class RepositoryArchivedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `archived`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["archived"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryCreatedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryDeletedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryDispatchPayload(BaseModel):
    """Payload for the GitHub `repository_dispatch` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: str
    branch: str
    client_payload: Any | None
    enterprise: Enterprise | None = None
    installation: Installation
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryEditedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: RepositoryEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryImportPayload(BaseModel):
    """Payload for the GitHub `repository_import` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    status: Literal["success", "cancelled", "failure"]


class RepositoryPrivatizedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `privatized`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["privatized"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryPublicizedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `publicized`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["publicized"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryUnarchivedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `unarchived`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unarchived"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryVulnerabilityAlertCreatePayload(BaseModel):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `create`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["create"]
    alert: WebhooksAlert
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryVulnerabilityAlertDismissPayload(BaseModel):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `dismiss`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["dismiss"]
    alert: RepositoryVulnerabilityAlertDismissPayloadAlert
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryVulnerabilityAlertReopenPayload(BaseModel):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `reopen`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopen"]
    alert: WebhooksAlert
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryVulnerabilityAlertResolvePayload(BaseModel):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `resolve`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["resolve"]
    alert: RepositoryVulnerabilityAlertResolvePayloadAlert
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class SecretScanningScanCompletedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_scan` webhook with action `completed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["completed"]
    type: Literal["backfill", "custom-pattern-backfill", "pattern-version-backfill"]
    source: Literal["git", "issues", "pull-requests", "discussions", "wiki"]
    started_at: str
    completed_at: str
    secret_types: Any | None = None
    custom_pattern_name: None | str = None
    custom_pattern_scope: Literal["repository", "organization", "enterprise"] | None = None
    repository: Repository | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    sender: User | None = None


class SponsorshipCancelledPayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `cancelled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["cancelled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class SponsorshipCreatedPayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class SponsorshipEditedPayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: SponsorshipEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class SponsorshipPendingCancellationPayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `pending_cancellation`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pending_cancellation"]
    effective_date: str | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class StarCreatedPayload(BaseModel):
    """Payload for the GitHub `star` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    starred_at: None | str


class StarDeletedPayload(BaseModel):
    """Payload for the GitHub `star` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    starred_at: None


class TeamAddPayload(BaseModel):
    """Payload for the GitHub `team_add` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    team: WebhooksTeam1


class WatchStartedPayload(BaseModel):
    """Payload for the GitHub `watch` webhook with action `started`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["started"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class WorkflowDispatchPayload(BaseModel):
    """Payload for the GitHub `workflow_dispatch` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enterprise: Enterprise | None = None
    inputs: Any | None
    installation: Installation | None = None
    organization: Organization | None = None
    ref: str
    repository: Repository
    sender: User
    workflow: str


class WorkflowJobCompletedPayload(BaseModel):
    """Payload for the GitHub `workflow_job` webhook with action `completed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["completed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow_job: Any
    deployment: Deployment | None = None


class WorkflowJobInProgressPayload(BaseModel):
    """Payload for the GitHub `workflow_job` webhook with action `in_progress`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["in_progress"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow_job: Any
    deployment: Deployment | None = None


class WorkflowJobQueuedPayload(BaseModel):
    """Payload for the GitHub `workflow_job` webhook with action `queued`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["queued"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow_job: WorkflowJobQueuedPayloadWorkflowJob
    deployment: Deployment | None = None


class WorkflowJobWaitingPayload(BaseModel):
    """Payload for the GitHub `workflow_job` webhook with action `waiting`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["waiting"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow_job: WorkflowJobWaitingPayloadWorkflowJob
    deployment: Deployment | None = None


class SecretScanningAlertAssignedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `assigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["assigned"]
    alert: SecretScanningAlertWebhook
    assignee: User | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertCreatedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    alert: SecretScanningAlertWebhook
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertLocationCreatedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert_location` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    alert: SecretScanningAlertWebhook
    installation: Installation | None = None
    location: SecretScanningLocation
    organization: Organization | None = None
    repository: Repository
    sender: User


class SecretScanningAlertPubliclyLeakedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `publicly_leaked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["publicly_leaked"]
    alert: SecretScanningAlertWebhook
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertReopenedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    alert: SecretScanningAlertWebhook
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertResolvedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `resolved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["resolved"]
    alert: SecretScanningAlertWebhook
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertUnassignedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `unassigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unassigned"]
    alert: SecretScanningAlertWebhook
    assignee: User | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class SecretScanningAlertValidatedPayload(BaseModel):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `validated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["validated"]
    alert: SecretScanningAlertWebhook
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User | None = None


class IssuesDeletedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesDeletedPayloadIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesDemilestonedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `demilestoned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["demilestoned"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesDemilestonedPayloadIssue
    milestone: WebhooksMilestone | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesEditedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: IssuesEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesEditedPayloadIssue
    label: WebhooksLabel | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesLabeledPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `labeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["labeled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesLabeledPayloadIssue
    label: WebhooksLabel | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesLockedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `locked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["locked"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesLockedPayloadIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesMilestonedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `milestoned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["milestoned"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesMilestonedPayloadIssue
    milestone: WebhooksMilestone
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesReopenedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesReopenedPayloadIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesTransferredPayloadChanges(BaseModel):
    """IssuesTransferredPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_issue: IssuesTransferredPayloadChangesNewIssue
    new_repository: IssuesTransferredPayloadChangesNewRepository


class IssuesUnlockedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `unlocked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlocked"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesUnlockedPayloadIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesAssignedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `assigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["assigned"]
    assignee: Any | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesTypedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `typed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["typed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue
    type: Any | None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesUnassignedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `unassigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unassigned"]
    assignee: Any | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesUnlabeledPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `unlabeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlabeled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue
    label: WebhooksLabel | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesUntypedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `untyped`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["untyped"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue
    type: Any | None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesPinnedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `pinned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pinned"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue2
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesUnpinnedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `unpinned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unpinned"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue2
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckSuiteCompletedPayloadCheckSuite(BaseModel):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: None | str
    app: CheckSuiteCompletedPayloadCheckSuiteApp
    before: None | str
    check_runs_url: str
    conclusion: (
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
            "startup_failure",
        ]
        | None
    )
    created_at: str
    head_branch: None | str
    head_commit: CheckSuiteCompletedPayloadCheckSuiteHeadCommit
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: list[CheckSuiteCompletedPayloadCheckSuitePullRequest]
    rerequestable: bool | None = None
    runs_rerequestable: bool | None = None
    status: Literal["requested", "in_progress", "completed", "queued", "pending"] | None
    updated_at: str
    url: str


class CheckSuiteRequestedPayloadCheckSuite(BaseModel):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: None | str
    app: CheckSuiteRequestedPayloadCheckSuiteApp
    before: None | str
    check_runs_url: str
    conclusion: (
        Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale", "skipped"] | None
    )
    created_at: str
    head_branch: None | str
    head_commit: CheckSuiteRequestedPayloadCheckSuiteHeadCommit
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: list[CheckSuiteRequestedPayloadCheckSuitePullRequest]
    rerequestable: bool | None = None
    runs_rerequestable: bool | None = None
    status: Literal["requested", "in_progress", "completed", "queued"] | None
    updated_at: str
    url: str


class CheckSuiteRerequestedPayloadCheckSuite(BaseModel):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: None | str
    app: CheckSuiteRerequestedPayloadCheckSuiteApp
    before: None | str
    check_runs_url: str
    conclusion: Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale"] | None
    created_at: str
    head_branch: None | str
    head_commit: CheckSuiteRerequestedPayloadCheckSuiteHeadCommit
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: list[CheckSuiteRerequestedPayloadCheckSuitePullRequest]
    rerequestable: bool | None = None
    runs_rerequestable: bool | None = None
    status: Literal["requested", "in_progress", "completed", "queued"] | None
    updated_at: str
    url: str


class DiscussionCategoryChangedPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `category_changed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["category_changed"]
    changes: DiscussionCategoryChangedPayloadChanges
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesOpenedPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `opened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["opened"]
    changes: IssuesOpenedPayloadChanges | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: IssuesOpenedPayloadIssue
    organization: Organization | None = None
    repository: Repository
    sender: User


class PullRequestAssignedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestAssignedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestAssignedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestAssignedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestAssignedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestAssignedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestAssignedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestAutoMergeDisabledPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestAutoMergeDisabledPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestAutoMergeDisabledPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestAutoMergeDisabledPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestAutoMergeDisabledPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestAutoMergeEnabledPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestAutoMergeEnabledPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestAutoMergeEnabledPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestAutoMergeEnabledPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestAutoMergeEnabledPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestDequeuedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestDequeuedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestDequeuedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestDequeuedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestDequeuedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestDequeuedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestEditedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: PullRequestEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: Any
    repository: Repository
    sender: User | None = None


class PullRequestEnqueuedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestEnqueuedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestEnqueuedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestEnqueuedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestEnqueuedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestEnqueuedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestLabeledPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestLabeledPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestLabeledPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestLabeledPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestLabeledPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestLabeledPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestLabeledPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestLockedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestLockedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestLockedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestLockedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestLockedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestLockedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestLockedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class SimpleCheckSuite(BaseModel):
    """A suite of checks performed on the code of a given code change."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: None | str = None
    app: Any | None = None
    before: None | str = None
    conclusion: (
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
            "stale",
            "startup_failure",
        ]
        | None
    ) = None
    created_at: str | None = None
    head_branch: None | str = None
    head_sha: str | None = None
    id: int | None = None
    node_id: str | None = None
    pull_requests: list[PullRequestMinimal] | None = None
    repository: MinimalRepository | None = None
    status: Literal["queued", "in_progress", "completed", "pending", "waiting"] | None = None
    updated_at: str | None = None
    url: str | None = None


class PullRequestReviewCommentCreatedPayloadPullRequest(BaseModel):
    """PullRequestReviewCommentCreatedPayloadPullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewCommentCreatedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None = None
    base: PullRequestReviewCommentCreatedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool | None = None
    head: PullRequestReviewCommentCreatedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewCommentCreatedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewCommentDeletedPayloadPullRequest(BaseModel):
    """PullRequestReviewCommentDeletedPayloadPullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewCommentDeletedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None = None
    base: PullRequestReviewCommentDeletedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool | None = None
    head: PullRequestReviewCommentDeletedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewCommentDeletedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewCommentEditedPayloadPullRequest(BaseModel):
    """PullRequestReviewCommentEditedPayloadPullRequest."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewCommentEditedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None = None
    base: PullRequestReviewCommentEditedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool | None = None
    head: PullRequestReviewCommentEditedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewCommentEditedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewCommentEditedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewDismissedPayloadPullRequest(BaseModel):
    """Simple Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewDismissedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestReviewDismissedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: PullRequestReviewDismissedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewDismissedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewDismissedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewEditedPayloadPullRequest(BaseModel):
    """Simple Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewEditedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestReviewEditedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: PullRequestReviewEditedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewEditedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewEditedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewSubmittedPayloadPullRequest(BaseModel):
    """Simple Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewSubmittedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestReviewSubmittedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: PullRequestReviewSubmittedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewSubmittedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewSubmittedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewThreadResolvedPayloadPullRequest(BaseModel):
    """Simple Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewThreadResolvedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestReviewThreadResolvedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: PullRequestReviewThreadResolvedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewThreadResolvedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewThreadResolvedPayloadThread(BaseModel):
    """PullRequestReviewThreadResolvedPayloadThread."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: list[PullRequestReviewThreadResolvedPayloadThreadComment]
    node_id: str


class PullRequestReviewThreadUnresolvedPayloadPullRequest(BaseModel):
    """Simple Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestReviewThreadUnresolvedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestReviewThreadUnresolvedPayloadPullRequestBase
    body: None | str
    closed_at: None | str
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: PullRequestReviewThreadUnresolvedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestReviewThreadUnresolvedPayloadPullRequestLabel]
    locked: bool
    merge_commit_sha: None | str
    merged_at: None | str
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: list[Any | None | PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestReviewThreadUnresolvedPayloadThread(BaseModel):
    """PullRequestReviewThreadUnresolvedPayloadThread."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: list[PullRequestReviewThreadUnresolvedPayloadThreadComment]
    node_id: str


class PullRequestSynchronizePayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestSynchronizePayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestSynchronizePayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestSynchronizePayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestSynchronizePayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestSynchronizePayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestUnassignedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestUnassignedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestUnassignedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestUnassignedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestUnassignedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestUnassignedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestUnlabeledPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestUnlabeledPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestUnlabeledPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestUnlabeledPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestUnlabeledPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestUnlabeledPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class PullRequestUnlockedPayloadPullRequest(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: PullRequestUnlockedPayloadPullRequestLinks
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: PullRequestUnlockedPayloadPullRequestBase
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: PullRequestUnlockedPayloadPullRequestHead
    html_url: str
    id: int
    issue_url: str
    labels: list[PullRequestUnlockedPayloadPullRequestLabel]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2]
    requested_teams: list[PullRequestUnlockedPayloadPullRequestRequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class RepositoryRenamedPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `renamed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["renamed"]
    changes: RepositoryRenamedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryRulesetEditedPayloadChangesConditions(BaseModel):
    """RepositoryRulesetEditedPayloadChangesConditions."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    added: list[RepositoryRulesetConditions] | None = None
    deleted: list[RepositoryRulesetConditions] | None = None
    updated: list[RepositoryRulesetEditedPayloadChangesConditionsUpdated] | None = None


class RepositoryTransferredPayloadChanges(BaseModel):
    """RepositoryTransferredPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    owner: RepositoryTransferredPayloadChangesOwner


class SecurityAdvisoryWithdrawnPayload(BaseModel):
    """Payload for the GitHub `security_advisory` webhook with action `withdrawn`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["withdrawn"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    security_advisory: SecurityAdvisoryWithdrawnPayloadSecurityAdvisory
    sender: User | None = None


class StatusPayload(BaseModel):
    """Payload for the GitHub `status` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: None | str = None
    branches: list[StatusPayloadBranche]
    commit: StatusPayloadCommit
    context: str
    created_at: str
    description: None | str
    enterprise: Enterprise | None = None
    id: int
    installation: Installation | None = None
    name: str
    organization: Organization | None = None
    repository: Repository
    sender: User
    sha: str
    state: Literal["pending", "success", "failure", "error"]
    target_url: None | str
    updated_at: str


class TeamEditedPayloadChanges(BaseModel):
    """The changes to the team if the action was `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: TeamEditedPayloadChangesDescription | None = None
    name: TeamEditedPayloadChangesName | None = None
    privacy: TeamEditedPayloadChangesPrivacy | None = None
    notification_setting: TeamEditedPayloadChangesNotificationSetting | None = None
    repository: TeamEditedPayloadChangesRepository | None = None


class PackageUpdatedPayloadPackage(BaseModel):
    """Information about the package."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: None | str
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Any | None
    package_type: str
    package_version: PackageUpdatedPayloadPackagePackageVersion
    registry: Any | None
    updated_at: str


class RegistryPackageUpdatedPayloadRegistryPackage(BaseModel):
    """RegistryPackageUpdatedPayloadRegistryPackage."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str
    description: None
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: RegistryPackageUpdatedPayloadRegistryPackageOwner
    package_type: str
    package_version: RegistryPackageUpdatedPayloadRegistryPackagePackageVersion
    registry: Any | None
    updated_at: str


class SponsorshipPendingTierChangePayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `pending_tier_change`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["pending_tier_change"]
    changes: WebhooksChanges8
    effective_date: str | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class SponsorshipTierChangedPayload(BaseModel):
    """Payload for the GitHub `sponsorship` webhook with action `tier_changed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["tier_changed"]
    changes: WebhooksChanges8
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User
    sponsorship: WebhooksSponsorship


class WebhooksPullRequest5(BaseModel):
    """Pull Request."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _links: WebhooksPullRequest5Links
    active_lock_reason: Literal["resolved", "off-topic", "too heated", "spam"] | None
    additions: int | None = None
    assignee: Any | None
    assignees: list[Any | None]
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    base: WebhooksPullRequest5Base
    body: None | str
    changed_files: int | None = None
    closed_at: None | str
    comments: int | None = None
    comments_url: str
    commits: int | None = None
    commits_url: str
    created_at: str
    deletions: int | None = None
    diff_url: str
    draft: bool
    head: WebhooksPullRequest5Head
    html_url: str
    id: int
    issue_url: str
    labels: list[WebhooksPullRequest5Label]
    locked: bool
    maintainer_can_modify: bool | None = None
    merge_commit_sha: None | str
    mergeable: None | bool = None
    mergeable_state: str | None = None
    merged: None | bool = None
    merged_at: None | str
    merged_by: Any | None = None
    milestone: Any | None
    node_id: str
    number: int
    patch_url: str
    rebaseable: None | bool = None
    requested_reviewers: list[Any | None | WebhooksPullRequest5RequestedReviewerOption2]
    requested_teams: list[WebhooksPullRequest5RequestedTeam]
    review_comment_url: str
    review_comments: int | None = None
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Any | None


class SecurityAdvisoryPublishedPayload(BaseModel):
    """Payload for the GitHub `security_advisory` webhook with action `published`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["published"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    security_advisory: WebhooksSecurityAdvisory
    sender: User | None = None


class SecurityAdvisoryUpdatedPayload(BaseModel):
    """Payload for the GitHub `security_advisory` webhook with action `updated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["updated"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    security_advisory: WebhooksSecurityAdvisory
    sender: User | None = None


class WorkflowRunCompletedPayload(BaseModel):
    """Payload for the GitHub `workflow_run` webhook with action `completed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["completed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow: Any | None
    workflow_run: WorkflowRunCompletedPayloadWorkflowRun


class WorkflowRunInProgressPayload(BaseModel):
    """Payload for the GitHub `workflow_run` webhook with action `in_progress`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["in_progress"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow: Any | None
    workflow_run: WorkflowRunInProgressPayloadWorkflowRun


class WorkflowRunRequestedPayloadWorkflowRun(BaseModel):
    """Workflow Run."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Any | None = None
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: (
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
            "startup_failure",
        ]
        | None
    )
    created_at: str
    event: str
    head_branch: None | str
    head_commit: WorkflowRunRequestedPayloadWorkflowRunHeadCommit
    head_repository: WorkflowRunRequestedPayloadWorkflowRunHeadRepository
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: None | str
    node_id: str
    path: str | None = None
    previous_attempt_url: None | str
    pull_requests: list[WorkflowRunRequestedPayloadWorkflowRunPullRequest]
    referenced_workflows: Any | None = None
    repository: WorkflowRunRequestedPayloadWorkflowRunRepository
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: str
    status: Literal["requested", "in_progress", "completed", "queued", "pending", "waiting"]
    triggering_actor: Any | None = None
    updated_at: str
    url: str
    workflow_id: int
    workflow_url: str
    display_title: str


class DependabotAlert(BaseModel):
    """A Dependabot alert."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number: int
    state: Literal["auto_dismissed", "dismissed", "fixed", "open"]
    dependency: DependabotAlertDependency
    security_advisory: DependabotAlertSecurityAdvisory
    security_vulnerability: DependabotAlertSecurityVulnerability
    url: str
    html_url: str
    created_at: str
    updated_at: str
    dismissed_at: None | str
    dismissed_by: None | User
    dismissed_reason: Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"] | None
    dismissed_comment: None | str
    fixed_at: None | str
    auto_dismissed_at: None | str = None


class ProjectsV2ItemEditedPayload(BaseModel):
    """Payload for the GitHub `projects_v2_item` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectsV2ItemEditedPayloadChangesOption1 | ProjectsV2ItemEditedPayloadChangesOption2 | None = None
    installation: Installation | None = None
    organization: Organization
    projects_v2_item: ProjectsV2Item
    sender: User


class RepositoryRulePullRequest(BaseModel):
    """Require all commits be made to a non-target branch and submitted via a pull request before they can be merged."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Literal["pull_request"]
    parameters: RepositoryRulePullRequestParameters | None = None


class ProjectsV2ClosedPayload(BaseModel):
    """Payload for the GitHub `projects_v2` webhook with action `closed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["closed"]
    installation: Installation | None = None
    organization: Organization
    projects_v2: ProjectsV2
    sender: User


class ProjectsV2CreatedPayload(BaseModel):
    """Payload for the GitHub `projects_v2` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    installation: Installation | None = None
    organization: Organization
    projects_v2: ProjectsV2
    sender: User


class ProjectsV2DeletedPayload(BaseModel):
    """Payload for the GitHub `projects_v2` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    installation: Installation | None = None
    organization: Organization
    projects_v2: ProjectsV2
    sender: User


class ProjectsV2EditedPayload(BaseModel):
    """Payload for the GitHub `projects_v2` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: ProjectsV2EditedPayloadChanges
    installation: Installation | None = None
    organization: Organization
    projects_v2: ProjectsV2
    sender: User


class ProjectsV2ReopenedPayload(BaseModel):
    """Payload for the GitHub `projects_v2` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    installation: Installation | None = None
    organization: Organization
    projects_v2: ProjectsV2
    sender: User


class PullRequest(BaseModel):
    """Pull requests let you tell others about changes you've pushed to a repository on GitHub. Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    number: int
    state: Literal["open", "closed"]
    locked: bool
    title: str
    user: User
    body: None | str
    labels: list[PullRequestLabel]
    milestone: Milestone | None
    active_lock_reason: None | str = None
    created_at: str
    updated_at: str
    closed_at: None | str
    merged_at: None | str
    merge_commit_sha: None | str
    assignee: None | User
    assignees: Any | None = None
    requested_reviewers: Any | None = None
    requested_teams: Any | None = None
    head: PullRequestHead
    base: PullRequestBase
    _links: PullRequestLinks
    author_association: Literal[
        "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
    ]
    auto_merge: Any | None
    draft: bool | None = None
    merged: bool
    mergeable: None | bool
    rebaseable: None | bool = None
    mergeable_state: str
    merged_by: None | User
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int


class SecurityAndAnalysisPayload(BaseModel):
    """Payload for the GitHub `security_and_analysis` webhook."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    changes: SecurityAndAnalysisPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: FullRepository
    sender: User | None = None


class IssueDependenciesBlockedByAddedPayload(BaseModel):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocked_by_added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["blocked_by_added"]
    blocked_issue_id: float
    blocked_issue: Issue
    blocking_issue_id: float
    blocking_issue: Issue
    blocking_issue_repo: Repository2
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    sender: User


class IssueDependenciesBlockedByRemovedPayload(BaseModel):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocked_by_removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["blocked_by_removed"]
    blocked_issue_id: float
    blocked_issue: Issue
    blocking_issue_id: float
    blocking_issue: Issue
    blocking_issue_repo: Repository2
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    sender: User


class IssueDependenciesBlockingAddedPayload(BaseModel):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocking_added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["blocking_added"]
    blocked_issue_id: float
    blocked_issue: Issue
    blocked_issue_repo: Repository2
    blocking_issue_id: float
    blocking_issue: Issue
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    sender: User


class IssueDependenciesBlockingRemovedPayload(BaseModel):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocking_removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["blocking_removed"]
    blocked_issue_id: float
    blocked_issue: Issue
    blocked_issue_repo: Repository2
    blocking_issue_id: float
    blocking_issue: Issue
    installation: Installation | None = None
    organization: Organization
    repository: Repository
    sender: User


class SubIssuesParentIssueAddedPayload(BaseModel):
    """Payload for the GitHub `sub-issues` webhook with action `parent_issue_added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["parent_issue_added"]
    parent_issue_id: float
    parent_issue: Issue
    parent_issue_repo: Repository2
    sub_issue_id: float
    sub_issue: Issue
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class SubIssuesParentIssueRemovedPayload(BaseModel):
    """Payload for the GitHub `sub-issues` webhook with action `parent_issue_removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["parent_issue_removed"]
    parent_issue_id: float
    parent_issue: Issue
    parent_issue_repo: Repository2
    sub_issue_id: float
    sub_issue: Issue
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class SubIssuesSubIssueAddedPayload(BaseModel):
    """Payload for the GitHub `sub-issues` webhook with action `sub_issue_added`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["sub_issue_added"]
    sub_issue_id: float
    sub_issue: Issue
    sub_issue_repo: Repository2
    parent_issue_id: float
    parent_issue: Issue
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class SubIssuesSubIssueRemovedPayload(BaseModel):
    """Payload for the GitHub `sub-issues` webhook with action `sub_issue_removed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["sub_issue_removed"]
    sub_issue_id: float
    sub_issue: Issue
    sub_issue_repo: Repository2
    parent_issue_id: float
    parent_issue: Issue
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    sender: User | None = None


class DiscussionTransferredPayload(BaseModel):
    """Payload for the GitHub `discussion` webhook with action `transferred`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["transferred"]
    changes: DiscussionTransferredPayloadChanges
    discussion: Discussion
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class IssuesTransferredPayload(BaseModel):
    """Payload for the GitHub `issues` webhook with action `transferred`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["transferred"]
    changes: IssuesTransferredPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    issue: WebhooksIssue2
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckSuiteCompletedPayload(BaseModel):
    """Payload for the GitHub `check_suite` webhook with action `completed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["completed"]
    check_suite: CheckSuiteCompletedPayloadCheckSuite
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckSuiteRequestedPayload(BaseModel):
    """Payload for the GitHub `check_suite` webhook with action `requested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["requested"]
    check_suite: CheckSuiteRequestedPayloadCheckSuite
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckSuiteRerequestedPayload(BaseModel):
    """Payload for the GitHub `check_suite` webhook with action `rerequested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["rerequested"]
    check_suite: CheckSuiteRerequestedPayloadCheckSuite
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class PullRequestAssignedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `assigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["assigned"]
    assignee: Any | None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestAssignedPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestAutoMergeDisabledPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_disabled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["auto_merge_disabled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestAutoMergeDisabledPayloadPullRequest
    reason: str
    repository: Repository
    sender: User


class PullRequestAutoMergeEnabledPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_enabled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["auto_merge_enabled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestAutoMergeEnabledPayloadPullRequest
    reason: str | None = None
    repository: Repository
    sender: User


class PullRequestDequeuedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `dequeued`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["dequeued"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestDequeuedPayloadPullRequest
    reason: Literal[
        "UNKNOWN_REMOVAL_REASON",
        "MANUAL",
        "MERGE",
        "MERGE_CONFLICT",
        "CI_FAILURE",
        "CI_TIMEOUT",
        "ALREADY_MERGED",
        "QUEUE_CLEARED",
        "ROLL_BACK",
        "BRANCH_PROTECTIONS",
        "GIT_TREE_INVALID",
        "INVALID_MERGE_COMMIT",
    ]
    repository: Repository
    sender: User


class PullRequestEnqueuedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `enqueued`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["enqueued"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestEnqueuedPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestLabeledPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `labeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["labeled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestLabeledPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestLockedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `locked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["locked"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestLockedPayloadPullRequest
    repository: Repository
    sender: User


class CheckRunWithSimpleCheckSuite(BaseModel):
    """A check performed on the code of a given code change."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    app: Any | None
    check_suite: SimpleCheckSuite
    completed_at: None | str
    conclusion: (
        Literal[
            "waiting",
            "pending",
            "startup_failure",
            "stale",
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
        ]
        | None
    )
    deployment: DeploymentSimple | None = None
    details_url: str
    external_id: str
    head_sha: str
    html_url: str
    id: int
    name: str
    node_id: str
    output: CheckRunWithSimpleCheckSuiteOutput
    pull_requests: list[PullRequestMinimal]
    started_at: str
    status: Literal["queued", "in_progress", "completed", "pending"]
    url: str


class PullRequestReviewCommentCreatedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    comment: PullRequestReviewCommentCreatedPayloadComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewCommentCreatedPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestReviewCommentDeletedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    comment: WebhooksReviewComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewCommentDeletedPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestReviewCommentEditedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: WebhooksChanges
    comment: WebhooksReviewComment
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewCommentEditedPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestReviewDismissedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review` webhook with action `dismissed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["dismissed"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewDismissedPayloadPullRequest
    repository: Repository
    review: PullRequestReviewDismissedPayloadReview
    sender: User


class PullRequestReviewEditedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: PullRequestReviewEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewEditedPayloadPullRequest
    repository: Repository
    review: WebhooksReview
    sender: User


class PullRequestReviewSubmittedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review` webhook with action `submitted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["submitted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewSubmittedPayloadPullRequest
    repository: Repository
    review: WebhooksReview
    sender: User


class PullRequestReviewThreadResolvedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `resolved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["resolved"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewThreadResolvedPayloadPullRequest
    repository: Repository
    sender: User | None = None
    thread: PullRequestReviewThreadResolvedPayloadThread
    updated_at: None | str = None


class PullRequestReviewThreadUnresolvedPayload(BaseModel):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `unresolved`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unresolved"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    pull_request: PullRequestReviewThreadUnresolvedPayloadPullRequest
    repository: Repository
    sender: User | None = None
    thread: PullRequestReviewThreadUnresolvedPayloadThread
    updated_at: None | str = None


class PullRequestSynchronizePayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `synchronize`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["synchronize"]
    after: str
    before: str
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestSynchronizePayloadPullRequest
    repository: Repository
    sender: User


class PullRequestUnassignedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `unassigned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unassigned"]
    assignee: Any | None = None
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestUnassignedPayloadPullRequest
    repository: Repository
    sender: User | None = None


class PullRequestUnlabeledPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `unlabeled`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlabeled"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    label: WebhooksLabel | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestUnlabeledPayloadPullRequest
    repository: Repository
    sender: User


class PullRequestUnlockedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `unlocked`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["unlocked"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    number: int
    organization: Organization | None = None
    pull_request: PullRequestUnlockedPayloadPullRequest
    repository: Repository
    sender: User


class RepositoryTransferredPayload(BaseModel):
    """Payload for the GitHub `repository` webhook with action `transferred`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["transferred"]
    changes: RepositoryTransferredPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class TeamEditedPayload(BaseModel):
    """Payload for the GitHub `team` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    changes: TeamEditedPayloadChanges
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization
    repository: TeamEditedPayloadRepository | None = None
    sender: User
    team: WebhooksTeam1


class PackageUpdatedPayload(BaseModel):
    """Payload for the GitHub `package` webhook with action `updated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["updated"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    package: PackageUpdatedPayloadPackage
    repository: Repository
    sender: User


class RegistryPackageUpdatedPayload(BaseModel):
    """Payload for the GitHub `registry_package` webhook with action `updated`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["updated"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    registry_package: RegistryPackageUpdatedPayloadRegistryPackage
    repository: Repository | None = None
    sender: User


class PullRequestDemilestonedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `demilestoned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["demilestoned"]
    enterprise: Enterprise | None = None
    milestone: Milestone | None = None
    number: int
    organization: Organization | None = None
    pull_request: WebhooksPullRequest5
    repository: Repository
    sender: User | None = None


class PullRequestMilestonedPayload(BaseModel):
    """Payload for the GitHub `pull_request` webhook with action `milestoned`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["milestoned"]
    enterprise: Enterprise | None = None
    milestone: Milestone | None = None
    number: int
    organization: Organization | None = None
    pull_request: WebhooksPullRequest5
    repository: Repository
    sender: User | None = None


class WorkflowRunRequestedPayload(BaseModel):
    """Payload for the GitHub `workflow_run` webhook with action `requested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["requested"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User
    workflow: Any | None
    workflow_run: WorkflowRunRequestedPayloadWorkflowRun


class DependabotAlertAutoDismissedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `auto_dismissed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["auto_dismissed"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertAutoReopenedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `auto_reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["auto_reopened"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertCreatedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertDismissedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `dismissed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["dismissed"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertFixedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `fixed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["fixed"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertReintroducedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `reintroduced`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reintroduced"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class DependabotAlertReopenedPayload(BaseModel):
    """Payload for the GitHub `dependabot_alert` webhook with action `reopened`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["reopened"]
    alert: DependabotAlert
    installation: Installation | None = None
    organization: Organization | None = None
    enterprise: Enterprise | None = None
    repository: Repository
    sender: User


class RepositoryRulesetEditedPayloadChangesRulesUpdated(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRulesUpdated."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rule: (
        RepositoryRuleBranchNamePattern
        | RepositoryRuleCodeScanning
        | RepositoryRuleCommitAuthorEmailPattern
        | RepositoryRuleCommitMessagePattern
        | RepositoryRuleCommitterEmailPattern
        | RepositoryRuleCopilotCodeReview
        | RepositoryRuleCreation
        | RepositoryRuleDeletion
        | RepositoryRuleFileExtensionRestriction
        | RepositoryRuleFilePathRestriction
        | RepositoryRuleMaxFilePathLength
        | RepositoryRuleMaxFileSize
        | RepositoryRuleMergeQueue
        | RepositoryRuleNonFastForward
        | RepositoryRulePullRequest
        | RepositoryRuleRequiredDeployments
        | RepositoryRuleRequiredLinearHistory
        | RepositoryRuleRequiredSignatures
        | RepositoryRuleRequiredStatusChecks
        | RepositoryRuleTagNamePattern
        | RepositoryRuleUpdate
        | RepositoryRuleWorkflows
        | None
    ) = None
    changes: RepositoryRulesetEditedPayloadChangesRulesUpdatedChanges | None = None


class RepositoryRuleset(BaseModel):
    """A set of rules to apply when specified conditions are met."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str
    target: Literal["branch", "tag", "push", "repository"] | None = None
    source_type: Literal["Repository", "Organization", "Enterprise"] | None = None
    source: str
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: list[RepositoryRulesetBypassActor] | None = None
    current_user_can_bypass: Literal["always", "pull_requests_only", "never", "exempt"] | None = None
    node_id: str | None = None
    _links: RepositoryRulesetLinks | None = None
    conditions: RepositoryRulesetConditions | dict[str, Any] | None = None
    rules: (
        list[
            RepositoryRuleBranchNamePattern
            | RepositoryRuleCodeScanning
            | RepositoryRuleCommitAuthorEmailPattern
            | RepositoryRuleCommitMessagePattern
            | RepositoryRuleCommitterEmailPattern
            | RepositoryRuleCopilotCodeReview
            | RepositoryRuleCreation
            | RepositoryRuleDeletion
            | RepositoryRuleFileExtensionRestriction
            | RepositoryRuleFilePathRestriction
            | RepositoryRuleMaxFilePathLength
            | RepositoryRuleMaxFileSize
            | RepositoryRuleMergeQueue
            | RepositoryRuleNonFastForward
            | RepositoryRulePullRequest
            | RepositoryRuleRequiredDeployments
            | RepositoryRuleRequiredLinearHistory
            | RepositoryRuleRequiredSignatures
            | RepositoryRuleRequiredStatusChecks
            | RepositoryRuleTagNamePattern
            | RepositoryRuleUpdate
            | RepositoryRuleWorkflows
        ]
        | None
    ) = None
    created_at: str | None = None
    updated_at: str | None = None


class DeploymentProtectionRuleRequestedPayload(BaseModel):
    """Payload for the GitHub `deployment_protection_rule` webhook with action `requested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["requested"]
    environment: str | None = None
    event: str | None = None
    deployment_callback_url: str | None = None
    deployment: Deployment | None = None
    pull_requests: list[PullRequest] | None = None
    repository: Repository
    organization: Organization | None = None
    installation: Installation | None = None
    sender: User


class CheckRunCompletedPayload(BaseModel):
    """Payload for the GitHub `check_run` webhook with action `completed`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["completed"]
    check_run: CheckRunWithSimpleCheckSuite
    installation: Installation | None = None
    enterprise: Enterprise | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckRunCreatedPayload(BaseModel):
    """Payload for the GitHub `check_run` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    check_run: CheckRunWithSimpleCheckSuite
    installation: Installation | None = None
    enterprise: Enterprise | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class CheckRunRequestedActionPayload(BaseModel):
    """Payload for the GitHub `check_run` webhook with action `requested_action`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["requested_action"]
    check_run: CheckRunWithSimpleCheckSuite
    installation: Installation | None = None
    enterprise: Enterprise | None = None
    organization: Organization | None = None
    repository: Repository
    requested_action: CheckRunRequestedActionPayloadRequestedAction | None = None
    sender: User


class CheckRunRerequestedPayload(BaseModel):
    """Payload for the GitHub `check_run` webhook with action `rerequested`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["rerequested"]
    check_run: CheckRunWithSimpleCheckSuite
    installation: Installation | None = None
    enterprise: Enterprise | None = None
    organization: Organization | None = None
    repository: Repository
    sender: User


class RepositoryRulesetEditedPayloadChangesRules(BaseModel):
    """RepositoryRulesetEditedPayloadChangesRules."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    added: (
        list[
            RepositoryRuleBranchNamePattern
            | RepositoryRuleCodeScanning
            | RepositoryRuleCommitAuthorEmailPattern
            | RepositoryRuleCommitMessagePattern
            | RepositoryRuleCommitterEmailPattern
            | RepositoryRuleCopilotCodeReview
            | RepositoryRuleCreation
            | RepositoryRuleDeletion
            | RepositoryRuleFileExtensionRestriction
            | RepositoryRuleFilePathRestriction
            | RepositoryRuleMaxFilePathLength
            | RepositoryRuleMaxFileSize
            | RepositoryRuleMergeQueue
            | RepositoryRuleNonFastForward
            | RepositoryRulePullRequest
            | RepositoryRuleRequiredDeployments
            | RepositoryRuleRequiredLinearHistory
            | RepositoryRuleRequiredSignatures
            | RepositoryRuleRequiredStatusChecks
            | RepositoryRuleTagNamePattern
            | RepositoryRuleUpdate
            | RepositoryRuleWorkflows
        ]
        | None
    ) = None
    deleted: (
        list[
            RepositoryRuleBranchNamePattern
            | RepositoryRuleCodeScanning
            | RepositoryRuleCommitAuthorEmailPattern
            | RepositoryRuleCommitMessagePattern
            | RepositoryRuleCommitterEmailPattern
            | RepositoryRuleCopilotCodeReview
            | RepositoryRuleCreation
            | RepositoryRuleDeletion
            | RepositoryRuleFileExtensionRestriction
            | RepositoryRuleFilePathRestriction
            | RepositoryRuleMaxFilePathLength
            | RepositoryRuleMaxFileSize
            | RepositoryRuleMergeQueue
            | RepositoryRuleNonFastForward
            | RepositoryRulePullRequest
            | RepositoryRuleRequiredDeployments
            | RepositoryRuleRequiredLinearHistory
            | RepositoryRuleRequiredSignatures
            | RepositoryRuleRequiredStatusChecks
            | RepositoryRuleTagNamePattern
            | RepositoryRuleUpdate
            | RepositoryRuleWorkflows
        ]
        | None
    ) = None
    updated: list[RepositoryRulesetEditedPayloadChangesRulesUpdated] | None = None


class RepositoryRulesetCreatedPayload(BaseModel):
    """Payload for the GitHub `repository_ruleset` webhook with action `created`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["created"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    repository_ruleset: RepositoryRuleset
    sender: User


class RepositoryRulesetDeletedPayload(BaseModel):
    """Payload for the GitHub `repository_ruleset` webhook with action `deleted`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["deleted"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    repository_ruleset: RepositoryRuleset
    sender: User


class RepositoryRulesetEditedPayloadChanges(BaseModel):
    """RepositoryRulesetEditedPayloadChanges."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: RepositoryRulesetEditedPayloadChangesName | None = None
    enforcement: RepositoryRulesetEditedPayloadChangesEnforcement | None = None
    conditions: RepositoryRulesetEditedPayloadChangesConditions | None = None
    rules: RepositoryRulesetEditedPayloadChangesRules | None = None


class RepositoryRulesetEditedPayload(BaseModel):
    """Payload for the GitHub `repository_ruleset` webhook with action `edited`."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Literal["edited"]
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    repository_ruleset: RepositoryRuleset
    changes: RepositoryRulesetEditedPayloadChanges | None = None
    sender: User


type WebhookPayloadModel = BaseModel
