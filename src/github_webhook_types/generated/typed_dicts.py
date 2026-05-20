# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""TypedDict payloads generated from Octokit's GitHub webhook schema.

Do not edit this module by hand. Run `pdm run generate` instead.
"""

from typing import Any, Literal, NotRequired, Required, TypedDict

__all__ = [
    "AppPermissionsDict",
    "BranchProtectionConfigurationDisabledPayloadDict",
    "BranchProtectionConfigurationEnabledPayloadDict",
    "BranchProtectionRuleCreatedPayloadDict",
    "BranchProtectionRuleDeletedPayloadDict",
    "BranchProtectionRuleEditedPayloadChangesAdminEnforcedDict",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorNamesDict",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnlyDict",
    "BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnlyDict",
    "BranchProtectionRuleEditedPayloadChangesDict",
    "BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevelDict",
    "BranchProtectionRuleEditedPayloadChangesLockAllowsForkSyncDict",
    "BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevelDict",
    "BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevelDict",
    "BranchProtectionRuleEditedPayloadChangesRequireLastPushApprovalDict",
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksDict",
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevelDict",
    "BranchProtectionRuleEditedPayloadDict",
    "CheckRunCompletedPayloadDict",
    "CheckRunCreatedPayloadDict",
    "CheckRunRequestedActionPayloadDict",
    "CheckRunRequestedActionPayloadRequestedActionDict",
    "CheckRunRerequestedPayloadDict",
    "CheckRunWithSimpleCheckSuiteDict",
    "CheckRunWithSimpleCheckSuiteOutputDict",
    "CheckSuiteCompletedPayloadCheckSuiteAppDict",
    "CheckSuiteCompletedPayloadCheckSuiteAppPermissionsDict",
    "CheckSuiteCompletedPayloadCheckSuiteDict",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthorDict",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitterDict",
    "CheckSuiteCompletedPayloadCheckSuiteHeadCommitDict",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestBaseDict",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepoDict",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestDict",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestHeadDict",
    "CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepoDict",
    "CheckSuiteCompletedPayloadDict",
    "CheckSuiteRequestedPayloadCheckSuiteAppDict",
    "CheckSuiteRequestedPayloadCheckSuiteAppPermissionsDict",
    "CheckSuiteRequestedPayloadCheckSuiteDict",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthorDict",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitterDict",
    "CheckSuiteRequestedPayloadCheckSuiteHeadCommitDict",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestBaseDict",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepoDict",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestDict",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestHeadDict",
    "CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepoDict",
    "CheckSuiteRequestedPayloadDict",
    "CheckSuiteRerequestedPayloadCheckSuiteAppDict",
    "CheckSuiteRerequestedPayloadCheckSuiteAppPermissionsDict",
    "CheckSuiteRerequestedPayloadCheckSuiteDict",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthorDict",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitterDict",
    "CheckSuiteRerequestedPayloadCheckSuiteHeadCommitDict",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseDict",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepoDict",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestDict",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadDict",
    "CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepoDict",
    "CheckSuiteRerequestedPayloadDict",
    "CodeOfConductDict",
    "CodeOfConductSimpleDict",
    "CodeScanningAlertAppearedInBranchPayloadAlertDict",
    "CodeScanningAlertAppearedInBranchPayloadAlertRuleDict",
    "CodeScanningAlertAppearedInBranchPayloadAlertToolDict",
    "CodeScanningAlertAppearedInBranchPayloadDict",
    "CodeScanningAlertClosedByUserPayloadAlertDict",
    "CodeScanningAlertClosedByUserPayloadAlertRuleDict",
    "CodeScanningAlertClosedByUserPayloadAlertToolDict",
    "CodeScanningAlertClosedByUserPayloadDict",
    "CodeScanningAlertCreatedPayloadAlertDict",
    "CodeScanningAlertCreatedPayloadAlertRuleDict",
    "CodeScanningAlertCreatedPayloadDict",
    "CodeScanningAlertFixedPayloadAlertDict",
    "CodeScanningAlertFixedPayloadAlertRuleDict",
    "CodeScanningAlertFixedPayloadAlertToolDict",
    "CodeScanningAlertFixedPayloadDict",
    "CodeScanningAlertReopenedByUserPayloadAlertDict",
    "CodeScanningAlertReopenedByUserPayloadAlertRuleDict",
    "CodeScanningAlertReopenedByUserPayloadAlertToolDict",
    "CodeScanningAlertReopenedByUserPayloadDict",
    "CodeScanningAlertReopenedPayloadAlertDict",
    "CodeScanningAlertReopenedPayloadAlertRuleDict",
    "CodeScanningAlertReopenedPayloadAlertToolDict",
    "CodeScanningAlertReopenedPayloadDict",
    "CommitCommentCreatedPayloadCommentDict",
    "CommitCommentCreatedPayloadCommentReactionsDict",
    "CommitCommentCreatedPayloadDict",
    "CreatePayloadDict",
    "CustomPropertyCreatedPayloadDict",
    "CustomPropertyDeletedPayloadDefinitionDict",
    "CustomPropertyDeletedPayloadDict",
    "CustomPropertyDict",
    "CustomPropertyPromoteToEnterprisePayloadDict",
    "CustomPropertyUpdatedPayloadDict",
    "CustomPropertyValueDict",
    "CustomPropertyValuesUpdatedPayloadDict",
    "DeletePayloadDict",
    "DependabotAlertAutoDismissedPayloadDict",
    "DependabotAlertAutoReopenedPayloadDict",
    "DependabotAlertCreatedPayloadDict",
    "DependabotAlertDependencyDict",
    "DependabotAlertDict",
    "DependabotAlertDismissedPayloadDict",
    "DependabotAlertFixedPayloadDict",
    "DependabotAlertPackageDict",
    "DependabotAlertReintroducedPayloadDict",
    "DependabotAlertReopenedPayloadDict",
    "DependabotAlertSecurityAdvisoryCvssDict",
    "DependabotAlertSecurityAdvisoryCweDict",
    "DependabotAlertSecurityAdvisoryDict",
    "DependabotAlertSecurityAdvisoryIdentifierDict",
    "DependabotAlertSecurityAdvisoryReferenceDict",
    "DependabotAlertSecurityVulnerabilityDict",
    "DeployKeyCreatedPayloadDict",
    "DeployKeyDeletedPayloadDict",
    "DeploymentCreatedPayloadDeploymentDict",
    "DeploymentCreatedPayloadDict",
    "DeploymentDict",
    "DeploymentProtectionRuleRequestedPayloadDict",
    "DeploymentReviewApprovedPayloadDict",
    "DeploymentReviewApprovedPayloadReviewerDict",
    "DeploymentReviewApprovedPayloadWorkflowJobRunDict",
    "DeploymentReviewRejectedPayloadDict",
    "DeploymentReviewRejectedPayloadReviewerDict",
    "DeploymentReviewRejectedPayloadWorkflowJobRunDict",
    "DeploymentReviewRequestedPayloadDict",
    "DeploymentReviewRequestedPayloadReviewerDict",
    "DeploymentReviewRequestedPayloadWorkflowJobRunDict",
    "DeploymentSimpleDict",
    "DeploymentStatusCreatedPayloadDeploymentDict",
    "DeploymentStatusCreatedPayloadDeploymentStatusDict",
    "DeploymentStatusCreatedPayloadDict",
    "DiscussionAnsweredPayloadDict",
    "DiscussionCategoryChangedPayloadChangesCategoryDict",
    "DiscussionCategoryChangedPayloadChangesCategoryFromDict",
    "DiscussionCategoryChangedPayloadChangesDict",
    "DiscussionCategoryChangedPayloadDict",
    "DiscussionCategoryDict",
    "DiscussionClosedPayloadDict",
    "DiscussionCommentCreatedPayloadDict",
    "DiscussionCommentDeletedPayloadDict",
    "DiscussionCommentEditedPayloadChangesBodyDict",
    "DiscussionCommentEditedPayloadChangesDict",
    "DiscussionCommentEditedPayloadDict",
    "DiscussionCreatedPayloadDict",
    "DiscussionDeletedPayloadDict",
    "DiscussionDict",
    "DiscussionEditedPayloadChangesBodyDict",
    "DiscussionEditedPayloadChangesDict",
    "DiscussionEditedPayloadChangesTitleDict",
    "DiscussionEditedPayloadDict",
    "DiscussionLabeledPayloadDict",
    "DiscussionLockedPayloadDict",
    "DiscussionPinnedPayloadDict",
    "DiscussionReactionsDict",
    "DiscussionReopenedPayloadDict",
    "DiscussionTransferredPayloadChangesDict",
    "DiscussionTransferredPayloadDict",
    "DiscussionUnansweredPayloadDict",
    "DiscussionUnlabeledPayloadDict",
    "DiscussionUnlockedPayloadDict",
    "DiscussionUnpinnedPayloadDict",
    "EnterpriseDict",
    "EnterpriseDict2",
    "ForkPayloadDict",
    "FullRepositoryDict",
    "FullRepositoryPermissionsDict",
    "GithubAppAuthorizationRevokedPayloadDict",
    "GollumPayloadDict",
    "GollumPayloadPageDict",
    "HookResponseDict",
    "InstallationCreatedPayloadDict",
    "InstallationCreatedPayloadRepositoryDict",
    "InstallationDeletedPayloadDict",
    "InstallationDeletedPayloadRepositoryDict",
    "InstallationDict",
    "InstallationDict2",
    "InstallationNewPermissionsAcceptedPayloadDict",
    "InstallationNewPermissionsAcceptedPayloadRepositoryDict",
    "InstallationRepositoriesAddedPayloadDict",
    "InstallationRepositoriesAddedPayloadRepositoriesAddedDict",
    "InstallationRepositoriesAddedPayloadRepositoriesRemovedDict",
    "InstallationRepositoriesRemovedPayloadDict",
    "InstallationRepositoriesRemovedPayloadRepositoriesAddedDict",
    "InstallationRepositoriesRemovedPayloadRepositoriesRemovedDict",
    "InstallationSuspendPayloadDict",
    "InstallationSuspendPayloadRepositoryDict",
    "InstallationTargetRenamedPayloadAccountDict",
    "InstallationTargetRenamedPayloadChangesDict",
    "InstallationTargetRenamedPayloadChangesLoginDict",
    "InstallationTargetRenamedPayloadChangesSlugDict",
    "InstallationTargetRenamedPayloadDict",
    "InstallationUnsuspendPayloadDict",
    "InstallationUnsuspendPayloadRepositoryDict",
    "IssueCommentCreatedPayloadCommentDict",
    "IssueCommentCreatedPayloadCommentReactionsDict",
    "IssueCommentCreatedPayloadDict",
    "IssueCommentDeletedPayloadDict",
    "IssueCommentEditedPayloadDict",
    "IssueDependenciesBlockedByAddedPayloadDict",
    "IssueDependenciesBlockedByRemovedPayloadDict",
    "IssueDependenciesBlockingAddedPayloadDict",
    "IssueDependenciesBlockingRemovedPayloadDict",
    "IssueDependenciesSummaryDict",
    "IssueDict",
    "IssueFieldValueDict",
    "IssueLabelOption2Dict",
    "IssuePullRequestDict",
    "IssuesAssignedPayloadDict",
    "IssuesClosedPayloadDict",
    "IssuesDeletedPayloadDict",
    "IssuesDeletedPayloadIssueDict",
    "IssuesDeletedPayloadIssueLabelDict",
    "IssuesDeletedPayloadIssuePullRequestDict",
    "IssuesDeletedPayloadIssueReactionsDict",
    "IssuesDemilestonedPayloadDict",
    "IssuesDemilestonedPayloadIssueDict",
    "IssuesDemilestonedPayloadIssuePullRequestDict",
    "IssuesDemilestonedPayloadIssueReactionsDict",
    "IssuesEditedPayloadChangesBodyDict",
    "IssuesEditedPayloadChangesDict",
    "IssuesEditedPayloadChangesTitleDict",
    "IssuesEditedPayloadDict",
    "IssuesEditedPayloadIssueDict",
    "IssuesEditedPayloadIssueLabelDict",
    "IssuesEditedPayloadIssuePullRequestDict",
    "IssuesEditedPayloadIssueReactionsDict",
    "IssuesLabeledPayloadDict",
    "IssuesLabeledPayloadIssueDict",
    "IssuesLabeledPayloadIssueLabelDict",
    "IssuesLabeledPayloadIssuePullRequestDict",
    "IssuesLabeledPayloadIssueReactionsDict",
    "IssuesLockedPayloadDict",
    "IssuesLockedPayloadIssueDict",
    "IssuesLockedPayloadIssuePullRequestDict",
    "IssuesLockedPayloadIssueReactionsDict",
    "IssuesMilestonedPayloadDict",
    "IssuesMilestonedPayloadIssueDict",
    "IssuesMilestonedPayloadIssuePullRequestDict",
    "IssuesMilestonedPayloadIssueReactionsDict",
    "IssuesOpenedPayloadChangesDict",
    "IssuesOpenedPayloadChangesOldRepositoryDict",
    "IssuesOpenedPayloadChangesOldRepositoryPermissionsDict",
    "IssuesOpenedPayloadDict",
    "IssuesOpenedPayloadIssueDict",
    "IssuesOpenedPayloadIssueLabelDict",
    "IssuesOpenedPayloadIssuePullRequestDict",
    "IssuesOpenedPayloadIssueReactionsDict",
    "IssuesPinnedPayloadDict",
    "IssuesReopenedPayloadDict",
    "IssuesReopenedPayloadIssueDict",
    "IssuesReopenedPayloadIssuePullRequestDict",
    "IssuesReopenedPayloadIssueReactionsDict",
    "IssuesTransferredPayloadChangesDict",
    "IssuesTransferredPayloadChangesNewIssueDict",
    "IssuesTransferredPayloadChangesNewIssueLabelDict",
    "IssuesTransferredPayloadChangesNewIssuePullRequestDict",
    "IssuesTransferredPayloadChangesNewIssueReactionsDict",
    "IssuesTransferredPayloadChangesNewRepositoryDict",
    "IssuesTransferredPayloadChangesNewRepositoryPermissionsDict",
    "IssuesTransferredPayloadDict",
    "IssuesTypedPayloadDict",
    "IssuesUnassignedPayloadDict",
    "IssuesUnlabeledPayloadDict",
    "IssuesUnlockedPayloadDict",
    "IssuesUnlockedPayloadIssueDict",
    "IssuesUnlockedPayloadIssuePullRequestDict",
    "IssuesUnlockedPayloadIssueReactionsDict",
    "IssuesUnpinnedPayloadDict",
    "IssuesUntypedPayloadDict",
    "LabelCreatedPayloadDict",
    "LabelDeletedPayloadDict",
    "LabelDict",
    "LabelEditedPayloadChangesColorDict",
    "LabelEditedPayloadChangesDescriptionDict",
    "LabelEditedPayloadChangesDict",
    "LabelEditedPayloadChangesNameDict",
    "LabelEditedPayloadDict",
    "LicenseSimpleDict",
    "LinkDict",
    "MarketplacePurchaseCancelledPayloadDict",
    "MarketplacePurchaseChangedPayloadDict",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccountDict",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseDict",
    "MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlanDict",
    "MarketplacePurchasePendingChangeCancelledPayloadDict",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccountDict",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseDict",
    "MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlanDict",
    "MarketplacePurchasePendingChangePayloadDict",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccountDict",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseDict",
    "MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlanDict",
    "MarketplacePurchasePurchasedPayloadDict",
    "MemberAddedPayloadChangesDict",
    "MemberAddedPayloadChangesPermissionDict",
    "MemberAddedPayloadChangesRoleNameDict",
    "MemberAddedPayloadDict",
    "MemberEditedPayloadChangesDict",
    "MemberEditedPayloadChangesOldPermissionDict",
    "MemberEditedPayloadChangesPermissionDict",
    "MemberEditedPayloadDict",
    "MemberRemovedPayloadDict",
    "MembershipAddedPayloadDict",
    "MembershipRemovedPayloadDict",
    "MergeGroupChecksRequestedPayloadDict",
    "MergeGroupDestroyedPayloadDict",
    "MergeGroupDict",
    "MetaDeletedPayloadDict",
    "MetaDeletedPayloadHookConfigDict",
    "MetaDeletedPayloadHookDict",
    "MilestoneClosedPayloadDict",
    "MilestoneClosedPayloadMilestoneDict",
    "MilestoneCreatedPayloadDict",
    "MilestoneCreatedPayloadMilestoneDict",
    "MilestoneDeletedPayloadDict",
    "MilestoneDict",
    "MilestoneEditedPayloadChangesDescriptionDict",
    "MilestoneEditedPayloadChangesDict",
    "MilestoneEditedPayloadChangesDueOnDict",
    "MilestoneEditedPayloadChangesTitleDict",
    "MilestoneEditedPayloadDict",
    "MilestoneOpenedPayloadDict",
    "MilestoneOpenedPayloadMilestoneDict",
    "MinimalRepositoryDict",
    "MinimalRepositoryPermissionsDict",
    "OrgBlockBlockedPayloadDict",
    "OrgBlockUnblockedPayloadDict",
    "OrganizationDeletedPayloadDict",
    "OrganizationDict",
    "OrganizationMemberAddedPayloadDict",
    "OrganizationMemberInvitedPayloadDict",
    "OrganizationMemberInvitedPayloadInvitationDict",
    "OrganizationMemberRemovedPayloadDict",
    "OrganizationRenamedPayloadChangesDict",
    "OrganizationRenamedPayloadChangesLoginDict",
    "OrganizationRenamedPayloadDict",
    "PackagePublishedPayloadDict",
    "PackagePublishedPayloadPackageDict",
    "PackageUpdatedPayloadDict",
    "PackageUpdatedPayloadPackageDict",
    "PackageUpdatedPayloadPackagePackageVersionDict",
    "PackageUpdatedPayloadPackagePackageVersionDockerMetadataDict",
    "PackageUpdatedPayloadPackagePackageVersionPackageFileDict",
    "PackageUpdatedPayloadPackagePackageVersionReleaseDict",
    "PageBuildPayloadBuildDict",
    "PageBuildPayloadBuildErrorDict",
    "PageBuildPayloadDict",
    "PersonalAccessTokenRequestApprovedPayloadDict",
    "PersonalAccessTokenRequestCancelledPayloadDict",
    "PersonalAccessTokenRequestCreatedPayloadDict",
    "PersonalAccessTokenRequestDeniedPayloadDict",
    "PersonalAccessTokenRequestDict",
    "PersonalAccessTokenRequestPermissionsAddedDict",
    "PersonalAccessTokenRequestPermissionsResultDict",
    "PersonalAccessTokenRequestPermissionsUpgradedDict",
    "PingPayloadDict",
    "PingPayloadHookConfigDict",
    "PingPayloadHookDict",
    "ProjectCardConvertedPayloadChangesDict",
    "ProjectCardConvertedPayloadChangesNoteDict",
    "ProjectCardConvertedPayloadDict",
    "ProjectCardCreatedPayloadDict",
    "ProjectCardDeletedPayloadDict",
    "ProjectCardDeletedPayloadProjectCardDict",
    "ProjectCardEditedPayloadChangesDict",
    "ProjectCardEditedPayloadChangesNoteDict",
    "ProjectCardEditedPayloadDict",
    "ProjectCardMovedPayloadChangesColumnIdDict",
    "ProjectCardMovedPayloadChangesDict",
    "ProjectCardMovedPayloadDict",
    "ProjectClosedPayloadDict",
    "ProjectColumnCreatedPayloadDict",
    "ProjectColumnDeletedPayloadDict",
    "ProjectColumnEditedPayloadChangesDict",
    "ProjectColumnEditedPayloadChangesNameDict",
    "ProjectColumnEditedPayloadDict",
    "ProjectColumnMovedPayloadDict",
    "ProjectCreatedPayloadDict",
    "ProjectDeletedPayloadDict",
    "ProjectEditedPayloadChangesBodyDict",
    "ProjectEditedPayloadChangesDict",
    "ProjectEditedPayloadChangesNameDict",
    "ProjectEditedPayloadDict",
    "ProjectReopenedPayloadDict",
    "ProjectsV2ClosedPayloadDict",
    "ProjectsV2CreatedPayloadDict",
    "ProjectsV2DeletedPayloadDict",
    "ProjectsV2Dict",
    "ProjectsV2EditedPayloadChangesDescriptionDict",
    "ProjectsV2EditedPayloadChangesDict",
    "ProjectsV2EditedPayloadChangesPublicDict",
    "ProjectsV2EditedPayloadChangesShortDescriptionDict",
    "ProjectsV2EditedPayloadChangesTitleDict",
    "ProjectsV2EditedPayloadDict",
    "ProjectsV2ItemArchivedPayloadDict",
    "ProjectsV2ItemConvertedPayloadChangesContentTypeDict",
    "ProjectsV2ItemConvertedPayloadChangesDict",
    "ProjectsV2ItemConvertedPayloadDict",
    "ProjectsV2ItemCreatedPayloadDict",
    "ProjectsV2ItemDeletedPayloadDict",
    "ProjectsV2ItemDict",
    "ProjectsV2ItemEditedPayloadChangesOption1Dict",
    "ProjectsV2ItemEditedPayloadChangesOption1FieldValueDict",
    "ProjectsV2ItemEditedPayloadChangesOption2BodyDict",
    "ProjectsV2ItemEditedPayloadChangesOption2Dict",
    "ProjectsV2ItemEditedPayloadDict",
    "ProjectsV2ItemReorderedPayloadChangesDict",
    "ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeIdDict",
    "ProjectsV2ItemReorderedPayloadDict",
    "ProjectsV2ItemRestoredPayloadDict",
    "ProjectsV2IterationSettingDict",
    "ProjectsV2ReopenedPayloadDict",
    "ProjectsV2SingleSelectOptionDict",
    "ProjectsV2StatusUpdateCreatedPayloadDict",
    "ProjectsV2StatusUpdateDeletedPayloadDict",
    "ProjectsV2StatusUpdateDict",
    "ProjectsV2StatusUpdateEditedPayloadChangesBodyDict",
    "ProjectsV2StatusUpdateEditedPayloadChangesDict",
    "ProjectsV2StatusUpdateEditedPayloadChangesStartDateDict",
    "ProjectsV2StatusUpdateEditedPayloadChangesStatusDict",
    "ProjectsV2StatusUpdateEditedPayloadChangesTargetDateDict",
    "ProjectsV2StatusUpdateEditedPayloadDict",
    "PublicPayloadDict",
    "PullRequestAssignedPayloadDict",
    "PullRequestAssignedPayloadPullRequestBaseDict",
    "PullRequestAssignedPayloadPullRequestBaseRepoDict",
    "PullRequestAssignedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestAssignedPayloadPullRequestDict",
    "PullRequestAssignedPayloadPullRequestHeadDict",
    "PullRequestAssignedPayloadPullRequestLabelDict",
    "PullRequestAssignedPayloadPullRequestLinksCommentsDict",
    "PullRequestAssignedPayloadPullRequestLinksCommitsDict",
    "PullRequestAssignedPayloadPullRequestLinksDict",
    "PullRequestAssignedPayloadPullRequestLinksHtmlDict",
    "PullRequestAssignedPayloadPullRequestLinksIssueDict",
    "PullRequestAssignedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestAssignedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestAssignedPayloadPullRequestLinksSelfDict",
    "PullRequestAssignedPayloadPullRequestLinksStatusesDict",
    "PullRequestAssignedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestAssignedPayloadPullRequestRequestedTeamDict",
    "PullRequestAutoMergeDisabledPayloadDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestBaseDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestHeadDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLabelDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksCommentsDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksCommitsDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksHtmlDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksIssueDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksSelfDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestLinksStatusesDict",
    "PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeamDict",
    "PullRequestAutoMergeEnabledPayloadDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestBaseDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestHeadDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLabelDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksCommentsDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksCommitsDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksHtmlDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksIssueDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksSelfDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestLinksStatusesDict",
    "PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeamDict",
    "PullRequestBaseDict",
    "PullRequestClosedPayloadDict",
    "PullRequestConvertedToDraftPayloadDict",
    "PullRequestDemilestonedPayloadDict",
    "PullRequestDequeuedPayloadDict",
    "PullRequestDequeuedPayloadPullRequestBaseDict",
    "PullRequestDequeuedPayloadPullRequestBaseRepoDict",
    "PullRequestDequeuedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestDequeuedPayloadPullRequestDict",
    "PullRequestDequeuedPayloadPullRequestHeadDict",
    "PullRequestDequeuedPayloadPullRequestHeadRepoDict",
    "PullRequestDequeuedPayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestDequeuedPayloadPullRequestLabelDict",
    "PullRequestDequeuedPayloadPullRequestLinksCommentsDict",
    "PullRequestDequeuedPayloadPullRequestLinksCommitsDict",
    "PullRequestDequeuedPayloadPullRequestLinksDict",
    "PullRequestDequeuedPayloadPullRequestLinksHtmlDict",
    "PullRequestDequeuedPayloadPullRequestLinksIssueDict",
    "PullRequestDequeuedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestDequeuedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestDequeuedPayloadPullRequestLinksSelfDict",
    "PullRequestDequeuedPayloadPullRequestLinksStatusesDict",
    "PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestDequeuedPayloadPullRequestRequestedTeamDict",
    "PullRequestDict",
    "PullRequestEditedPayloadChangesBaseDict",
    "PullRequestEditedPayloadChangesBaseRefDict",
    "PullRequestEditedPayloadChangesBaseShaDict",
    "PullRequestEditedPayloadChangesBodyDict",
    "PullRequestEditedPayloadChangesDict",
    "PullRequestEditedPayloadChangesTitleDict",
    "PullRequestEditedPayloadDict",
    "PullRequestEnqueuedPayloadDict",
    "PullRequestEnqueuedPayloadPullRequestBaseDict",
    "PullRequestEnqueuedPayloadPullRequestBaseRepoDict",
    "PullRequestEnqueuedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestEnqueuedPayloadPullRequestDict",
    "PullRequestEnqueuedPayloadPullRequestHeadDict",
    "PullRequestEnqueuedPayloadPullRequestHeadRepoDict",
    "PullRequestEnqueuedPayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestEnqueuedPayloadPullRequestLabelDict",
    "PullRequestEnqueuedPayloadPullRequestLinksCommentsDict",
    "PullRequestEnqueuedPayloadPullRequestLinksCommitsDict",
    "PullRequestEnqueuedPayloadPullRequestLinksDict",
    "PullRequestEnqueuedPayloadPullRequestLinksHtmlDict",
    "PullRequestEnqueuedPayloadPullRequestLinksIssueDict",
    "PullRequestEnqueuedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestEnqueuedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestEnqueuedPayloadPullRequestLinksSelfDict",
    "PullRequestEnqueuedPayloadPullRequestLinksStatusesDict",
    "PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestEnqueuedPayloadPullRequestRequestedTeamDict",
    "PullRequestHeadDict",
    "PullRequestLabelDict",
    "PullRequestLabeledPayloadDict",
    "PullRequestLabeledPayloadPullRequestBaseDict",
    "PullRequestLabeledPayloadPullRequestBaseRepoDict",
    "PullRequestLabeledPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestLabeledPayloadPullRequestDict",
    "PullRequestLabeledPayloadPullRequestHeadDict",
    "PullRequestLabeledPayloadPullRequestLabelDict",
    "PullRequestLabeledPayloadPullRequestLinksCommentsDict",
    "PullRequestLabeledPayloadPullRequestLinksCommitsDict",
    "PullRequestLabeledPayloadPullRequestLinksDict",
    "PullRequestLabeledPayloadPullRequestLinksHtmlDict",
    "PullRequestLabeledPayloadPullRequestLinksIssueDict",
    "PullRequestLabeledPayloadPullRequestLinksReviewCommentDict",
    "PullRequestLabeledPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestLabeledPayloadPullRequestLinksSelfDict",
    "PullRequestLabeledPayloadPullRequestLinksStatusesDict",
    "PullRequestLabeledPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestLabeledPayloadPullRequestRequestedTeamDict",
    "PullRequestLinksDict",
    "PullRequestLockedPayloadDict",
    "PullRequestLockedPayloadPullRequestBaseDict",
    "PullRequestLockedPayloadPullRequestBaseRepoDict",
    "PullRequestLockedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestLockedPayloadPullRequestDict",
    "PullRequestLockedPayloadPullRequestHeadDict",
    "PullRequestLockedPayloadPullRequestLabelDict",
    "PullRequestLockedPayloadPullRequestLinksCommentsDict",
    "PullRequestLockedPayloadPullRequestLinksCommitsDict",
    "PullRequestLockedPayloadPullRequestLinksDict",
    "PullRequestLockedPayloadPullRequestLinksHtmlDict",
    "PullRequestLockedPayloadPullRequestLinksIssueDict",
    "PullRequestLockedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestLockedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestLockedPayloadPullRequestLinksSelfDict",
    "PullRequestLockedPayloadPullRequestLinksStatusesDict",
    "PullRequestLockedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestLockedPayloadPullRequestRequestedTeamDict",
    "PullRequestMilestonedPayloadDict",
    "PullRequestMinimalBaseDict",
    "PullRequestMinimalBaseRepoDict",
    "PullRequestMinimalDict",
    "PullRequestMinimalHeadDict",
    "PullRequestMinimalHeadRepoDict",
    "PullRequestOpenedPayloadDict",
    "PullRequestPayloadDict",
    "PullRequestPayloadDict2",
    "PullRequestReadyForReviewPayloadDict",
    "PullRequestReopenedPayloadDict",
    "PullRequestReviewCommentCreatedPayloadCommentDict",
    "PullRequestReviewCommentCreatedPayloadCommentLinksDict",
    "PullRequestReviewCommentCreatedPayloadCommentLinksHtmlDict",
    "PullRequestReviewCommentCreatedPayloadCommentLinksPullRequestDict",
    "PullRequestReviewCommentCreatedPayloadCommentLinksSelfDict",
    "PullRequestReviewCommentCreatedPayloadCommentReactionsDict",
    "PullRequestReviewCommentCreatedPayloadDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestBaseDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestHeadDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLabelDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewCommentDeletedPayloadDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestBaseDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestHeadDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLabelDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewCommentEditedPayloadDict",
    "PullRequestReviewCommentEditedPayloadPullRequestBaseDict",
    "PullRequestReviewCommentEditedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewCommentEditedPayloadPullRequestDict",
    "PullRequestReviewCommentEditedPayloadPullRequestHeadDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLabelDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewCommentEditedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewCommentEditedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewDismissedPayloadDict",
    "PullRequestReviewDismissedPayloadPullRequestBaseDict",
    "PullRequestReviewDismissedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewDismissedPayloadPullRequestDict",
    "PullRequestReviewDismissedPayloadPullRequestHeadDict",
    "PullRequestReviewDismissedPayloadPullRequestLabelDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewDismissedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewDismissedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewDismissedPayloadReviewDict",
    "PullRequestReviewDismissedPayloadReviewLinksDict",
    "PullRequestReviewDismissedPayloadReviewLinksHtmlDict",
    "PullRequestReviewDismissedPayloadReviewLinksPullRequestDict",
    "PullRequestReviewEditedPayloadChangesBodyDict",
    "PullRequestReviewEditedPayloadChangesDict",
    "PullRequestReviewEditedPayloadDict",
    "PullRequestReviewEditedPayloadPullRequestBaseDict",
    "PullRequestReviewEditedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewEditedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewEditedPayloadPullRequestDict",
    "PullRequestReviewEditedPayloadPullRequestHeadDict",
    "PullRequestReviewEditedPayloadPullRequestLabelDict",
    "PullRequestReviewEditedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewEditedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewEditedPayloadPullRequestLinksDict",
    "PullRequestReviewEditedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewEditedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewEditedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewEditedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewEditedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewEditedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewEditedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewSubmittedPayloadDict",
    "PullRequestReviewSubmittedPayloadPullRequestBaseDict",
    "PullRequestReviewSubmittedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewSubmittedPayloadPullRequestDict",
    "PullRequestReviewSubmittedPayloadPullRequestHeadDict",
    "PullRequestReviewSubmittedPayloadPullRequestLabelDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewSubmittedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewSubmittedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewThreadResolvedPayloadDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestBaseDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestHeadDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLabelDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtmlDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequestDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelfDict",
    "PullRequestReviewThreadResolvedPayloadThreadCommentReactionsDict",
    "PullRequestReviewThreadResolvedPayloadThreadDict",
    "PullRequestReviewThreadUnresolvedPayloadDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBaseDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHeadDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLabelDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommentsDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommitsDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtmlDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssueDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelfDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatusesDict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeamDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtmlDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequestDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelfDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentReactionsDict",
    "PullRequestReviewThreadUnresolvedPayloadThreadDict",
    "PullRequestSynchronizePayloadDict",
    "PullRequestSynchronizePayloadPullRequestBaseDict",
    "PullRequestSynchronizePayloadPullRequestBaseRepoDict",
    "PullRequestSynchronizePayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestSynchronizePayloadPullRequestDict",
    "PullRequestSynchronizePayloadPullRequestHeadDict",
    "PullRequestSynchronizePayloadPullRequestHeadRepoDict",
    "PullRequestSynchronizePayloadPullRequestHeadRepoPermissionsDict",
    "PullRequestSynchronizePayloadPullRequestLabelDict",
    "PullRequestSynchronizePayloadPullRequestLinksCommentsDict",
    "PullRequestSynchronizePayloadPullRequestLinksCommitsDict",
    "PullRequestSynchronizePayloadPullRequestLinksDict",
    "PullRequestSynchronizePayloadPullRequestLinksHtmlDict",
    "PullRequestSynchronizePayloadPullRequestLinksIssueDict",
    "PullRequestSynchronizePayloadPullRequestLinksReviewCommentDict",
    "PullRequestSynchronizePayloadPullRequestLinksReviewCommentsDict",
    "PullRequestSynchronizePayloadPullRequestLinksSelfDict",
    "PullRequestSynchronizePayloadPullRequestLinksStatusesDict",
    "PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestSynchronizePayloadPullRequestRequestedTeamDict",
    "PullRequestUnassignedPayloadDict",
    "PullRequestUnassignedPayloadPullRequestBaseDict",
    "PullRequestUnassignedPayloadPullRequestBaseRepoDict",
    "PullRequestUnassignedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestUnassignedPayloadPullRequestDict",
    "PullRequestUnassignedPayloadPullRequestHeadDict",
    "PullRequestUnassignedPayloadPullRequestLabelDict",
    "PullRequestUnassignedPayloadPullRequestLinksCommentsDict",
    "PullRequestUnassignedPayloadPullRequestLinksCommitsDict",
    "PullRequestUnassignedPayloadPullRequestLinksDict",
    "PullRequestUnassignedPayloadPullRequestLinksHtmlDict",
    "PullRequestUnassignedPayloadPullRequestLinksIssueDict",
    "PullRequestUnassignedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestUnassignedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestUnassignedPayloadPullRequestLinksSelfDict",
    "PullRequestUnassignedPayloadPullRequestLinksStatusesDict",
    "PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestUnassignedPayloadPullRequestRequestedTeamDict",
    "PullRequestUnlabeledPayloadDict",
    "PullRequestUnlabeledPayloadPullRequestBaseDict",
    "PullRequestUnlabeledPayloadPullRequestBaseRepoDict",
    "PullRequestUnlabeledPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestUnlabeledPayloadPullRequestDict",
    "PullRequestUnlabeledPayloadPullRequestHeadDict",
    "PullRequestUnlabeledPayloadPullRequestLabelDict",
    "PullRequestUnlabeledPayloadPullRequestLinksCommentsDict",
    "PullRequestUnlabeledPayloadPullRequestLinksCommitsDict",
    "PullRequestUnlabeledPayloadPullRequestLinksDict",
    "PullRequestUnlabeledPayloadPullRequestLinksHtmlDict",
    "PullRequestUnlabeledPayloadPullRequestLinksIssueDict",
    "PullRequestUnlabeledPayloadPullRequestLinksReviewCommentDict",
    "PullRequestUnlabeledPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestUnlabeledPayloadPullRequestLinksSelfDict",
    "PullRequestUnlabeledPayloadPullRequestLinksStatusesDict",
    "PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestUnlabeledPayloadPullRequestRequestedTeamDict",
    "PullRequestUnlockedPayloadDict",
    "PullRequestUnlockedPayloadPullRequestBaseDict",
    "PullRequestUnlockedPayloadPullRequestBaseRepoDict",
    "PullRequestUnlockedPayloadPullRequestBaseRepoPermissionsDict",
    "PullRequestUnlockedPayloadPullRequestDict",
    "PullRequestUnlockedPayloadPullRequestHeadDict",
    "PullRequestUnlockedPayloadPullRequestLabelDict",
    "PullRequestUnlockedPayloadPullRequestLinksCommentsDict",
    "PullRequestUnlockedPayloadPullRequestLinksCommitsDict",
    "PullRequestUnlockedPayloadPullRequestLinksDict",
    "PullRequestUnlockedPayloadPullRequestLinksHtmlDict",
    "PullRequestUnlockedPayloadPullRequestLinksIssueDict",
    "PullRequestUnlockedPayloadPullRequestLinksReviewCommentDict",
    "PullRequestUnlockedPayloadPullRequestLinksReviewCommentsDict",
    "PullRequestUnlockedPayloadPullRequestLinksSelfDict",
    "PullRequestUnlockedPayloadPullRequestLinksStatusesDict",
    "PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2Dict",
    "PullRequestUnlockedPayloadPullRequestRequestedTeamDict",
    "PushPayloadCommitAuthorDict",
    "PushPayloadCommitCommitterDict",
    "PushPayloadCommitDict",
    "PushPayloadDict",
    "PushPayloadPusherDict",
    "PushPayloadRepositoryDict",
    "PushPayloadRepositoryPermissionsDict",
    "ReactionRollupDict",
    "RegistryPackagePublishedPayloadDict",
    "RegistryPackagePublishedPayloadRegistryPackageDict",
    "RegistryPackagePublishedPayloadRegistryPackageOwnerDict",
    "RegistryPackageUpdatedPayloadDict",
    "RegistryPackageUpdatedPayloadRegistryPackageDict",
    "RegistryPackageUpdatedPayloadRegistryPackageOwnerDict",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthorDict",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionDict",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFileDict",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthorDict",
    "RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseDict",
    "ReleaseCreatedPayloadDict",
    "ReleaseDeletedPayloadDict",
    "ReleaseEditedPayloadChangesBodyDict",
    "ReleaseEditedPayloadChangesDict",
    "ReleaseEditedPayloadChangesMakeLatestDict",
    "ReleaseEditedPayloadChangesNameDict",
    "ReleaseEditedPayloadChangesTagNameDict",
    "ReleaseEditedPayloadDict",
    "ReleasePrereleasedPayloadDict",
    "ReleasePrereleasedPayloadReleaseDict",
    "ReleasePrereleasedPayloadReleaseReactionsDict",
    "ReleasePublishedPayloadDict",
    "ReleaseReleasedPayloadDict",
    "ReleaseUnpublishedPayloadDict",
    "Repository2CodeSearchIndexStatusDict",
    "Repository2PermissionsDict",
    "RepositoryAdvisoryDict",
    "RepositoryAdvisoryIdentifierDict",
    "RepositoryAdvisoryPublishedPayloadDict",
    "RepositoryAdvisoryReportedPayloadDict",
    "RepositoryArchivedPayloadDict",
    "RepositoryCreatedPayloadDict",
    "RepositoryDeletedPayloadDict",
    "RepositoryDict",
    "RepositoryDict2",
    "RepositoryDispatchPayloadDict",
    "RepositoryEditedPayloadChangesDefaultBranchDict",
    "RepositoryEditedPayloadChangesDescriptionDict",
    "RepositoryEditedPayloadChangesDict",
    "RepositoryEditedPayloadChangesHomepageDict",
    "RepositoryEditedPayloadChangesTopicsDict",
    "RepositoryEditedPayloadDict",
    "RepositoryImportPayloadDict",
    "RepositoryPermissionsDict",
    "RepositoryPrivatizedPayloadDict",
    "RepositoryPublicizedPayloadDict",
    "RepositoryRenamedPayloadChangesDict",
    "RepositoryRenamedPayloadChangesRepositoryDict",
    "RepositoryRenamedPayloadChangesRepositoryNameDict",
    "RepositoryRenamedPayloadDict",
    "RepositoryRuleBranchNamePatternDict",
    "RepositoryRuleBranchNamePatternParametersDict",
    "RepositoryRuleCodeScanningDict",
    "RepositoryRuleCodeScanningParametersDict",
    "RepositoryRuleCommitAuthorEmailPatternDict",
    "RepositoryRuleCommitAuthorEmailPatternParametersDict",
    "RepositoryRuleCommitMessagePatternDict",
    "RepositoryRuleCommitMessagePatternParametersDict",
    "RepositoryRuleCommitterEmailPatternDict",
    "RepositoryRuleCommitterEmailPatternParametersDict",
    "RepositoryRuleCopilotCodeReviewDict",
    "RepositoryRuleCopilotCodeReviewParametersDict",
    "RepositoryRuleCreationDict",
    "RepositoryRuleDeletionDict",
    "RepositoryRuleFileExtensionRestrictionDict",
    "RepositoryRuleFileExtensionRestrictionParametersDict",
    "RepositoryRuleFilePathRestrictionDict",
    "RepositoryRuleFilePathRestrictionParametersDict",
    "RepositoryRuleMaxFilePathLengthDict",
    "RepositoryRuleMaxFilePathLengthParametersDict",
    "RepositoryRuleMaxFileSizeDict",
    "RepositoryRuleMaxFileSizeParametersDict",
    "RepositoryRuleMergeQueueDict",
    "RepositoryRuleMergeQueueParametersDict",
    "RepositoryRuleNonFastForwardDict",
    "RepositoryRuleParamsCodeScanningToolDict",
    "RepositoryRuleParamsRequiredReviewerConfigurationDict",
    "RepositoryRuleParamsReviewerDict",
    "RepositoryRuleParamsStatusCheckConfigurationDict",
    "RepositoryRuleParamsWorkflowFileReferenceDict",
    "RepositoryRulePullRequestDict",
    "RepositoryRulePullRequestParametersDict",
    "RepositoryRuleRequiredDeploymentsDict",
    "RepositoryRuleRequiredDeploymentsParametersDict",
    "RepositoryRuleRequiredLinearHistoryDict",
    "RepositoryRuleRequiredSignaturesDict",
    "RepositoryRuleRequiredStatusChecksDict",
    "RepositoryRuleRequiredStatusChecksParametersDict",
    "RepositoryRuleTagNamePatternDict",
    "RepositoryRuleTagNamePatternParametersDict",
    "RepositoryRuleUpdateDict",
    "RepositoryRuleUpdateParametersDict",
    "RepositoryRuleWorkflowsDict",
    "RepositoryRuleWorkflowsParametersDict",
    "RepositoryRulesetBypassActorDict",
    "RepositoryRulesetConditionsDict",
    "RepositoryRulesetConditionsRefNameDict",
    "RepositoryRulesetCreatedPayloadDict",
    "RepositoryRulesetDeletedPayloadDict",
    "RepositoryRulesetDict",
    "RepositoryRulesetEditedPayloadChangesConditionsDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionTypeDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExcludeDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesIncludeDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTargetDict",
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedDict",
    "RepositoryRulesetEditedPayloadChangesDict",
    "RepositoryRulesetEditedPayloadChangesEnforcementDict",
    "RepositoryRulesetEditedPayloadChangesNameDict",
    "RepositoryRulesetEditedPayloadChangesRulesDict",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfigurationDict",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesDict",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPatternDict",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleTypeDict",
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedDict",
    "RepositoryRulesetEditedPayloadDict",
    "RepositoryRulesetLinksDict",
    "RepositoryRulesetLinksSelfDict",
    "RepositoryTransferredPayloadChangesDict",
    "RepositoryTransferredPayloadChangesOwnerDict",
    "RepositoryTransferredPayloadChangesOwnerFromDict",
    "RepositoryTransferredPayloadChangesOwnerFromOrganizationDict",
    "RepositoryTransferredPayloadDict",
    "RepositoryUnarchivedPayloadDict",
    "RepositoryVulnerabilityAlertCreatePayloadDict",
    "RepositoryVulnerabilityAlertDismissPayloadAlertDict",
    "RepositoryVulnerabilityAlertDismissPayloadDict",
    "RepositoryVulnerabilityAlertReopenPayloadDict",
    "RepositoryVulnerabilityAlertResolvePayloadAlertDict",
    "RepositoryVulnerabilityAlertResolvePayloadDict",
    "SecretScanningAlertAssignedPayloadDict",
    "SecretScanningAlertCreatedPayloadDict",
    "SecretScanningAlertLocationCreatedPayloadDict",
    "SecretScanningAlertPubliclyLeakedPayloadDict",
    "SecretScanningAlertReopenedPayloadDict",
    "SecretScanningAlertResolvedPayloadDict",
    "SecretScanningAlertUnassignedPayloadDict",
    "SecretScanningAlertValidatedPayloadDict",
    "SecretScanningAlertWebhookDict",
    "SecretScanningLocationCommitDict",
    "SecretScanningLocationDict",
    "SecretScanningLocationDiscussionBodyDict",
    "SecretScanningLocationDiscussionCommentDict",
    "SecretScanningLocationDiscussionTitleDict",
    "SecretScanningLocationIssueBodyDict",
    "SecretScanningLocationIssueCommentDict",
    "SecretScanningLocationIssueTitleDict",
    "SecretScanningLocationPullRequestBodyDict",
    "SecretScanningLocationPullRequestCommentDict",
    "SecretScanningLocationPullRequestReviewCommentDict",
    "SecretScanningLocationPullRequestReviewDict",
    "SecretScanningLocationPullRequestTitleDict",
    "SecretScanningLocationWikiCommitDict",
    "SecretScanningScanCompletedPayloadDict",
    "SecurityAdvisoryPublishedPayloadDict",
    "SecurityAdvisoryUpdatedPayloadDict",
    "SecurityAdvisoryWithdrawnPayloadDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvssDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCweDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifierDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReferenceDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityDict",
    "SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackageDict",
    "SecurityAndAnalysisPayloadChangesDict",
    "SecurityAndAnalysisPayloadChangesFromDict",
    "SecurityAndAnalysisPayloadDict",
    "SimpleCheckSuiteDict",
    "SimpleCommitDict",
    "SponsorshipCancelledPayloadDict",
    "SponsorshipCreatedPayloadDict",
    "SponsorshipEditedPayloadChangesDict",
    "SponsorshipEditedPayloadChangesPrivacyLevelDict",
    "SponsorshipEditedPayloadDict",
    "SponsorshipPendingCancellationPayloadDict",
    "SponsorshipPendingTierChangePayloadDict",
    "SponsorshipTierChangedPayloadDict",
    "StarCreatedPayloadDict",
    "StarDeletedPayloadDict",
    "StatusPayloadBrancheCommitDict",
    "StatusPayloadBrancheDict",
    "StatusPayloadCommitCommitDict",
    "StatusPayloadCommitCommitTreeDict",
    "StatusPayloadCommitCommitVerificationDict",
    "StatusPayloadCommitDict",
    "StatusPayloadCommitParentDict",
    "StatusPayloadDict",
    "SubIssuesParentIssueAddedPayloadDict",
    "SubIssuesParentIssueRemovedPayloadDict",
    "SubIssuesSubIssueAddedPayloadDict",
    "SubIssuesSubIssueRemovedPayloadDict",
    "SubIssuesSummaryDict",
    "TeamAddPayloadDict",
    "TeamAddedToRepositoryPayloadDict",
    "TeamAddedToRepositoryPayloadRepositoryDict",
    "TeamAddedToRepositoryPayloadRepositoryPermissionsDict",
    "TeamCreatedPayloadDict",
    "TeamCreatedPayloadRepositoryDict",
    "TeamCreatedPayloadRepositoryPermissionsDict",
    "TeamDeletedPayloadDict",
    "TeamDeletedPayloadRepositoryDict",
    "TeamDeletedPayloadRepositoryPermissionsDict",
    "TeamEditedPayloadChangesDescriptionDict",
    "TeamEditedPayloadChangesDict",
    "TeamEditedPayloadChangesNameDict",
    "TeamEditedPayloadChangesNotificationSettingDict",
    "TeamEditedPayloadChangesPrivacyDict",
    "TeamEditedPayloadChangesRepositoryDict",
    "TeamEditedPayloadChangesRepositoryPermissionsDict",
    "TeamEditedPayloadChangesRepositoryPermissionsFromDict",
    "TeamEditedPayloadDict",
    "TeamEditedPayloadRepositoryDict",
    "TeamEditedPayloadRepositoryPermissionsDict",
    "TeamRemovedFromRepositoryPayloadDict",
    "TeamRemovedFromRepositoryPayloadRepositoryDict",
    "TeamRemovedFromRepositoryPayloadRepositoryPermissionsDict",
    "UserDict",
    "WatchStartedPayloadDict",
    "WebhookPayload",
    "WebhookRubygemsMetadataDict",
    "WebhookRubygemsMetadataVersionInfoDict",
    "WebhooksAlertDict",
    "WebhooksAnswerDict",
    "WebhooksAnswerReactionsDict",
    "WebhooksApproverDict",
    "WebhooksChanges8Dict",
    "WebhooksChanges8TierDict",
    "WebhooksChanges8TierFromDict",
    "WebhooksChangesBodyDict",
    "WebhooksChangesDict",
    "WebhooksCommentDict",
    "WebhooksCommentReactionsDict",
    "WebhooksDeployKeyDict",
    "WebhooksIssue2Dict",
    "WebhooksIssue2LabelDict",
    "WebhooksIssue2PullRequestDict",
    "WebhooksIssue2ReactionsDict",
    "WebhooksIssueCommentDict",
    "WebhooksIssueCommentReactionsDict",
    "WebhooksIssueDict",
    "WebhooksIssueLabelDict",
    "WebhooksIssuePullRequestDict",
    "WebhooksIssueReactionsDict",
    "WebhooksLabelDict",
    "WebhooksMarketplacePurchaseAccountDict",
    "WebhooksMarketplacePurchaseDict",
    "WebhooksMarketplacePurchasePlanDict",
    "WebhooksMembershipDict",
    "WebhooksMilestoneDict",
    "WebhooksPreviousMarketplacePurchaseAccountDict",
    "WebhooksPreviousMarketplacePurchaseDict",
    "WebhooksPreviousMarketplacePurchasePlanDict",
    "WebhooksProjectCardDict",
    "WebhooksProjectChangesArchivedAtDict",
    "WebhooksProjectChangesDict",
    "WebhooksProjectColumnDict",
    "WebhooksProjectDict",
    "WebhooksPullRequest5BaseDict",
    "WebhooksPullRequest5BaseRepoDict",
    "WebhooksPullRequest5BaseRepoPermissionsDict",
    "WebhooksPullRequest5Dict",
    "WebhooksPullRequest5HeadDict",
    "WebhooksPullRequest5HeadRepoDict",
    "WebhooksPullRequest5HeadRepoPermissionsDict",
    "WebhooksPullRequest5LabelDict",
    "WebhooksPullRequest5LinksCommentsDict",
    "WebhooksPullRequest5LinksCommitsDict",
    "WebhooksPullRequest5LinksDict",
    "WebhooksPullRequest5LinksHtmlDict",
    "WebhooksPullRequest5LinksIssueDict",
    "WebhooksPullRequest5LinksReviewCommentDict",
    "WebhooksPullRequest5LinksReviewCommentsDict",
    "WebhooksPullRequest5LinksSelfDict",
    "WebhooksPullRequest5LinksStatusesDict",
    "WebhooksPullRequest5RequestedReviewerOption2Dict",
    "WebhooksPullRequest5RequestedTeamDict",
    "WebhooksRelease1Dict",
    "WebhooksRelease1ReactionsDict",
    "WebhooksReleaseAssetDict",
    "WebhooksReleaseDict",
    "WebhooksReleaseReactionsDict",
    "WebhooksReviewCommentDict",
    "WebhooksReviewCommentLinksDict",
    "WebhooksReviewCommentLinksHtmlDict",
    "WebhooksReviewCommentLinksPullRequestDict",
    "WebhooksReviewCommentLinksSelfDict",
    "WebhooksReviewCommentReactionsDict",
    "WebhooksReviewDict",
    "WebhooksReviewLinksDict",
    "WebhooksReviewLinksHtmlDict",
    "WebhooksReviewLinksPullRequestDict",
    "WebhooksRuleDict",
    "WebhooksSecurityAdvisoryCvssDict",
    "WebhooksSecurityAdvisoryCweDict",
    "WebhooksSecurityAdvisoryDict",
    "WebhooksSecurityAdvisoryIdentifierDict",
    "WebhooksSecurityAdvisoryReferenceDict",
    "WebhooksSecurityAdvisoryVulnerabilityDict",
    "WebhooksSecurityAdvisoryVulnerabilityPackageDict",
    "WebhooksSponsorshipDict",
    "WebhooksSponsorshipMaintainerDict",
    "WebhooksSponsorshipTierDict",
    "WebhooksTeam1Dict",
    "WebhooksTeamDict",
    "WebhooksWorkflowJobRunDict",
    "WorkflowDispatchPayloadDict",
    "WorkflowJobCompletedPayloadDict",
    "WorkflowJobInProgressPayloadDict",
    "WorkflowJobQueuedPayloadDict",
    "WorkflowJobQueuedPayloadWorkflowJobDict",
    "WorkflowJobQueuedPayloadWorkflowJobStepDict",
    "WorkflowJobWaitingPayloadDict",
    "WorkflowJobWaitingPayloadWorkflowJobDict",
    "WorkflowJobWaitingPayloadWorkflowJobStepDict",
    "WorkflowRunCompletedPayloadDict",
    "WorkflowRunCompletedPayloadWorkflowRunDict",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthorDict",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitterDict",
    "WorkflowRunCompletedPayloadWorkflowRunHeadCommitDict",
    "WorkflowRunCompletedPayloadWorkflowRunHeadRepositoryDict",
    "WorkflowRunCompletedPayloadWorkflowRunRepositoryDict",
    "WorkflowRunInProgressPayloadDict",
    "WorkflowRunInProgressPayloadWorkflowRunDict",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthorDict",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitterDict",
    "WorkflowRunInProgressPayloadWorkflowRunHeadCommitDict",
    "WorkflowRunInProgressPayloadWorkflowRunHeadRepositoryDict",
    "WorkflowRunInProgressPayloadWorkflowRunRepositoryDict",
    "WorkflowRunRequestedPayloadDict",
    "WorkflowRunRequestedPayloadWorkflowRunDict",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthorDict",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitterDict",
    "WorkflowRunRequestedPayloadWorkflowRunHeadCommitDict",
    "WorkflowRunRequestedPayloadWorkflowRunHeadRepositoryDict",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseDict",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepoDict",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestDict",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadDict",
    "WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepoDict",
    "WorkflowRunRequestedPayloadWorkflowRunRepositoryDict",
]

BranchProtectionRuleEditedPayloadChangesAdminEnforcedDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesAdminEnforcedDict",
    {
        "from": Required[None | bool],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesAdminEnforcedDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesAdminEnforced."""
)

BranchProtectionRuleEditedPayloadChangesAuthorizedActorNamesDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorNamesDict",
    {
        "from": Required[list[str]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesAuthorizedActorNamesDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesAuthorizedActorNames."""
)

BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnlyDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnlyDict",
    {
        "from": Required[None | bool],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnlyDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnly."""
)

BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnlyDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnlyDict",
    {
        "from": Required[None | bool],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnlyDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnly."""
)

BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevelDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevelDict",
    {
        "from": Required[Literal["off", "non_admins", "everyone"]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevelDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevel."""
)

BranchProtectionRuleEditedPayloadChangesLockAllowsForkSyncDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesLockAllowsForkSyncDict",
    {
        "from": Required[None | bool],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesLockAllowsForkSyncDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesLockAllowsForkSync."""
)

BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevelDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevelDict",
    {
        "from": Required[Literal["off", "non_admins", "everyone"]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevelDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevel."""
)

BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevelDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevelDict",
    {
        "from": Required[Literal["off", "non_admins", "everyone"]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevelDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevel."""
)

BranchProtectionRuleEditedPayloadChangesRequireLastPushApprovalDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesRequireLastPushApprovalDict",
    {
        "from": Required[None | bool],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesRequireLastPushApprovalDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesRequireLastPushApproval."""
)

BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksDict",
    {
        "from": Required[list[str]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesRequiredStatusChecks."""
)

BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevelDict = TypedDict(
    "BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevelDict",
    {
        "from": Required[Literal["off", "non_admins", "everyone"]],
    },
    total=False,
)
BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevelDict.__doc__ = (
    """BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevel."""
)


class CheckRunRequestedActionPayloadRequestedActionDict(TypedDict, total=False):
    """The action requested by the user."""

    identifier: NotRequired[str]


class CheckRunWithSimpleCheckSuiteOutputDict(TypedDict, total=False):
    """CheckRunWithSimpleCheckSuiteOutput."""

    annotations_count: Required[int]
    annotations_url: Required[str]
    summary: Required[None | str]
    text: Required[None | str]
    title: Required[None | str]


class CheckSuiteCompletedPayloadCheckSuiteAppPermissionsDict(TypedDict, total=False):
    """The set of permissions for the GitHub app."""

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CheckSuiteRequestedPayloadCheckSuiteAppPermissionsDict(TypedDict, total=False):
    """The set of permissions for the GitHub app."""

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    artifact_metadata: NotRequired[Literal["read", "write"]]
    attestations: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    copilot_requests: NotRequired[Literal["write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    merge_queues: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    models: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CheckSuiteRerequestedPayloadCheckSuiteAppPermissionsDict(TypedDict, total=False):
    """The set of permissions for the GitHub app."""

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    artifact_metadata: NotRequired[Literal["read", "write"]]
    attestations: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    copilot_requests: NotRequired[Literal["write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    merge_queues: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    models: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class CodeScanningAlertAppearedInBranchPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertAppearedInBranchPayloadAlertRule."""

    description: Required[str]
    id: Required[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]


class CodeScanningAlertAppearedInBranchPayloadAlertToolDict(TypedDict, total=False):
    """CodeScanningAlertAppearedInBranchPayloadAlertTool."""

    name: Required[str]
    version: Required[None | str]


class CodeScanningAlertClosedByUserPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertClosedByUserPayloadAlertRule."""

    description: Required[str]
    full_description: NotRequired[str]
    help: NotRequired[None | str]
    help_uri: NotRequired[None | str]
    id: Required[str]
    name: NotRequired[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]
    tags: NotRequired[Any | None]


class CodeScanningAlertClosedByUserPayloadAlertToolDict(TypedDict, total=False):
    """CodeScanningAlertClosedByUserPayloadAlertTool."""

    guid: NotRequired[None | str]
    name: Required[str]
    version: Required[None | str]


class CodeScanningAlertCreatedPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertCreatedPayloadAlertRule."""

    description: Required[str]
    full_description: NotRequired[str]
    help: NotRequired[None | str]
    help_uri: NotRequired[None | str]
    id: Required[str]
    name: NotRequired[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]
    tags: NotRequired[Any | None]


class CodeScanningAlertFixedPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertFixedPayloadAlertRule."""

    description: Required[str]
    full_description: NotRequired[str]
    help: NotRequired[None | str]
    help_uri: NotRequired[None | str]
    id: Required[str]
    name: NotRequired[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]
    tags: NotRequired[Any | None]


class CodeScanningAlertFixedPayloadAlertToolDict(TypedDict, total=False):
    """CodeScanningAlertFixedPayloadAlertTool."""

    guid: NotRequired[None | str]
    name: Required[str]
    version: Required[None | str]


class CodeScanningAlertReopenedByUserPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertReopenedByUserPayloadAlertRule."""

    description: Required[str]
    id: Required[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]


class CodeScanningAlertReopenedByUserPayloadAlertToolDict(TypedDict, total=False):
    """CodeScanningAlertReopenedByUserPayloadAlertTool."""

    name: Required[str]
    version: Required[None | str]


class CodeScanningAlertReopenedPayloadAlertRuleDict(TypedDict, total=False):
    """CodeScanningAlertReopenedPayloadAlertRule."""

    description: Required[str]
    full_description: NotRequired[str]
    help: NotRequired[None | str]
    help_uri: NotRequired[None | str]
    id: Required[str]
    name: NotRequired[str]
    severity: Required[Literal["none", "note", "warning", "error"] | None]
    tags: NotRequired[Any | None]


class CodeScanningAlertReopenedPayloadAlertToolDict(TypedDict, total=False):
    """CodeScanningAlertReopenedPayloadAlertTool."""

    guid: NotRequired[None | str]
    name: Required[str]
    version: Required[None | str]


CommitCommentCreatedPayloadCommentReactionsDict = TypedDict(
    "CommitCommentCreatedPayloadCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
CommitCommentCreatedPayloadCommentReactionsDict.__doc__ = """Reactions."""


class CustomPropertyDeletedPayloadDefinitionDict(TypedDict, total=False):
    """CustomPropertyDeletedPayloadDefinition."""

    property_name: Required[str]


class DependabotAlertSecurityAdvisoryCvssDict(TypedDict, total=False):
    """Details for the advisory pertaining to the Common Vulnerability Scoring System."""

    score: Required[float]
    vector_string: Required[None | str]


class DependabotAlertSecurityAdvisoryCweDict(TypedDict, total=False):
    """A CWE weakness assigned to the advisory."""

    cwe_id: Required[str]
    name: Required[str]


class DependabotAlertSecurityAdvisoryIdentifierDict(TypedDict, total=False):
    """An advisory identifier."""

    type: Required[Literal["CVE", "GHSA"]]
    value: Required[str]


class DependabotAlertSecurityAdvisoryReferenceDict(TypedDict, total=False):
    """A link to additional advisory information."""

    url: Required[str]


class DeploymentCreatedPayloadDeploymentDict(TypedDict, total=False):
    """The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments)."""

    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    environment: Required[str]
    id: Required[int]
    node_id: Required[str]
    original_environment: Required[str]
    payload: Required[dict[str, Any] | str]
    performed_via_github_app: NotRequired[Any | None]
    production_environment: NotRequired[bool]
    ref: Required[str]
    repository_url: Required[str]
    sha: Required[str]
    statuses_url: Required[str]
    task: Required[str]
    transient_environment: NotRequired[bool]
    updated_at: Required[str]
    url: Required[str]


class DeploymentReviewApprovedPayloadReviewerDict(TypedDict, total=False):
    """DeploymentReviewApprovedPayloadReviewer."""

    reviewer: NotRequired[Any | None]
    type: NotRequired[Literal["User"]]


class DeploymentReviewApprovedPayloadWorkflowJobRunDict(TypedDict, total=False):
    """DeploymentReviewApprovedPayloadWorkflowJobRun."""

    conclusion: NotRequired[None]
    created_at: NotRequired[str]
    environment: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[None | str]
    status: NotRequired[str]
    updated_at: NotRequired[str]


class DeploymentReviewRejectedPayloadReviewerDict(TypedDict, total=False):
    """DeploymentReviewRejectedPayloadReviewer."""

    reviewer: NotRequired[Any | None]
    type: NotRequired[Literal["User"]]


class DeploymentReviewRejectedPayloadWorkflowJobRunDict(TypedDict, total=False):
    """DeploymentReviewRejectedPayloadWorkflowJobRun."""

    conclusion: NotRequired[None | str]
    created_at: NotRequired[str]
    environment: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[None | str]
    status: NotRequired[str]
    updated_at: NotRequired[str]


class DeploymentReviewRequestedPayloadReviewerDict(TypedDict, total=False):
    """DeploymentReviewRequestedPayloadReviewer."""

    reviewer: NotRequired[Any | None]
    type: NotRequired[Literal["User", "Team"]]


class DeploymentReviewRequestedPayloadWorkflowJobRunDict(TypedDict, total=False):
    """DeploymentReviewRequestedPayloadWorkflowJobRun."""

    conclusion: Required[None]
    created_at: Required[str]
    environment: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[None | str]
    status: Required[str]
    updated_at: Required[str]


class DeploymentStatusCreatedPayloadDeploymentDict(TypedDict, total=False):
    """The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments)."""

    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    environment: Required[str]
    id: Required[int]
    node_id: Required[str]
    original_environment: Required[str]
    payload: Required[dict[str, Any] | str]
    performed_via_github_app: NotRequired[Any | None]
    production_environment: NotRequired[bool]
    ref: Required[str]
    repository_url: Required[str]
    sha: Required[str]
    statuses_url: Required[str]
    task: Required[str]
    transient_environment: NotRequired[bool]
    updated_at: Required[str]
    url: Required[str]


class DeploymentStatusCreatedPayloadDeploymentStatusDict(TypedDict, total=False):
    """The [deployment status](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses)."""

    created_at: Required[str]
    creator: Required[Any | None]
    deployment_url: Required[str]
    description: Required[str]
    environment: Required[str]
    environment_url: NotRequired[str]
    id: Required[int]
    log_url: NotRequired[str]
    node_id: Required[str]
    performed_via_github_app: NotRequired[Any | None]
    repository_url: Required[str]
    state: Required[str]
    target_url: Required[str]
    updated_at: Required[str]
    url: Required[str]


class DiscussionCategoryDict(TypedDict, total=False):
    """DiscussionCategory."""

    created_at: Required[str]
    description: Required[str]
    emoji: Required[str]
    id: Required[int]
    is_answerable: Required[bool]
    name: Required[str]
    node_id: NotRequired[str]
    repository_id: Required[int]
    slug: Required[str]
    updated_at: Required[str]


DiscussionReactionsDict = TypedDict(
    "DiscussionReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
DiscussionReactionsDict.__doc__ = """Reactions."""


class DiscussionCategoryChangedPayloadChangesCategoryFromDict(TypedDict, total=False):
    """DiscussionCategoryChangedPayloadChangesCategoryFrom."""

    created_at: Required[str]
    description: Required[str]
    emoji: Required[str]
    id: Required[int]
    is_answerable: Required[bool]
    name: Required[str]
    node_id: NotRequired[str]
    repository_id: Required[int]
    slug: Required[str]
    updated_at: Required[str]


DiscussionCommentEditedPayloadChangesBodyDict = TypedDict(
    "DiscussionCommentEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
DiscussionCommentEditedPayloadChangesBodyDict.__doc__ = """DiscussionCommentEditedPayloadChangesBody."""

DiscussionEditedPayloadChangesBodyDict = TypedDict(
    "DiscussionEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
DiscussionEditedPayloadChangesBodyDict.__doc__ = """DiscussionEditedPayloadChangesBody."""

DiscussionEditedPayloadChangesTitleDict = TypedDict(
    "DiscussionEditedPayloadChangesTitleDict",
    {
        "from": Required[str],
    },
    total=False,
)
DiscussionEditedPayloadChangesTitleDict.__doc__ = """DiscussionEditedPayloadChangesTitle."""


class FullRepositoryPermissionsDict(TypedDict, total=False):
    """FullRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    push: Required[bool]
    triage: NotRequired[bool]
    pull: Required[bool]


class GollumPayloadPageDict(TypedDict, total=False):
    """GollumPayloadPage."""

    action: Required[Literal["created", "edited"]]
    html_url: Required[str]
    page_name: Required[str]
    sha: Required[str]
    summary: Required[None | str]
    title: Required[str]


class InstallationCreatedPayloadRepositoryDict(TypedDict, total=False):
    """InstallationCreatedPayloadRepository."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationDeletedPayloadRepositoryDict(TypedDict, total=False):
    """InstallationDeletedPayloadRepository."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationNewPermissionsAcceptedPayloadRepositoryDict(TypedDict, total=False):
    """InstallationNewPermissionsAcceptedPayloadRepository."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationRepositoriesAddedPayloadRepositoriesAddedDict(TypedDict, total=False):
    """InstallationRepositoriesAddedPayloadRepositoriesAdded."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationRepositoriesAddedPayloadRepositoriesRemovedDict(TypedDict, total=False):
    """InstallationRepositoriesAddedPayloadRepositoriesRemoved."""

    full_name: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[str]
    node_id: NotRequired[str]
    private: NotRequired[bool]


class InstallationRepositoriesRemovedPayloadRepositoriesAddedDict(TypedDict, total=False):
    """InstallationRepositoriesRemovedPayloadRepositoriesAdded."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationRepositoriesRemovedPayloadRepositoriesRemovedDict(TypedDict, total=False):
    """InstallationRepositoriesRemovedPayloadRepositoriesRemoved."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationSuspendPayloadRepositoryDict(TypedDict, total=False):
    """InstallationSuspendPayloadRepository."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class InstallationTargetRenamedPayloadAccountDict(TypedDict, total=False):
    """InstallationTargetRenamedPayloadAccount."""

    archived_at: NotRequired[None | str]
    avatar_url: Required[str]
    created_at: NotRequired[str]
    description: NotRequired[None]
    events_url: NotRequired[str]
    followers: NotRequired[int]
    followers_url: NotRequired[str]
    following: NotRequired[int]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    has_organization_projects: NotRequired[bool]
    has_repository_projects: NotRequired[bool]
    hooks_url: NotRequired[str]
    html_url: Required[str]
    id: Required[int]
    is_verified: NotRequired[bool]
    issues_url: NotRequired[str]
    login: NotRequired[str]
    members_url: NotRequired[str]
    name: NotRequired[str]
    node_id: Required[str]
    organizations_url: NotRequired[str]
    public_gists: NotRequired[int]
    public_members_url: NotRequired[str]
    public_repos: NotRequired[int]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    slug: NotRequired[str]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    website_url: NotRequired[None]
    user_view_type: NotRequired[str]


InstallationTargetRenamedPayloadChangesLoginDict = TypedDict(
    "InstallationTargetRenamedPayloadChangesLoginDict",
    {
        "from": Required[str],
    },
    total=False,
)
InstallationTargetRenamedPayloadChangesLoginDict.__doc__ = """InstallationTargetRenamedPayloadChangesLogin."""

InstallationTargetRenamedPayloadChangesSlugDict = TypedDict(
    "InstallationTargetRenamedPayloadChangesSlugDict",
    {
        "from": Required[str],
    },
    total=False,
)
InstallationTargetRenamedPayloadChangesSlugDict.__doc__ = """InstallationTargetRenamedPayloadChangesSlug."""


class InstallationUnsuspendPayloadRepositoryDict(TypedDict, total=False):
    """InstallationUnsuspendPayloadRepository."""

    full_name: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    private: Required[bool]


class IssueLabelOption2Dict(TypedDict, total=False):
    """IssueLabelOption2."""

    id: NotRequired[int]
    node_id: NotRequired[str]
    url: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[None | str]
    color: NotRequired[None | str]
    default: NotRequired[bool]


class IssuePullRequestDict(TypedDict, total=False):
    """IssuePullRequest."""

    merged_at: NotRequired[None | str]
    diff_url: Required[None | str]
    html_url: Required[None | str]
    patch_url: Required[None | str]
    url: Required[None | str]


IssueCommentCreatedPayloadCommentReactionsDict = TypedDict(
    "IssueCommentCreatedPayloadCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssueCommentCreatedPayloadCommentReactionsDict.__doc__ = """Reactions."""


class IssuesDeletedPayloadIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class IssuesDeletedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesDeletedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesDeletedPayloadIssueReactionsDict = TypedDict(
    "IssuesDeletedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesDeletedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesDemilestonedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesDemilestonedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesDemilestonedPayloadIssueReactionsDict = TypedDict(
    "IssuesDemilestonedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesDemilestonedPayloadIssueReactionsDict.__doc__ = """Reactions."""

IssuesEditedPayloadChangesBodyDict = TypedDict(
    "IssuesEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
IssuesEditedPayloadChangesBodyDict.__doc__ = """IssuesEditedPayloadChangesBody."""

IssuesEditedPayloadChangesTitleDict = TypedDict(
    "IssuesEditedPayloadChangesTitleDict",
    {
        "from": Required[str],
    },
    total=False,
)
IssuesEditedPayloadChangesTitleDict.__doc__ = """IssuesEditedPayloadChangesTitle."""


class IssuesEditedPayloadIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class IssuesEditedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesEditedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesEditedPayloadIssueReactionsDict = TypedDict(
    "IssuesEditedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesEditedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesLabeledPayloadIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class IssuesLabeledPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesLabeledPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesLabeledPayloadIssueReactionsDict = TypedDict(
    "IssuesLabeledPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesLabeledPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesLockedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesLockedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesLockedPayloadIssueReactionsDict = TypedDict(
    "IssuesLockedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesLockedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesMilestonedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesMilestonedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesMilestonedPayloadIssueReactionsDict = TypedDict(
    "IssuesMilestonedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesMilestonedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesOpenedPayloadChangesOldRepositoryPermissionsDict(TypedDict, total=False):
    """IssuesOpenedPayloadChangesOldRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class IssuesOpenedPayloadIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class IssuesOpenedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesOpenedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesOpenedPayloadIssueReactionsDict = TypedDict(
    "IssuesOpenedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesOpenedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesReopenedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesReopenedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesReopenedPayloadIssueReactionsDict = TypedDict(
    "IssuesReopenedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesReopenedPayloadIssueReactionsDict.__doc__ = """Reactions."""


class IssuesTransferredPayloadChangesNewIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class IssuesTransferredPayloadChangesNewIssuePullRequestDict(TypedDict, total=False):
    """IssuesTransferredPayloadChangesNewIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesTransferredPayloadChangesNewIssueReactionsDict = TypedDict(
    "IssuesTransferredPayloadChangesNewIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesTransferredPayloadChangesNewIssueReactionsDict.__doc__ = """Reactions."""


class IssuesTransferredPayloadChangesNewRepositoryPermissionsDict(TypedDict, total=False):
    """IssuesTransferredPayloadChangesNewRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class IssuesUnlockedPayloadIssuePullRequestDict(TypedDict, total=False):
    """IssuesUnlockedPayloadIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


IssuesUnlockedPayloadIssueReactionsDict = TypedDict(
    "IssuesUnlockedPayloadIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
IssuesUnlockedPayloadIssueReactionsDict.__doc__ = """Reactions."""

LabelEditedPayloadChangesColorDict = TypedDict(
    "LabelEditedPayloadChangesColorDict",
    {
        "from": Required[str],
    },
    total=False,
)
LabelEditedPayloadChangesColorDict.__doc__ = """LabelEditedPayloadChangesColor."""

LabelEditedPayloadChangesDescriptionDict = TypedDict(
    "LabelEditedPayloadChangesDescriptionDict",
    {
        "from": Required[str],
    },
    total=False,
)
LabelEditedPayloadChangesDescriptionDict.__doc__ = """LabelEditedPayloadChangesDescription."""

LabelEditedPayloadChangesNameDict = TypedDict(
    "LabelEditedPayloadChangesNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
LabelEditedPayloadChangesNameDict.__doc__ = """LabelEditedPayloadChangesName."""


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccountDict(TypedDict, total=False):
    """MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccount."""

    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organization_billing_email: Required[None | str]
    type: Required[str]


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlanDict(TypedDict, total=False):
    """MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlan."""

    bullets: Required[list[str]]
    description: Required[str]
    has_free_trial: Required[bool]
    id: Required[int]
    monthly_price_in_cents: Required[int]
    name: Required[str]
    price_model: Required[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: Required[None | str]
    yearly_price_in_cents: Required[int]


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccountDict(TypedDict, total=False):
    """MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccount."""

    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organization_billing_email: Required[None | str]
    type: Required[str]


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlanDict(TypedDict, total=False):
    """MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlan."""

    bullets: Required[list[str]]
    description: Required[str]
    has_free_trial: Required[bool]
    id: Required[int]
    monthly_price_in_cents: Required[int]
    name: Required[str]
    price_model: Required[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: Required[None | str]
    yearly_price_in_cents: Required[int]


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccountDict(TypedDict, total=False):
    """MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccount."""

    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organization_billing_email: Required[None | str]
    type: Required[str]


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlanDict(TypedDict, total=False):
    """MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlan."""

    bullets: Required[list[str]]
    description: Required[str]
    has_free_trial: Required[bool]
    id: Required[int]
    monthly_price_in_cents: Required[int]
    name: Required[str]
    price_model: Required[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: Required[None | str]
    yearly_price_in_cents: Required[int]


class MemberAddedPayloadChangesPermissionDict(TypedDict, total=False):
    """This field is included for legacy purposes; use the `role_name` field instead. The `maintain` role is mapped to `write` and the `triage` role is mapped to `read`. To determine the role assigned to the collaborator, use the `role_name` field instead, which will provide the full role name, including custom roles."""

    to: Required[Literal["write", "admin", "read"]]


class MemberAddedPayloadChangesRoleNameDict(TypedDict, total=False):
    """The role assigned to the collaborator."""

    to: Required[str]


MemberEditedPayloadChangesOldPermissionDict = TypedDict(
    "MemberEditedPayloadChangesOldPermissionDict",
    {
        "from": Required[str],
    },
    total=False,
)
MemberEditedPayloadChangesOldPermissionDict.__doc__ = """MemberEditedPayloadChangesOldPermission."""

MemberEditedPayloadChangesPermissionDict = TypedDict(
    "MemberEditedPayloadChangesPermissionDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
MemberEditedPayloadChangesPermissionDict.__doc__ = """MemberEditedPayloadChangesPermission."""


class MetaDeletedPayloadHookConfigDict(TypedDict, total=False):
    """MetaDeletedPayloadHookConfig."""

    content_type: Required[Literal["json", "form"]]
    insecure_ssl: Required[str]
    secret: NotRequired[str]
    url: Required[str]


class MilestoneClosedPayloadMilestoneDict(TypedDict, total=False):
    """A collection of related issues and pull requests."""

    closed_at: Required[str]
    closed_issues: Required[int]
    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    due_on: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    labels_url: Required[str]
    node_id: Required[str]
    number: Required[int]
    open_issues: Required[int]
    state: Required[Literal["closed"]]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]


class MilestoneCreatedPayloadMilestoneDict(TypedDict, total=False):
    """A collection of related issues and pull requests."""

    closed_at: Required[None]
    closed_issues: Required[int]
    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    due_on: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    labels_url: Required[str]
    node_id: Required[str]
    number: Required[int]
    open_issues: Required[int]
    state: Required[Literal["open"]]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]


MilestoneEditedPayloadChangesDescriptionDict = TypedDict(
    "MilestoneEditedPayloadChangesDescriptionDict",
    {
        "from": Required[str],
    },
    total=False,
)
MilestoneEditedPayloadChangesDescriptionDict.__doc__ = """MilestoneEditedPayloadChangesDescription."""

MilestoneEditedPayloadChangesDueOnDict = TypedDict(
    "MilestoneEditedPayloadChangesDueOnDict",
    {
        "from": Required[str],
    },
    total=False,
)
MilestoneEditedPayloadChangesDueOnDict.__doc__ = """MilestoneEditedPayloadChangesDueOn."""

MilestoneEditedPayloadChangesTitleDict = TypedDict(
    "MilestoneEditedPayloadChangesTitleDict",
    {
        "from": Required[str],
    },
    total=False,
)
MilestoneEditedPayloadChangesTitleDict.__doc__ = """MilestoneEditedPayloadChangesTitle."""


class MilestoneOpenedPayloadMilestoneDict(TypedDict, total=False):
    """A collection of related issues and pull requests."""

    closed_at: Required[None]
    closed_issues: Required[int]
    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    due_on: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    labels_url: Required[str]
    node_id: Required[str]
    number: Required[int]
    open_issues: Required[int]
    state: Required[Literal["open"]]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]


class MinimalRepositoryPermissionsDict(TypedDict, total=False):
    """MinimalRepositoryPermissions."""

    admin: NotRequired[bool]
    maintain: NotRequired[bool]
    push: NotRequired[bool]
    triage: NotRequired[bool]
    pull: NotRequired[bool]


class OrganizationMemberInvitedPayloadInvitationDict(TypedDict, total=False):
    """The invitation for the user or email if the action is `member_invited`."""

    created_at: Required[str]
    email: Required[None | str]
    failed_at: Required[None | str]
    failed_reason: Required[None | str]
    id: Required[float]
    invitation_teams_url: Required[str]
    inviter: Required[Any | None]
    login: Required[None | str]
    node_id: Required[str]
    role: Required[str]
    team_count: Required[float]
    invitation_source: NotRequired[str]


OrganizationRenamedPayloadChangesLoginDict = TypedDict(
    "OrganizationRenamedPayloadChangesLoginDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
OrganizationRenamedPayloadChangesLoginDict.__doc__ = """OrganizationRenamedPayloadChangesLogin."""


class PackagePublishedPayloadPackageDict(TypedDict, total=False):
    """Information about the package."""

    created_at: Required[None | str]
    description: Required[None | str]
    ecosystem: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    namespace: Required[str]
    owner: Required[Any | None]
    package_type: Required[str]
    package_version: Required[Any | None]
    registry: Required[Any | None]
    updated_at: Required[None | str]


class PackageUpdatedPayloadPackagePackageVersionDockerMetadataDict(TypedDict, total=False):
    """PackageUpdatedPayloadPackagePackageVersionDockerMetadata."""

    tags: NotRequired[list[str]]


class PackageUpdatedPayloadPackagePackageVersionPackageFileDict(TypedDict, total=False):
    """PackageUpdatedPayloadPackagePackageVersionPackageFile."""

    content_type: Required[str]
    created_at: Required[str]
    download_url: Required[str]
    id: Required[int]
    md5: Required[None | str]
    name: Required[str]
    sha1: Required[None | str]
    sha256: Required[str]
    size: Required[int]
    state: Required[str]
    updated_at: Required[str]


class PackageUpdatedPayloadPackagePackageVersionReleaseDict(TypedDict, total=False):
    """PackageUpdatedPayloadPackagePackageVersionRelease."""

    author: Required[Any | None]
    created_at: Required[str]
    draft: Required[bool]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    prerelease: Required[bool]
    published_at: Required[str]
    tag_name: Required[str]
    target_commitish: Required[str]
    url: Required[str]


class PageBuildPayloadBuildErrorDict(TypedDict, total=False):
    """PageBuildPayloadBuildError."""

    message: Required[None | str]


class PersonalAccessTokenRequestPermissionsAddedDict(TypedDict, total=False):
    """New requested permissions, categorized by type of permission."""

    organization: NotRequired[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    other: NotRequired[dict[str, Any]]


class PersonalAccessTokenRequestPermissionsResultDict(TypedDict, total=False):
    """Permissions requested, categorized by type of permission. This field incorporates `permissions_added` and `permissions_upgraded`."""

    organization: NotRequired[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    other: NotRequired[dict[str, Any]]


class PersonalAccessTokenRequestPermissionsUpgradedDict(TypedDict, total=False):
    """Requested permissions that elevate access for a previously approved request for access, categorized by type of permission."""

    organization: NotRequired[dict[str, Any]]
    repository: NotRequired[dict[str, Any]]
    other: NotRequired[dict[str, Any]]


class PingPayloadHookConfigDict(TypedDict, total=False):
    """PingPayloadHookConfig."""

    content_type: NotRequired[str]
    insecure_ssl: NotRequired[float | str]
    secret: NotRequired[str]
    url: NotRequired[str]


ProjectCardConvertedPayloadChangesNoteDict = TypedDict(
    "ProjectCardConvertedPayloadChangesNoteDict",
    {
        "from": Required[str],
    },
    total=False,
)
ProjectCardConvertedPayloadChangesNoteDict.__doc__ = """ProjectCardConvertedPayloadChangesNote."""


class ProjectCardDeletedPayloadProjectCardDict(TypedDict, total=False):
    """Project Card."""

    after_id: NotRequired[None | int]
    archived: Required[bool]
    column_id: Required[None | int]
    column_url: Required[str]
    content_url: NotRequired[str]
    created_at: Required[str]
    creator: Required[Any | None]
    id: Required[int]
    node_id: Required[str]
    note: Required[None | str]
    project_url: Required[str]
    updated_at: Required[str]
    url: Required[str]


ProjectCardEditedPayloadChangesNoteDict = TypedDict(
    "ProjectCardEditedPayloadChangesNoteDict",
    {
        "from": Required[None | str],
    },
    total=False,
)
ProjectCardEditedPayloadChangesNoteDict.__doc__ = """ProjectCardEditedPayloadChangesNote."""

ProjectCardMovedPayloadChangesColumnIdDict = TypedDict(
    "ProjectCardMovedPayloadChangesColumnIdDict",
    {
        "from": Required[int],
    },
    total=False,
)
ProjectCardMovedPayloadChangesColumnIdDict.__doc__ = """ProjectCardMovedPayloadChangesColumnId."""

ProjectColumnEditedPayloadChangesNameDict = TypedDict(
    "ProjectColumnEditedPayloadChangesNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
ProjectColumnEditedPayloadChangesNameDict.__doc__ = """ProjectColumnEditedPayloadChangesName."""

ProjectEditedPayloadChangesBodyDict = TypedDict(
    "ProjectEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
ProjectEditedPayloadChangesBodyDict.__doc__ = """ProjectEditedPayloadChangesBody."""

ProjectEditedPayloadChangesNameDict = TypedDict(
    "ProjectEditedPayloadChangesNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
ProjectEditedPayloadChangesNameDict.__doc__ = """ProjectEditedPayloadChangesName."""

ProjectsV2EditedPayloadChangesDescriptionDict = TypedDict(
    "ProjectsV2EditedPayloadChangesDescriptionDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2EditedPayloadChangesDescriptionDict.__doc__ = """ProjectsV2EditedPayloadChangesDescription."""

ProjectsV2EditedPayloadChangesPublicDict = TypedDict(
    "ProjectsV2EditedPayloadChangesPublicDict",
    {
        "from": NotRequired[bool],
        "to": NotRequired[bool],
    },
    total=False,
)
ProjectsV2EditedPayloadChangesPublicDict.__doc__ = """ProjectsV2EditedPayloadChangesPublic."""

ProjectsV2EditedPayloadChangesShortDescriptionDict = TypedDict(
    "ProjectsV2EditedPayloadChangesShortDescriptionDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2EditedPayloadChangesShortDescriptionDict.__doc__ = """ProjectsV2EditedPayloadChangesShortDescription."""

ProjectsV2EditedPayloadChangesTitleDict = TypedDict(
    "ProjectsV2EditedPayloadChangesTitleDict",
    {
        "from": NotRequired[str],
        "to": NotRequired[str],
    },
    total=False,
)
ProjectsV2EditedPayloadChangesTitleDict.__doc__ = """ProjectsV2EditedPayloadChangesTitle."""

ProjectsV2ItemConvertedPayloadChangesContentTypeDict = TypedDict(
    "ProjectsV2ItemConvertedPayloadChangesContentTypeDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[str],
    },
    total=False,
)
ProjectsV2ItemConvertedPayloadChangesContentTypeDict.__doc__ = """ProjectsV2ItemConvertedPayloadChangesContentType."""

ProjectsV2ItemEditedPayloadChangesOption2BodyDict = TypedDict(
    "ProjectsV2ItemEditedPayloadChangesOption2BodyDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2ItemEditedPayloadChangesOption2BodyDict.__doc__ = """ProjectsV2ItemEditedPayloadChangesOption2Body."""

ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeIdDict = TypedDict(
    "ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeIdDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeIdDict.__doc__ = (
    """ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeId."""
)

ProjectsV2StatusUpdateEditedPayloadChangesBodyDict = TypedDict(
    "ProjectsV2StatusUpdateEditedPayloadChangesBodyDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2StatusUpdateEditedPayloadChangesBodyDict.__doc__ = """ProjectsV2StatusUpdateEditedPayloadChangesBody."""

ProjectsV2StatusUpdateEditedPayloadChangesStartDateDict = TypedDict(
    "ProjectsV2StatusUpdateEditedPayloadChangesStartDateDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2StatusUpdateEditedPayloadChangesStartDateDict.__doc__ = (
    """ProjectsV2StatusUpdateEditedPayloadChangesStartDate."""
)

ProjectsV2StatusUpdateEditedPayloadChangesStatusDict = TypedDict(
    "ProjectsV2StatusUpdateEditedPayloadChangesStatusDict",
    {
        "from": NotRequired[Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None],
        "to": NotRequired[Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None],
    },
    total=False,
)
ProjectsV2StatusUpdateEditedPayloadChangesStatusDict.__doc__ = """ProjectsV2StatusUpdateEditedPayloadChangesStatus."""

ProjectsV2StatusUpdateEditedPayloadChangesTargetDateDict = TypedDict(
    "ProjectsV2StatusUpdateEditedPayloadChangesTargetDateDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
ProjectsV2StatusUpdateEditedPayloadChangesTargetDateDict.__doc__ = (
    """ProjectsV2StatusUpdateEditedPayloadChangesTargetDate."""
)


class PullRequestLabelDict(TypedDict, total=False):
    """PullRequestLabel."""

    id: Required[int]
    node_id: Required[str]
    url: Required[str]
    name: Required[str]
    description: Required[None | str]
    color: Required[str]
    default: Required[bool]


class PullRequestAssignedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestAssignedPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestAssignedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestAssignedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestAssignedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestAssignedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestAssignedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestAssignedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAssignedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestDequeuedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestDequeuedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestDequeuedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestDequeuedPayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestDequeuedPayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestDequeuedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestDequeuedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


PullRequestEditedPayloadChangesBodyDict = TypedDict(
    "PullRequestEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
PullRequestEditedPayloadChangesBodyDict.__doc__ = """PullRequestEditedPayloadChangesBody."""

PullRequestEditedPayloadChangesTitleDict = TypedDict(
    "PullRequestEditedPayloadChangesTitleDict",
    {
        "from": Required[str],
    },
    total=False,
)
PullRequestEditedPayloadChangesTitleDict.__doc__ = """PullRequestEditedPayloadChangesTitle."""

PullRequestEditedPayloadChangesBaseRefDict = TypedDict(
    "PullRequestEditedPayloadChangesBaseRefDict",
    {
        "from": Required[str],
    },
    total=False,
)
PullRequestEditedPayloadChangesBaseRefDict.__doc__ = """PullRequestEditedPayloadChangesBaseRef."""

PullRequestEditedPayloadChangesBaseShaDict = TypedDict(
    "PullRequestEditedPayloadChangesBaseShaDict",
    {
        "from": Required[str],
    },
    total=False,
)
PullRequestEditedPayloadChangesBaseShaDict.__doc__ = """PullRequestEditedPayloadChangesBaseSha."""


class PullRequestEnqueuedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestEnqueuedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestEnqueuedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestEnqueuedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestEnqueuedPayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestEnqueuedPayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestEnqueuedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestEnqueuedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestLabeledPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestLabeledPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestLabeledPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestLabeledPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestLabeledPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestLabeledPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestLabeledPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLabeledPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestLockedPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestLockedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestLockedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestLockedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestLockedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestLockedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestLockedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestLockedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestMinimalBaseRepoDict(TypedDict, total=False):
    """PullRequestMinimalBaseRepo."""

    id: Required[int]
    url: Required[str]
    name: Required[str]


class PullRequestMinimalHeadRepoDict(TypedDict, total=False):
    """PullRequestMinimalHeadRepo."""

    id: Required[int]
    url: Required[str]
    name: Required[str]


PullRequestReviewCommentCreatedPayloadCommentReactionsDict = TypedDict(
    "PullRequestReviewCommentCreatedPayloadCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
PullRequestReviewCommentCreatedPayloadCommentReactionsDict.__doc__ = """Reactions."""


class PullRequestReviewCommentCreatedPayloadCommentLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadCommentLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadCommentLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentCreatedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewCommentDeletedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentDeletedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewCommentEditedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentEditedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentEditedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewCommentEditedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewCommentEditedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewDismissedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewDismissedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestReviewDismissedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewDismissedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadReviewLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewDismissedPayloadReviewLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


PullRequestReviewEditedPayloadChangesBodyDict = TypedDict(
    "PullRequestReviewEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
PullRequestReviewEditedPayloadChangesBodyDict.__doc__ = """PullRequestReviewEditedPayloadChangesBody."""


class PullRequestReviewEditedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewEditedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewEditedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestReviewEditedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewEditedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewEditedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewEditedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewEditedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewSubmittedPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewSubmittedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewSubmittedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewSubmittedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadResolvedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


PullRequestReviewThreadResolvedPayloadThreadCommentReactionsDict = TypedDict(
    "PullRequestReviewThreadResolvedPayloadThreadCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
PullRequestReviewThreadResolvedPayloadThreadCommentReactionsDict.__doc__ = """Reactions."""


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


PullRequestReviewThreadUnresolvedPayloadThreadCommentReactionsDict = TypedDict(
    "PullRequestReviewThreadUnresolvedPayloadThreadCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
PullRequestReviewThreadUnresolvedPayloadThreadCommentReactionsDict.__doc__ = """Reactions."""


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestSynchronizePayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestSynchronizePayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestSynchronizePayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestSynchronizePayloadPullRequestHeadRepoPermissionsDict(TypedDict, total=False):
    """PullRequestSynchronizePayloadPullRequestHeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestSynchronizePayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestSynchronizePayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestUnassignedPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnassignedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestUnassignedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestUnassignedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestUnassignedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestUnassignedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnassignedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestUnlabeledPayloadPullRequestHead."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnlabeledPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    members_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    parent: NotRequired[Any | None]
    permission: Required[str]
    privacy: Required[Literal["open", "closed", "secret"]]
    repositories_url: Required[str]
    slug: Required[str]
    url: Required[str]


class PullRequestUnlabeledPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestUnlabeledPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestUnlabeledPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestUnlabeledPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlabeledPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestUnlockedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[Any | None]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnlockedPayloadPullRequestLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestUnlockedPayloadPullRequestRequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class PullRequestUnlockedPayloadPullRequestBaseRepoPermissionsDict(TypedDict, total=False):
    """PullRequestUnlockedPayloadPullRequestBaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class PullRequestUnlockedPayloadPullRequestLinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PullRequestUnlockedPayloadPullRequestLinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class PushPayloadPusherDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: NotRequired[None | str]
    name: Required[str]
    username: NotRequired[str]


class PushPayloadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class PushPayloadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class PushPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """PushPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class RegistryPackagePublishedPayloadRegistryPackageOwnerDict(TypedDict, total=False):
    """RegistryPackagePublishedPayloadRegistryPackageOwner."""

    avatar_url: Required[str]
    events_url: Required[str]
    followers_url: Required[str]
    following_url: Required[str]
    gists_url: Required[str]
    gravatar_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organizations_url: Required[str]
    received_events_url: Required[str]
    repos_url: Required[str]
    site_admin: Required[bool]
    starred_url: Required[str]
    subscriptions_url: Required[str]
    type: Required[str]
    url: Required[str]
    user_view_type: NotRequired[str]


class RegistryPackageUpdatedPayloadRegistryPackageOwnerDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackageOwner."""

    avatar_url: Required[str]
    events_url: Required[str]
    followers_url: Required[str]
    following_url: Required[str]
    gists_url: Required[str]
    gravatar_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organizations_url: Required[str]
    received_events_url: Required[str]
    repos_url: Required[str]
    site_admin: Required[bool]
    starred_url: Required[str]
    subscriptions_url: Required[str]
    type: Required[str]
    url: Required[str]
    user_view_type: NotRequired[str]


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthorDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthor."""

    avatar_url: Required[str]
    events_url: Required[str]
    followers_url: Required[str]
    following_url: Required[str]
    gists_url: Required[str]
    gravatar_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organizations_url: Required[str]
    received_events_url: Required[str]
    repos_url: Required[str]
    site_admin: Required[bool]
    starred_url: Required[str]
    subscriptions_url: Required[str]
    type: Required[str]
    url: Required[str]
    user_view_type: NotRequired[str]


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFileDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFile."""

    content_type: NotRequired[str]
    created_at: NotRequired[str]
    download_url: NotRequired[str]
    id: NotRequired[int]
    md5: NotRequired[None | str]
    name: NotRequired[str]
    sha1: NotRequired[None | str]
    sha256: NotRequired[str]
    size: NotRequired[int]
    state: NotRequired[str]
    updated_at: NotRequired[str]


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthorDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthor."""

    avatar_url: Required[str]
    events_url: Required[str]
    followers_url: Required[str]
    following_url: Required[str]
    gists_url: Required[str]
    gravatar_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organizations_url: Required[str]
    received_events_url: Required[str]
    repos_url: Required[str]
    site_admin: Required[bool]
    starred_url: Required[str]
    subscriptions_url: Required[str]
    type: Required[str]
    url: Required[str]
    user_view_type: NotRequired[str]


ReleaseEditedPayloadChangesBodyDict = TypedDict(
    "ReleaseEditedPayloadChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
ReleaseEditedPayloadChangesBodyDict.__doc__ = """ReleaseEditedPayloadChangesBody."""


class ReleaseEditedPayloadChangesMakeLatestDict(TypedDict, total=False):
    """ReleaseEditedPayloadChangesMakeLatest."""

    to: Required[bool]


ReleaseEditedPayloadChangesNameDict = TypedDict(
    "ReleaseEditedPayloadChangesNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
ReleaseEditedPayloadChangesNameDict.__doc__ = """ReleaseEditedPayloadChangesName."""

ReleaseEditedPayloadChangesTagNameDict = TypedDict(
    "ReleaseEditedPayloadChangesTagNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
ReleaseEditedPayloadChangesTagNameDict.__doc__ = """ReleaseEditedPayloadChangesTagName."""

ReleasePrereleasedPayloadReleaseReactionsDict = TypedDict(
    "ReleasePrereleasedPayloadReleaseReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
ReleasePrereleasedPayloadReleaseReactionsDict.__doc__ = """Reactions."""


class Repository2CodeSearchIndexStatusDict(TypedDict, total=False):
    """The status of the code search index for this repository."""

    lexical_search_ok: NotRequired[bool]
    lexical_commit_sha: NotRequired[str]


class Repository2PermissionsDict(TypedDict, total=False):
    """Repository2Permissions."""

    admin: Required[bool]
    pull: Required[bool]
    triage: NotRequired[bool]
    push: Required[bool]
    maintain: NotRequired[bool]


class RepositoryPermissionsDict(TypedDict, total=False):
    """RepositoryPermissions."""

    admin: Required[bool]
    pull: Required[bool]
    triage: NotRequired[bool]
    push: Required[bool]
    maintain: NotRequired[bool]


class RepositoryAdvisoryIdentifierDict(TypedDict, total=False):
    """RepositoryAdvisoryIdentifier."""

    type: Required[Literal["CVE", "GHSA"]]
    value: Required[str]


RepositoryEditedPayloadChangesDefaultBranchDict = TypedDict(
    "RepositoryEditedPayloadChangesDefaultBranchDict",
    {
        "from": Required[str],
    },
    total=False,
)
RepositoryEditedPayloadChangesDefaultBranchDict.__doc__ = """RepositoryEditedPayloadChangesDefaultBranch."""

RepositoryEditedPayloadChangesDescriptionDict = TypedDict(
    "RepositoryEditedPayloadChangesDescriptionDict",
    {
        "from": Required[None | str],
    },
    total=False,
)
RepositoryEditedPayloadChangesDescriptionDict.__doc__ = """RepositoryEditedPayloadChangesDescription."""

RepositoryEditedPayloadChangesHomepageDict = TypedDict(
    "RepositoryEditedPayloadChangesHomepageDict",
    {
        "from": Required[None | str],
    },
    total=False,
)
RepositoryEditedPayloadChangesHomepageDict.__doc__ = """RepositoryEditedPayloadChangesHomepage."""

RepositoryEditedPayloadChangesTopicsDict = TypedDict(
    "RepositoryEditedPayloadChangesTopicsDict",
    {
        "from": NotRequired[Any | None],
    },
    total=False,
)
RepositoryEditedPayloadChangesTopicsDict.__doc__ = """RepositoryEditedPayloadChangesTopics."""

RepositoryRenamedPayloadChangesRepositoryNameDict = TypedDict(
    "RepositoryRenamedPayloadChangesRepositoryNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
RepositoryRenamedPayloadChangesRepositoryNameDict.__doc__ = """RepositoryRenamedPayloadChangesRepositoryName."""


class RepositoryRuleBranchNamePatternParametersDict(TypedDict, total=False):
    """RepositoryRuleBranchNamePatternParameters."""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    pattern: Required[str]


class RepositoryRuleCommitAuthorEmailPatternParametersDict(TypedDict, total=False):
    """RepositoryRuleCommitAuthorEmailPatternParameters."""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    pattern: Required[str]


class RepositoryRuleCommitMessagePatternParametersDict(TypedDict, total=False):
    """RepositoryRuleCommitMessagePatternParameters."""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    pattern: Required[str]


class RepositoryRuleCommitterEmailPatternParametersDict(TypedDict, total=False):
    """RepositoryRuleCommitterEmailPatternParameters."""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    pattern: Required[str]


class RepositoryRuleCopilotCodeReviewParametersDict(TypedDict, total=False):
    """RepositoryRuleCopilotCodeReviewParameters."""

    review_draft_pull_requests: NotRequired[bool]
    review_on_push: NotRequired[bool]


class RepositoryRuleFileExtensionRestrictionParametersDict(TypedDict, total=False):
    """RepositoryRuleFileExtensionRestrictionParameters."""

    restricted_file_extensions: Required[list[str]]


class RepositoryRuleFilePathRestrictionParametersDict(TypedDict, total=False):
    """RepositoryRuleFilePathRestrictionParameters."""

    restricted_file_paths: Required[list[str]]


class RepositoryRuleMaxFilePathLengthParametersDict(TypedDict, total=False):
    """RepositoryRuleMaxFilePathLengthParameters."""

    max_file_path_length: Required[int]


class RepositoryRuleMaxFileSizeParametersDict(TypedDict, total=False):
    """RepositoryRuleMaxFileSizeParameters."""

    max_file_size: Required[int]


class RepositoryRuleMergeQueueParametersDict(TypedDict, total=False):
    """RepositoryRuleMergeQueueParameters."""

    check_response_timeout_minutes: Required[int]
    grouping_strategy: Required[Literal["ALLGREEN", "HEADGREEN"]]
    max_entries_to_build: Required[int]
    max_entries_to_merge: Required[int]
    merge_method: Required[Literal["MERGE", "SQUASH", "REBASE"]]
    min_entries_to_merge: Required[int]
    min_entries_to_merge_wait_minutes: Required[int]


class RepositoryRuleRequiredDeploymentsParametersDict(TypedDict, total=False):
    """RepositoryRuleRequiredDeploymentsParameters."""

    required_deployment_environments: Required[list[str]]


class RepositoryRuleTagNamePatternParametersDict(TypedDict, total=False):
    """RepositoryRuleTagNamePatternParameters."""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    pattern: Required[str]


class RepositoryRuleUpdateParametersDict(TypedDict, total=False):
    """RepositoryRuleUpdateParameters."""

    update_allows_fetch_and_merge: Required[bool]


class RepositoryRulesetConditionsRefNameDict(TypedDict, total=False):
    """RepositoryRulesetConditionsRefName."""

    include: NotRequired[list[str]]
    exclude: NotRequired[list[str]]


RepositoryRulesetEditedPayloadChangesEnforcementDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesEnforcementDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesEnforcementDict.__doc__ = """RepositoryRulesetEditedPayloadChangesEnforcement."""

RepositoryRulesetEditedPayloadChangesNameDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesNameDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesNameDict.__doc__ = """RepositoryRulesetEditedPayloadChangesName."""

RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionTypeDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionTypeDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionTypeDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionType."""
)

RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExcludeDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExcludeDict",
    {
        "from": NotRequired[list[str]],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExcludeDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExclude."""
)

RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesIncludeDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesIncludeDict",
    {
        "from": NotRequired[list[str]],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesIncludeDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesInclude."""
)

RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTargetDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTargetDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTargetDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTarget."""
)

RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfigurationDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfigurationDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfigurationDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfiguration."""
)

RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPatternDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPatternDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPatternDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPattern."""
)

RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleTypeDict = TypedDict(
    "RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleTypeDict",
    {
        "from": NotRequired[str],
    },
    total=False,
)
RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleTypeDict.__doc__ = (
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleType."""
)


class RepositoryRulesetLinksSelfDict(TypedDict, total=False):
    """RepositoryRulesetLinksSelf."""

    href: NotRequired[str]


class RepositoryTransferredPayloadChangesOwnerFromOrganizationDict(TypedDict, total=False):
    """Organization."""

    avatar_url: Required[str]
    description: Required[None | str]
    events_url: Required[str]
    hooks_url: Required[str]
    html_url: NotRequired[str]
    id: Required[int]
    issues_url: Required[str]
    login: Required[str]
    members_url: Required[str]
    node_id: Required[str]
    public_members_url: Required[str]
    repos_url: Required[str]
    url: Required[str]


class RepositoryVulnerabilityAlertDismissPayloadAlertDict(TypedDict, total=False):
    """The security alert of the vulnerable dependency."""

    affected_package_name: Required[str]
    affected_range: Required[str]
    created_at: Required[str]
    dismiss_comment: NotRequired[None | str]
    dismiss_reason: Required[str]
    dismissed_at: Required[str]
    dismisser: Required[Any | None]
    external_identifier: Required[str]
    external_reference: Required[None | str]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[str]
    fixed_in: NotRequired[str]
    ghsa_id: Required[str]
    id: Required[int]
    node_id: Required[str]
    number: Required[int]
    severity: Required[str]
    state: Required[Literal["dismissed"]]


class RepositoryVulnerabilityAlertResolvePayloadAlertDict(TypedDict, total=False):
    """The security alert of the vulnerable dependency."""

    affected_package_name: Required[str]
    affected_range: Required[str]
    created_at: Required[str]
    dismiss_reason: NotRequired[str]
    dismissed_at: NotRequired[str]
    dismisser: NotRequired[Any | None]
    external_identifier: Required[str]
    external_reference: Required[None | str]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[str]
    fixed_in: NotRequired[str]
    ghsa_id: Required[str]
    id: Required[int]
    node_id: Required[str]
    number: Required[int]
    severity: Required[str]
    state: Required[Literal["fixed", "open"]]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvssDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvss."""

    score: Required[float]
    vector_string: Required[None | str]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCweDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCwe."""

    cwe_id: Required[str]
    name: Required[str]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifierDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifier."""

    type: Required[str]
    value: Required[str]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReferenceDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReference."""

    url: Required[str]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackageDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackage."""

    ecosystem: Required[str]
    name: Required[str]


class SecurityAndAnalysisPayloadChangesFromDict(TypedDict, total=False):
    """SecurityAndAnalysisPayloadChangesFrom."""

    security_and_analysis: NotRequired[Any | None]


SponsorshipEditedPayloadChangesPrivacyLevelDict = TypedDict(
    "SponsorshipEditedPayloadChangesPrivacyLevelDict",
    {
        "from": Required[str],
    },
    total=False,
)
SponsorshipEditedPayloadChangesPrivacyLevelDict.__doc__ = """SponsorshipEditedPayloadChangesPrivacyLevel."""


class StatusPayloadBrancheCommitDict(TypedDict, total=False):
    """StatusPayloadBrancheCommit."""

    sha: Required[None | str]
    url: Required[None | str]


class StatusPayloadCommitParentDict(TypedDict, total=False):
    """StatusPayloadCommitParent."""

    html_url: Required[str]
    sha: Required[str]
    url: Required[str]


class StatusPayloadCommitCommitTreeDict(TypedDict, total=False):
    """StatusPayloadCommitCommitTree."""

    sha: Required[str]
    url: Required[str]


class StatusPayloadCommitCommitVerificationDict(TypedDict, total=False):
    """StatusPayloadCommitCommitVerification."""

    payload: Required[None | str]
    reason: Required[
        Literal[
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
    ]
    signature: Required[None | str]
    verified: Required[bool]
    verified_at: Required[None | str]


class TeamAddedToRepositoryPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """TeamAddedToRepositoryPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class TeamCreatedPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """TeamCreatedPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class TeamDeletedPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """TeamDeletedPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


TeamEditedPayloadChangesDescriptionDict = TypedDict(
    "TeamEditedPayloadChangesDescriptionDict",
    {
        "from": Required[str],
    },
    total=False,
)
TeamEditedPayloadChangesDescriptionDict.__doc__ = """TeamEditedPayloadChangesDescription."""

TeamEditedPayloadChangesNameDict = TypedDict(
    "TeamEditedPayloadChangesNameDict",
    {
        "from": Required[str],
    },
    total=False,
)
TeamEditedPayloadChangesNameDict.__doc__ = """TeamEditedPayloadChangesName."""

TeamEditedPayloadChangesNotificationSettingDict = TypedDict(
    "TeamEditedPayloadChangesNotificationSettingDict",
    {
        "from": Required[str],
    },
    total=False,
)
TeamEditedPayloadChangesNotificationSettingDict.__doc__ = """TeamEditedPayloadChangesNotificationSetting."""

TeamEditedPayloadChangesPrivacyDict = TypedDict(
    "TeamEditedPayloadChangesPrivacyDict",
    {
        "from": Required[str],
    },
    total=False,
)
TeamEditedPayloadChangesPrivacyDict.__doc__ = """TeamEditedPayloadChangesPrivacy."""


class TeamEditedPayloadChangesRepositoryPermissionsFromDict(TypedDict, total=False):
    """TeamEditedPayloadChangesRepositoryPermissionsFrom."""

    admin: NotRequired[bool]
    pull: NotRequired[bool]
    push: NotRequired[bool]


class TeamEditedPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """TeamEditedPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class TeamRemovedFromRepositoryPayloadRepositoryPermissionsDict(TypedDict, total=False):
    """TeamRemovedFromRepositoryPayloadRepositoryPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class WebhookRubygemsMetadataVersionInfoDict(TypedDict, total=False):
    """WebhookRubygemsMetadataVersionInfo."""

    version: NotRequired[str]


WebhooksAnswerReactionsDict = TypedDict(
    "WebhooksAnswerReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksAnswerReactionsDict.__doc__ = """Reactions."""


class WebhooksChanges8TierFromDict(TypedDict, total=False):
    """The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload."""

    created_at: Required[str]
    description: Required[str]
    is_custom_ammount: NotRequired[bool]
    is_custom_amount: NotRequired[bool]
    is_one_time: Required[bool]
    monthly_price_in_cents: Required[int]
    monthly_price_in_dollars: Required[int]
    name: Required[str]
    node_id: Required[str]


WebhooksChangesBodyDict = TypedDict(
    "WebhooksChangesBodyDict",
    {
        "from": Required[str],
    },
    total=False,
)
WebhooksChangesBodyDict.__doc__ = """WebhooksChangesBody."""

WebhooksCommentReactionsDict = TypedDict(
    "WebhooksCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksCommentReactionsDict.__doc__ = """Reactions."""


class WebhooksIssue2LabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class WebhooksIssue2PullRequestDict(TypedDict, total=False):
    """WebhooksIssue2PullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


WebhooksIssue2ReactionsDict = TypedDict(
    "WebhooksIssue2ReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksIssue2ReactionsDict.__doc__ = """Reactions."""


class WebhooksIssueLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class WebhooksIssuePullRequestDict(TypedDict, total=False):
    """WebhooksIssuePullRequest."""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[None | str]
    patch_url: NotRequired[str]
    url: NotRequired[str]


WebhooksIssueReactionsDict = TypedDict(
    "WebhooksIssueReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksIssueReactionsDict.__doc__ = """Reactions."""

WebhooksIssueCommentReactionsDict = TypedDict(
    "WebhooksIssueCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksIssueCommentReactionsDict.__doc__ = """Reactions."""


class WebhooksMarketplacePurchaseAccountDict(TypedDict, total=False):
    """WebhooksMarketplacePurchaseAccount."""

    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organization_billing_email: Required[None | str]
    type: Required[str]


class WebhooksMarketplacePurchasePlanDict(TypedDict, total=False):
    """WebhooksMarketplacePurchasePlan."""

    bullets: Required[list[None | str]]
    description: Required[str]
    has_free_trial: Required[bool]
    id: Required[int]
    monthly_price_in_cents: Required[int]
    name: Required[str]
    price_model: Required[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: Required[None | str]
    yearly_price_in_cents: Required[int]


class WebhooksPreviousMarketplacePurchaseAccountDict(TypedDict, total=False):
    """WebhooksPreviousMarketplacePurchaseAccount."""

    id: Required[int]
    login: Required[str]
    node_id: Required[str]
    organization_billing_email: Required[None | str]
    type: Required[str]


class WebhooksPreviousMarketplacePurchasePlanDict(TypedDict, total=False):
    """WebhooksPreviousMarketplacePurchasePlan."""

    bullets: Required[list[str]]
    description: Required[str]
    has_free_trial: Required[bool]
    id: Required[int]
    monthly_price_in_cents: Required[int]
    name: Required[str]
    price_model: Required[Literal["FREE", "FLAT_RATE", "PER_UNIT"]]
    unit_name: Required[None | str]
    yearly_price_in_cents: Required[int]


WebhooksProjectChangesArchivedAtDict = TypedDict(
    "WebhooksProjectChangesArchivedAtDict",
    {
        "from": NotRequired[None | str],
        "to": NotRequired[None | str],
    },
    total=False,
)
WebhooksProjectChangesArchivedAtDict.__doc__ = """WebhooksProjectChangesArchivedAt."""


class WebhooksPullRequest5LabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class WebhooksPullRequest5RequestedReviewerOption2Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhooksPullRequest5RequestedTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhooksPullRequest5BaseRepoPermissionsDict(TypedDict, total=False):
    """WebhooksPullRequest5BaseRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class WebhooksPullRequest5HeadRepoPermissionsDict(TypedDict, total=False):
    """WebhooksPullRequest5HeadRepoPermissions."""

    admin: Required[bool]
    maintain: NotRequired[bool]
    pull: Required[bool]
    push: Required[bool]
    triage: NotRequired[bool]


class WebhooksPullRequest5LinksCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksCommitsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksIssueDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksReviewCommentDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksReviewCommentsDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksPullRequest5LinksStatusesDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


WebhooksRelease1ReactionsDict = TypedDict(
    "WebhooksRelease1ReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksRelease1ReactionsDict.__doc__ = """Reactions."""


class WebhooksReleaseAssetDict(TypedDict, total=False):
    """Data related to a release."""

    browser_download_url: Required[str]
    content_type: Required[str]
    created_at: Required[str]
    download_count: Required[int]
    id: Required[int]
    label: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    size: Required[int]
    digest: Required[None | str]
    state: Required[Literal["uploaded"]]
    updated_at: Required[str]
    uploader: NotRequired[Any | None]
    url: Required[str]


WebhooksReleaseReactionsDict = TypedDict(
    "WebhooksReleaseReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksReleaseReactionsDict.__doc__ = """Reactions."""

WebhooksReviewCommentReactionsDict = TypedDict(
    "WebhooksReviewCommentReactionsDict",
    {
        "+1": Required[int],
        "-1": Required[int],
        "confused": Required[int],
        "eyes": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "laugh": Required[int],
        "rocket": Required[int],
        "total_count": Required[int],
        "url": Required[str],
    },
    total=False,
)
WebhooksReviewCommentReactionsDict.__doc__ = """Reactions."""


class WebhooksReviewCommentLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksReviewCommentLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksReviewCommentLinksSelfDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksReviewLinksHtmlDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksReviewLinksPullRequestDict(TypedDict, total=False):
    """Link."""

    href: Required[str]


class WebhooksSecurityAdvisoryCvssDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryCvss."""

    score: Required[float]
    vector_string: Required[None | str]


class WebhooksSecurityAdvisoryCweDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryCwe."""

    cwe_id: Required[str]
    name: Required[str]


class WebhooksSecurityAdvisoryIdentifierDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryIdentifier."""

    type: Required[str]
    value: Required[str]


class WebhooksSecurityAdvisoryReferenceDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryReference."""

    url: Required[str]


class WebhooksSecurityAdvisoryVulnerabilityPackageDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryVulnerabilityPackage."""

    ecosystem: Required[str]
    name: Required[str]


class WebhooksSponsorshipMaintainerDict(TypedDict, total=False):
    """WebhooksSponsorshipMaintainer."""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhooksSponsorshipTierDict(TypedDict, total=False):
    """The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload."""

    created_at: Required[str]
    description: Required[str]
    is_custom_ammount: NotRequired[bool]
    is_custom_amount: NotRequired[bool]
    is_one_time: Required[bool]
    monthly_price_in_cents: Required[int]
    monthly_price_in_dollars: Required[int]
    name: Required[str]
    node_id: Required[str]


class WorkflowJobQueuedPayloadWorkflowJobStepDict(TypedDict, total=False):
    """Workflow Step."""

    completed_at: Required[None | str]
    conclusion: Required[Literal["failure", "skipped", "success", "cancelled"] | None]
    name: Required[str]
    number: Required[int]
    started_at: Required[None | str]
    status: Required[Literal["completed", "in_progress", "queued", "pending"]]


class WorkflowJobWaitingPayloadWorkflowJobStepDict(TypedDict, total=False):
    """Workflow Step."""

    completed_at: Required[None | str]
    conclusion: Required[Literal["failure", "skipped", "success", "cancelled"] | None]
    name: Required[str]
    number: Required[int]
    started_at: Required[None | str]
    status: Required[Literal["completed", "in_progress", "queued", "pending", "waiting"]]


class WorkflowRunCompletedPayloadWorkflowRunHeadRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunCompletedPayloadWorkflowRunRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunInProgressPayloadWorkflowRunHeadRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[None | str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunInProgressPayloadWorkflowRunRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunRequestedPayloadWorkflowRunHeadRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunRepositoryDict(TypedDict, total=False):
    """Repository Lite."""

    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    description: Required[None | str]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    owner: Required[Any | None]
    private: Required[bool]
    pulls_url: Required[str]
    releases_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    url: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthorDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitterDict(TypedDict, total=False):
    """Metaproperties for Git author/committer information."""

    date: NotRequired[str]
    email: Required[None | str]
    name: Required[str]
    username: NotRequired[str]


class WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepoDict(TypedDict, total=False):
    """Repo Ref."""

    id: Required[int]
    name: Required[str]
    url: Required[str]


class AppPermissionsDict(TypedDict, total=False):
    """The permissions granted to the user access token."""

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    artifact_metadata: NotRequired[Literal["read", "write"]]
    attestations: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    codespaces: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    dependabot_secrets: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    merge_queues: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_custom_properties: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["write"]]
    custom_properties_for_organizations: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_custom_roles: NotRequired[Literal["read", "write"]]
    organization_custom_org_roles: NotRequired[Literal["read", "write"]]
    organization_custom_properties: NotRequired[Literal["read", "write", "admin"]]
    organization_copilot_seat_management: NotRequired[Literal["write"]]
    organization_announcement_banners: NotRequired[Literal["read", "write"]]
    organization_events: NotRequired[Literal["read"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_personal_access_tokens: NotRequired[Literal["read", "write"]]
    organization_personal_access_token_requests: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    email_addresses: NotRequired[Literal["read", "write"]]
    followers: NotRequired[Literal["read", "write"]]
    git_ssh_keys: NotRequired[Literal["read", "write"]]
    gpg_keys: NotRequired[Literal["read", "write"]]
    interaction_limits: NotRequired[Literal["read", "write"]]
    profile: NotRequired[Literal["write"]]
    starring: NotRequired[Literal["read", "write"]]
    enterprise_custom_properties_for_organizations: NotRequired[Literal["read", "write", "admin"]]


class CodeOfConductDict(TypedDict, total=False):
    """Code Of Conduct."""

    key: Required[str]
    name: Required[str]
    url: Required[str]
    body: NotRequired[str]
    html_url: Required[None | str]


class CodeOfConductSimpleDict(TypedDict, total=False):
    """Code of Conduct Simple."""

    url: Required[str]
    key: Required[str]
    name: Required[str]
    html_url: Required[None | str]


class CustomPropertyDict(TypedDict, total=False):
    """Custom property defined on an organization."""

    property_name: Required[str]
    url: NotRequired[str]
    source_type: NotRequired[Literal["organization", "enterprise"]]
    value_type: Required[Literal["string", "single_select", "multi_select", "true_false"]]
    required: NotRequired[bool]
    default_value: NotRequired[list[str] | str]
    description: NotRequired[None | str]
    allowed_values: NotRequired[Any | None]
    values_editable_by: NotRequired[Literal["org_actors", "org_and_repo_actors"] | None]


class CustomPropertyValueDict(TypedDict, total=False):
    """Custom property name and associated value."""

    property_name: Required[str]
    value: Required[list[str] | str]


class DependabotAlertPackageDict(TypedDict, total=False):
    """Details for the vulnerable package."""

    ecosystem: Required[str]
    name: Required[str]


class DeploymentSimpleDict(TypedDict, total=False):
    """A deployment created as the result of an Actions check run from a workflow that references an environment."""

    url: Required[str]
    id: Required[int]
    node_id: Required[str]
    task: Required[str]
    original_environment: NotRequired[str]
    environment: Required[str]
    description: Required[None | str]
    created_at: Required[str]
    updated_at: Required[str]
    statuses_url: Required[str]
    repository_url: Required[str]
    transient_environment: NotRequired[bool]
    production_environment: NotRequired[bool]
    performed_via_github_app: NotRequired[Any | None]


class EnterpriseDict2(TypedDict, total=False):
    """An enterprise on GitHub."""

    description: NotRequired[None | str]
    html_url: Required[str]
    website_url: NotRequired[None | str]
    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    slug: Required[str]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    avatar_url: Required[str]


class EnterpriseDict(TypedDict, total=False):
    """An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured on an enterprise account or an organization that's part of an enterprise account. For more information, see "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."""

    description: NotRequired[None | str]
    html_url: Required[str]
    website_url: NotRequired[None | str]
    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    slug: Required[str]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    avatar_url: Required[str]


class HookResponseDict(TypedDict, total=False):
    """Hook Response."""

    code: Required[None | int]
    status: Required[None | str]
    message: Required[None | str]


class IssueDependenciesSummaryDict(TypedDict, total=False):
    """Issue Dependencies Summary."""

    blocked_by: Required[int]
    blocking: Required[int]
    total_blocked_by: Required[int]
    total_blocking: Required[int]


class IssueFieldValueDict(TypedDict, total=False):
    """A value assigned to an issue field."""

    issue_field_id: Required[int]
    node_id: Required[str]
    data_type: Required[Literal["text", "single_select", "number", "date"]]
    value: Required[float | int | str]
    single_select_option: NotRequired[Any | None]


class LabelDict(TypedDict, total=False):
    """Color-coded labels help you categorize and filter your issues (just like labels in Gmail)."""

    id: Required[int]
    node_id: Required[str]
    url: Required[str]
    name: Required[str]
    description: Required[None | str]
    color: Required[str]
    default: Required[bool]


class LicenseSimpleDict(TypedDict, total=False):
    """License Simple."""

    key: Required[str]
    name: Required[str]
    url: Required[None | str]
    spdx_id: Required[None | str]
    node_id: Required[str]
    html_url: NotRequired[str]


class LinkDict(TypedDict, total=False):
    """Hypermedia Link."""

    href: Required[str]


class OrganizationDict(TypedDict, total=False):
    """A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an organization, or when the event occurs from activity in a repository owned by an organization."""

    login: Required[str]
    id: Required[int]
    node_id: Required[str]
    url: Required[str]
    repos_url: Required[str]
    events_url: Required[str]
    hooks_url: Required[str]
    issues_url: Required[str]
    members_url: Required[str]
    public_members_url: Required[str]
    avatar_url: Required[str]
    description: Required[None | str]


class ProjectsV2IterationSettingDict(TypedDict, total=False):
    """An iteration setting for an iteration field."""

    id: Required[str]
    title: Required[str]
    title_html: NotRequired[str]
    duration: NotRequired[None | float]
    start_date: NotRequired[None | str]
    completed: NotRequired[bool]


class ProjectsV2SingleSelectOptionDict(TypedDict, total=False):
    """An option for a single select field."""

    id: Required[str]
    name: Required[str]
    color: NotRequired[None | str]
    description: NotRequired[None | str]


ReactionRollupDict = TypedDict(
    "ReactionRollupDict",
    {
        "url": Required[str],
        "total_count": Required[int],
        "+1": Required[int],
        "-1": Required[int],
        "laugh": Required[int],
        "confused": Required[int],
        "heart": Required[int],
        "hooray": Required[int],
        "eyes": Required[int],
        "rocket": Required[int],
    },
    total=False,
)
ReactionRollupDict.__doc__ = """Reaction Rollup."""


class RepositoryRuleCreationDict(TypedDict, total=False):
    """Only allow users with bypass permission to create matching refs."""

    type: Required[Literal["creation"]]


class RepositoryRuleDeletionDict(TypedDict, total=False):
    """Only allow users with bypass permissions to delete matching refs."""

    type: Required[Literal["deletion"]]


class RepositoryRuleNonFastForwardDict(TypedDict, total=False):
    """Prevent users with push access from force pushing to refs."""

    type: Required[Literal["non_fast_forward"]]


class RepositoryRuleParamsCodeScanningToolDict(TypedDict, total=False):
    """A tool that must provide code scanning results for this rule to pass."""

    alerts_threshold: Required[Literal["none", "errors", "errors_and_warnings", "all"]]
    security_alerts_threshold: Required[Literal["none", "critical", "high_or_higher", "medium_or_higher", "all"]]
    tool: Required[str]


class RepositoryRuleParamsReviewerDict(TypedDict, total=False):
    """A required reviewing team."""

    id: Required[int]
    type: Required[Literal["Team"]]


class RepositoryRuleParamsStatusCheckConfigurationDict(TypedDict, total=False):
    """Required status check."""

    context: Required[str]
    integration_id: NotRequired[int]


class RepositoryRuleParamsWorkflowFileReferenceDict(TypedDict, total=False):
    """A workflow that must run for this rule to pass."""

    path: Required[str]
    ref: NotRequired[str]
    repository_id: Required[int]
    sha: NotRequired[str]


class RepositoryRuleRequiredLinearHistoryDict(TypedDict, total=False):
    """Prevent merge commits from being pushed to matching refs."""

    type: Required[Literal["required_linear_history"]]


class RepositoryRuleRequiredSignaturesDict(TypedDict, total=False):
    """Commits pushed to matching refs must have verified signatures."""

    type: Required[Literal["required_signatures"]]


class RepositoryRulesetBypassActorDict(TypedDict, total=False):
    """An actor that can bypass rules in a ruleset."""

    actor_id: NotRequired[None | int]
    actor_type: Required[Literal["Integration", "OrganizationAdmin", "RepositoryRole", "Team", "DeployKey"]]
    bypass_mode: NotRequired[Literal["always", "pull_request", "exempt"]]


class SecretScanningLocationCommitDict(TypedDict, total=False):
    """Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository."""

    path: Required[str]
    start_line: Required[float]
    end_line: Required[float]
    start_column: Required[float]
    end_column: Required[float]
    blob_sha: Required[str]
    blob_url: Required[str]
    commit_sha: Required[str]
    commit_url: Required[str]


class SecretScanningLocationDiscussionBodyDict(TypedDict, total=False):
    """Represents a 'discussion_body' secret scanning location type. This location type shows that a secret was detected in the body of a discussion."""

    discussion_body_url: Required[str]


class SecretScanningLocationDiscussionCommentDict(TypedDict, total=False):
    """Represents a 'discussion_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a discussion."""

    discussion_comment_url: Required[str]


class SecretScanningLocationDiscussionTitleDict(TypedDict, total=False):
    """Represents a 'discussion_title' secret scanning location type. This location type shows that a secret was detected in the title of a discussion."""

    discussion_title_url: Required[str]


class SecretScanningLocationIssueBodyDict(TypedDict, total=False):
    """Represents an 'issue_body' secret scanning location type. This location type shows that a secret was detected in the body of an issue."""

    issue_body_url: Required[str]


class SecretScanningLocationIssueCommentDict(TypedDict, total=False):
    """Represents an 'issue_comment' secret scanning location type. This location type shows that a secret was detected in a comment on an issue."""

    issue_comment_url: Required[str]


class SecretScanningLocationIssueTitleDict(TypedDict, total=False):
    """Represents an 'issue_title' secret scanning location type. This location type shows that a secret was detected in the title of an issue."""

    issue_title_url: Required[str]


class SecretScanningLocationPullRequestBodyDict(TypedDict, total=False):
    """Represents a 'pull_request_body' secret scanning location type. This location type shows that a secret was detected in the body of a pull request."""

    pull_request_body_url: Required[str]


class SecretScanningLocationPullRequestCommentDict(TypedDict, total=False):
    """Represents a 'pull_request_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a pull request."""

    pull_request_comment_url: Required[str]


class SecretScanningLocationPullRequestReviewDict(TypedDict, total=False):
    """Represents a 'pull_request_review' secret scanning location type. This location type shows that a secret was detected in a review on a pull request."""

    pull_request_review_url: Required[str]


class SecretScanningLocationPullRequestReviewCommentDict(TypedDict, total=False):
    """Represents a 'pull_request_review_comment' secret scanning location type. This location type shows that a secret was detected in a review comment on a pull request."""

    pull_request_review_comment_url: Required[str]


class SecretScanningLocationPullRequestTitleDict(TypedDict, total=False):
    """Represents a 'pull_request_title' secret scanning location type. This location type shows that a secret was detected in the title of a pull request."""

    pull_request_title_url: Required[str]


class SecretScanningLocationWikiCommitDict(TypedDict, total=False):
    """Represents a 'wiki_commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository wiki."""

    path: Required[str]
    start_line: Required[float]
    end_line: Required[float]
    start_column: Required[float]
    end_column: Required[float]
    blob_sha: Required[str]
    page_url: Required[str]
    commit_sha: Required[str]
    commit_url: Required[str]


class SimpleCommitDict(TypedDict, total=False):
    """A commit."""

    id: Required[str]
    tree_id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    author: Required[Any | None]
    committer: Required[Any | None]


class InstallationDict(TypedDict, total=False):
    """The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured for and sent to a GitHub App. For more information, see "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."""

    id: Required[int]
    node_id: Required[str]


class UserDict(TypedDict, total=False):
    """A GitHub user."""

    name: NotRequired[None | str]
    email: NotRequired[None | str]
    login: Required[str]
    id: Required[int]
    node_id: Required[str]
    avatar_url: Required[str]
    gravatar_id: Required[None | str]
    url: Required[str]
    html_url: Required[str]
    followers_url: Required[str]
    following_url: Required[str]
    gists_url: Required[str]
    starred_url: Required[str]
    subscriptions_url: Required[str]
    organizations_url: Required[str]
    repos_url: Required[str]
    events_url: Required[str]
    received_events_url: Required[str]
    type: Required[str]
    site_admin: Required[bool]
    starred_at: NotRequired[str]
    user_view_type: NotRequired[str]


class SubIssuesSummaryDict(TypedDict, total=False):
    """Sub-issues Summary."""

    total: Required[int]
    completed: Required[int]
    percent_completed: Required[int]


class PullRequestPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook."""


class PullRequestPayloadDict2(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook."""


class WebhooksAlertDict(TypedDict, total=False):
    """The security alert of the vulnerable dependency."""

    affected_package_name: Required[str]
    affected_range: Required[str]
    created_at: Required[str]
    dismiss_reason: NotRequired[str]
    dismissed_at: NotRequired[str]
    dismisser: NotRequired[Any | None]
    external_identifier: Required[str]
    external_reference: Required[None | str]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[str]
    fixed_in: NotRequired[str]
    ghsa_id: Required[str]
    id: Required[int]
    node_id: Required[str]
    number: Required[int]
    severity: Required[str]
    state: Required[Literal["open"]]


class WebhooksApproverDict(TypedDict, total=False):
    """WebhooksApprover."""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhooksDeployKeyDict(TypedDict, total=False):
    """The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) resource."""

    added_by: NotRequired[None | str]
    created_at: Required[str]
    id: Required[int]
    key: Required[str]
    last_used: NotRequired[None | str]
    read_only: Required[bool]
    title: Required[str]
    url: Required[str]
    verified: Required[bool]
    enabled: NotRequired[bool]


class WebhooksLabelDict(TypedDict, total=False):
    """Label."""

    color: Required[str]
    default: Required[bool]
    description: Required[None | str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    url: Required[str]


class WebhooksMembershipDict(TypedDict, total=False):
    """The membership between the user and the organization. Not present when the action is `member_invited`."""

    organization_url: Required[str]
    role: Required[str]
    direct_membership: NotRequired[bool]
    enterprise_teams_providing_indirect_membership: NotRequired[list[str]]
    state: Required[str]
    url: Required[str]
    user: Required[Any | None]


class WebhooksMilestoneDict(TypedDict, total=False):
    """A collection of related issues and pull requests."""

    closed_at: Required[None | str]
    closed_issues: Required[int]
    created_at: Required[str]
    creator: Required[Any | None]
    description: Required[None | str]
    due_on: Required[None | str]
    html_url: Required[str]
    id: Required[int]
    labels_url: Required[str]
    node_id: Required[str]
    number: Required[int]
    open_issues: Required[int]
    state: Required[Literal["open", "closed"]]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]


class WebhooksProjectDict(TypedDict, total=False):
    """Project."""

    body: Required[None | str]
    columns_url: Required[str]
    created_at: Required[str]
    creator: Required[Any | None]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    number: Required[int]
    owner_url: Required[str]
    state: Required[Literal["open", "closed"]]
    updated_at: Required[str]
    url: Required[str]


class WebhooksProjectCardDict(TypedDict, total=False):
    """Project Card."""

    after_id: NotRequired[None | int]
    archived: Required[bool]
    column_id: Required[int]
    column_url: Required[str]
    content_url: NotRequired[str]
    created_at: Required[str]
    creator: Required[Any | None]
    id: Required[int]
    node_id: Required[str]
    note: Required[None | str]
    project_url: Required[str]
    updated_at: Required[str]
    url: Required[str]


class WebhooksProjectColumnDict(TypedDict, total=False):
    """Project Column."""

    after_id: NotRequired[None | int]
    cards_url: Required[str]
    created_at: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    project_url: Required[str]
    updated_at: Required[str]
    url: Required[str]


class WebhooksRuleDict(TypedDict, total=False):
    """The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings."""

    admin_enforced: Required[bool]
    allow_deletions_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    allow_force_pushes_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    authorized_actor_names: Required[list[str]]
    authorized_actors_only: Required[bool]
    authorized_dismissal_actors_only: Required[bool]
    create_protected: NotRequired[bool]
    created_at: Required[str]
    dismiss_stale_reviews_on_push: Required[bool]
    id: Required[int]
    ignore_approvals_from_contributors: Required[bool]
    linear_history_requirement_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    lock_branch_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    lock_allows_fork_sync: NotRequired[bool]
    merge_queue_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    name: Required[str]
    pull_request_reviews_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    repository_id: Required[int]
    require_code_owner_review: Required[bool]
    require_last_push_approval: NotRequired[bool]
    required_approving_review_count: Required[int]
    required_conversation_resolution_level: Required[Literal["off", "non_admins", "everyone"]]
    required_deployments_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    required_status_checks: Required[list[str]]
    required_status_checks_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    signature_requirement_enforcement_level: Required[Literal["off", "non_admins", "everyone"]]
    strict_required_status_checks_policy: Required[bool]
    updated_at: Required[str]


class WebhooksTeamDict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    notification_setting: NotRequired[Literal["notifications_enabled", "notifications_disabled"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]
    type: NotRequired[Literal["enterprise", "organization"]]
    organization_id: NotRequired[int]
    enterprise_id: NotRequired[int]


class WebhooksTeam1Dict(TypedDict, total=False):
    """Groups of organization members that gives permissions on specified repositories."""

    deleted: NotRequired[bool]
    description: NotRequired[None | str]
    html_url: NotRequired[str]
    id: Required[int]
    members_url: NotRequired[str]
    name: Required[str]
    node_id: NotRequired[str]
    parent: NotRequired[Any | None]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    notification_setting: NotRequired[Literal["notifications_enabled", "notifications_disabled"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]
    type: NotRequired[Literal["enterprise", "organization"]]
    organization_id: NotRequired[int]
    enterprise_id: NotRequired[int]


class WebhooksWorkflowJobRunDict(TypedDict, total=False):
    """WebhooksWorkflowJobRun."""

    conclusion: Required[None]
    created_at: Required[str]
    environment: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[None]
    status: Required[str]
    updated_at: Required[str]


class BranchProtectionRuleEditedPayloadChangesDict(TypedDict, total=False):
    """If the action was `edited`, the changes to the rule."""

    admin_enforced: NotRequired[BranchProtectionRuleEditedPayloadChangesAdminEnforcedDict]
    authorized_actor_names: NotRequired[BranchProtectionRuleEditedPayloadChangesAuthorizedActorNamesDict]
    authorized_actors_only: NotRequired[BranchProtectionRuleEditedPayloadChangesAuthorizedActorsOnlyDict]
    authorized_dismissal_actors_only: NotRequired[
        BranchProtectionRuleEditedPayloadChangesAuthorizedDismissalActorsOnlyDict
    ]
    linear_history_requirement_enforcement_level: NotRequired[
        BranchProtectionRuleEditedPayloadChangesLinearHistoryRequirementEnforcementLevelDict
    ]
    lock_branch_enforcement_level: NotRequired[BranchProtectionRuleEditedPayloadChangesLockBranchEnforcementLevelDict]
    lock_allows_fork_sync: NotRequired[BranchProtectionRuleEditedPayloadChangesLockAllowsForkSyncDict]
    pull_request_reviews_enforcement_level: NotRequired[
        BranchProtectionRuleEditedPayloadChangesPullRequestReviewsEnforcementLevelDict
    ]
    require_last_push_approval: NotRequired[BranchProtectionRuleEditedPayloadChangesRequireLastPushApprovalDict]
    required_status_checks: NotRequired[BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksDict]
    required_status_checks_enforcement_level: NotRequired[
        BranchProtectionRuleEditedPayloadChangesRequiredStatusChecksEnforcementLevelDict
    ]


class CheckSuiteCompletedPayloadCheckSuiteAppDict(TypedDict, total=False):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    created_at: Required[None | str]
    description: Required[None | str]
    events: NotRequired[list[str]]
    external_url: Required[None | str]
    html_url: Required[str]
    id: Required[None | int]
    client_id: NotRequired[None | str]
    name: Required[str]
    node_id: Required[str]
    owner: Required[Any | None]
    permissions: NotRequired[CheckSuiteCompletedPayloadCheckSuiteAppPermissionsDict]
    slug: NotRequired[str]
    updated_at: Required[None | str]


class CheckSuiteCompletedPayloadCheckSuiteHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[CheckSuiteCompletedPayloadCheckSuiteHeadCommitAuthorDict]
    committer: Required[CheckSuiteCompletedPayloadCheckSuiteHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class CheckSuiteCompletedPayloadCheckSuitePullRequestBaseDict(TypedDict, total=False):
    """CheckSuiteCompletedPayloadCheckSuitePullRequestBase."""

    ref: Required[str]
    repo: Required[CheckSuiteCompletedPayloadCheckSuitePullRequestBaseRepoDict]
    sha: Required[str]


class CheckSuiteCompletedPayloadCheckSuitePullRequestHeadDict(TypedDict, total=False):
    """CheckSuiteCompletedPayloadCheckSuitePullRequestHead."""

    ref: Required[str]
    repo: Required[CheckSuiteCompletedPayloadCheckSuitePullRequestHeadRepoDict]
    sha: Required[str]


class CheckSuiteRequestedPayloadCheckSuiteAppDict(TypedDict, total=False):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    created_at: Required[None | str]
    description: Required[None | str]
    events: NotRequired[list[str]]
    external_url: Required[None | str]
    html_url: Required[str]
    id: Required[None | int]
    client_id: NotRequired[None | str]
    name: Required[str]
    node_id: Required[str]
    owner: Required[Any | None]
    permissions: NotRequired[CheckSuiteRequestedPayloadCheckSuiteAppPermissionsDict]
    slug: NotRequired[str]
    updated_at: Required[None | str]


class CheckSuiteRequestedPayloadCheckSuiteHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[CheckSuiteRequestedPayloadCheckSuiteHeadCommitAuthorDict]
    committer: Required[CheckSuiteRequestedPayloadCheckSuiteHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class CheckSuiteRequestedPayloadCheckSuitePullRequestBaseDict(TypedDict, total=False):
    """CheckSuiteRequestedPayloadCheckSuitePullRequestBase."""

    ref: Required[str]
    repo: Required[CheckSuiteRequestedPayloadCheckSuitePullRequestBaseRepoDict]
    sha: Required[str]


class CheckSuiteRequestedPayloadCheckSuitePullRequestHeadDict(TypedDict, total=False):
    """CheckSuiteRequestedPayloadCheckSuitePullRequestHead."""

    ref: Required[str]
    repo: Required[CheckSuiteRequestedPayloadCheckSuitePullRequestHeadRepoDict]
    sha: Required[str]


class CheckSuiteRerequestedPayloadCheckSuiteAppDict(TypedDict, total=False):
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub."""

    created_at: Required[None | str]
    description: Required[None | str]
    events: NotRequired[list[str]]
    external_url: Required[None | str]
    html_url: Required[str]
    id: Required[None | int]
    client_id: NotRequired[None | str]
    name: Required[str]
    node_id: Required[str]
    owner: Required[Any | None]
    permissions: NotRequired[CheckSuiteRerequestedPayloadCheckSuiteAppPermissionsDict]
    slug: NotRequired[str]
    updated_at: Required[None | str]


class CheckSuiteRerequestedPayloadCheckSuiteHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[CheckSuiteRerequestedPayloadCheckSuiteHeadCommitAuthorDict]
    committer: Required[CheckSuiteRerequestedPayloadCheckSuiteHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseDict(TypedDict, total=False):
    """CheckSuiteRerequestedPayloadCheckSuitePullRequestBase."""

    ref: Required[str]
    repo: Required[CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseRepoDict]
    sha: Required[str]


class CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadDict(TypedDict, total=False):
    """CheckSuiteRerequestedPayloadCheckSuitePullRequestHead."""

    ref: Required[str]
    repo: Required[CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadRepoDict]
    sha: Required[str]


class CommitCommentCreatedPayloadCommentDict(TypedDict, total=False):
    """The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource."""

    author_association: Required[
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
    ]
    body: Required[str]
    commit_id: Required[str]
    created_at: Required[str]
    html_url: Required[str]
    id: Required[int]
    line: Required[None | int]
    node_id: Required[str]
    path: Required[None | str]
    position: Required[None | int]
    reactions: NotRequired[CommitCommentCreatedPayloadCommentReactionsDict]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


DiscussionCategoryChangedPayloadChangesCategoryDict = TypedDict(
    "DiscussionCategoryChangedPayloadChangesCategoryDict",
    {
        "from": Required[DiscussionCategoryChangedPayloadChangesCategoryFromDict],
    },
    total=False,
)
DiscussionCategoryChangedPayloadChangesCategoryDict.__doc__ = """DiscussionCategoryChangedPayloadChangesCategory."""


class DiscussionCommentEditedPayloadChangesDict(TypedDict, total=False):
    """DiscussionCommentEditedPayloadChanges."""

    body: Required[DiscussionCommentEditedPayloadChangesBodyDict]


class DiscussionEditedPayloadChangesDict(TypedDict, total=False):
    """DiscussionEditedPayloadChanges."""

    body: NotRequired[DiscussionEditedPayloadChangesBodyDict]
    title: NotRequired[DiscussionEditedPayloadChangesTitleDict]


class InstallationTargetRenamedPayloadChangesDict(TypedDict, total=False):
    """InstallationTargetRenamedPayloadChanges."""

    login: NotRequired[InstallationTargetRenamedPayloadChangesLoginDict]
    slug: NotRequired[InstallationTargetRenamedPayloadChangesSlugDict]


class IssueCommentCreatedPayloadCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself."""

    author_association: Required[
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
    ]
    body: Required[str]
    created_at: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    node_id: Required[str]
    performed_via_github_app: Required[Any | None]
    reactions: Required[IssueCommentCreatedPayloadCommentReactionsDict]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the issue."""

    body: NotRequired[IssuesEditedPayloadChangesBodyDict]
    title: NotRequired[IssuesEditedPayloadChangesTitleDict]


class IssuesOpenedPayloadChangesOldRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_discussions: NotRequired[bool]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[IssuesOpenedPayloadChangesOldRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class IssuesTransferredPayloadChangesNewRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[IssuesTransferredPayloadChangesNewRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class LabelEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the label if the action was `edited`."""

    color: NotRequired[LabelEditedPayloadChangesColorDict]
    description: NotRequired[LabelEditedPayloadChangesDescriptionDict]
    name: NotRequired[LabelEditedPayloadChangesNameDict]


class MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseDict(TypedDict, total=False):
    """Marketplace Purchase."""

    account: Required[MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseAccountDict]
    billing_cycle: Required[str]
    free_trial_ends_on: Required[None | str]
    next_billing_date: NotRequired[None | str]
    on_free_trial: Required[None | bool]
    plan: Required[MarketplacePurchaseChangedPayloadPreviousMarketplacePurchasePlanDict]
    unit_count: Required[int]


class MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseDict(TypedDict, total=False):
    """Marketplace Purchase."""

    account: Required[MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseAccountDict]
    billing_cycle: Required[str]
    free_trial_ends_on: Required[None]
    next_billing_date: Required[None | str]
    on_free_trial: Required[bool]
    plan: Required[MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchasePlanDict]
    unit_count: Required[int]


class MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseDict(TypedDict, total=False):
    """Marketplace Purchase."""

    account: Required[MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseAccountDict]
    billing_cycle: Required[str]
    free_trial_ends_on: Required[None | str]
    next_billing_date: NotRequired[None | str]
    on_free_trial: Required[bool]
    plan: Required[MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchasePlanDict]
    unit_count: Required[int]


class MemberAddedPayloadChangesDict(TypedDict, total=False):
    """MemberAddedPayloadChanges."""

    permission: NotRequired[MemberAddedPayloadChangesPermissionDict]
    role_name: NotRequired[MemberAddedPayloadChangesRoleNameDict]


class MemberEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the collaborator permissions."""

    old_permission: NotRequired[MemberEditedPayloadChangesOldPermissionDict]
    permission: NotRequired[MemberEditedPayloadChangesPermissionDict]


class MetaDeletedPayloadHookDict(TypedDict, total=False):
    """The deleted webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace."""

    active: Required[bool]
    config: Required[MetaDeletedPayloadHookConfigDict]
    created_at: Required[str]
    events: Required[list[str]]
    id: Required[int]
    name: Required[str]
    type: Required[str]
    updated_at: Required[str]


class MilestoneEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the milestone if the action was `edited`."""

    description: NotRequired[MilestoneEditedPayloadChangesDescriptionDict]
    due_on: NotRequired[MilestoneEditedPayloadChangesDueOnDict]
    title: NotRequired[MilestoneEditedPayloadChangesTitleDict]


class OrganizationRenamedPayloadChangesDict(TypedDict, total=False):
    """OrganizationRenamedPayloadChanges."""

    login: NotRequired[OrganizationRenamedPayloadChangesLoginDict]


class PageBuildPayloadBuildDict(TypedDict, total=False):
    """The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-github-pages-builds) itself."""

    commit: Required[None | str]
    created_at: Required[str]
    duration: Required[int]
    error: Required[PageBuildPayloadBuildErrorDict]
    pusher: Required[Any | None]
    status: Required[str]
    updated_at: Required[str]
    url: Required[str]


class ProjectCardConvertedPayloadChangesDict(TypedDict, total=False):
    """ProjectCardConvertedPayloadChanges."""

    note: Required[ProjectCardConvertedPayloadChangesNoteDict]


class ProjectCardEditedPayloadChangesDict(TypedDict, total=False):
    """ProjectCardEditedPayloadChanges."""

    note: Required[ProjectCardEditedPayloadChangesNoteDict]


class ProjectCardMovedPayloadChangesDict(TypedDict, total=False):
    """ProjectCardMovedPayloadChanges."""

    column_id: Required[ProjectCardMovedPayloadChangesColumnIdDict]


class ProjectColumnEditedPayloadChangesDict(TypedDict, total=False):
    """ProjectColumnEditedPayloadChanges."""

    name: NotRequired[ProjectColumnEditedPayloadChangesNameDict]


class ProjectEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the project if the action was `edited`."""

    body: NotRequired[ProjectEditedPayloadChangesBodyDict]
    name: NotRequired[ProjectEditedPayloadChangesNameDict]


class ProjectsV2EditedPayloadChangesDict(TypedDict, total=False):
    """ProjectsV2EditedPayloadChanges."""

    description: NotRequired[ProjectsV2EditedPayloadChangesDescriptionDict]
    public: NotRequired[ProjectsV2EditedPayloadChangesPublicDict]
    short_description: NotRequired[ProjectsV2EditedPayloadChangesShortDescriptionDict]
    title: NotRequired[ProjectsV2EditedPayloadChangesTitleDict]


class ProjectsV2ItemConvertedPayloadChangesDict(TypedDict, total=False):
    """ProjectsV2ItemConvertedPayloadChanges."""

    content_type: NotRequired[ProjectsV2ItemConvertedPayloadChangesContentTypeDict]


class ProjectsV2ItemEditedPayloadChangesOption2Dict(TypedDict, total=False):
    """ProjectsV2ItemEditedPayloadChangesOption2."""

    body: Required[ProjectsV2ItemEditedPayloadChangesOption2BodyDict]


class ProjectsV2ItemReorderedPayloadChangesDict(TypedDict, total=False):
    """ProjectsV2ItemReorderedPayloadChanges."""

    previous_projects_v2_item_node_id: NotRequired[
        ProjectsV2ItemReorderedPayloadChangesPreviousProjectsV2ItemNodeIdDict
    ]


class ProjectsV2StatusUpdateEditedPayloadChangesDict(TypedDict, total=False):
    """ProjectsV2StatusUpdateEditedPayloadChanges."""

    body: NotRequired[ProjectsV2StatusUpdateEditedPayloadChangesBodyDict]
    status: NotRequired[ProjectsV2StatusUpdateEditedPayloadChangesStatusDict]
    start_date: NotRequired[ProjectsV2StatusUpdateEditedPayloadChangesStartDateDict]
    target_date: NotRequired[ProjectsV2StatusUpdateEditedPayloadChangesTargetDateDict]


class PullRequestAssignedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestAssignedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestAssignedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestAssignedPayloadPullRequestLinks."""

    comments: Required[PullRequestAssignedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestAssignedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestAssignedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestAssignedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestAssignedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestAssignedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestAssignedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestAssignedPayloadPullRequestLinksStatusesDict]


class PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_discussions: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestAutoMergeDisabledPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestAutoMergeDisabledPayloadPullRequestLinks."""

    comments: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksStatusesDict]


class PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestAutoMergeEnabledPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestAutoMergeEnabledPayloadPullRequestLinks."""

    comments: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksStatusesDict]


class PullRequestDequeuedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestDequeuedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestDequeuedPayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestDequeuedPayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestDequeuedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestDequeuedPayloadPullRequestLinks."""

    comments: Required[PullRequestDequeuedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestDequeuedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestDequeuedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestDequeuedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestDequeuedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestDequeuedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestDequeuedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestDequeuedPayloadPullRequestLinksStatusesDict]


class PullRequestEditedPayloadChangesBaseDict(TypedDict, total=False):
    """PullRequestEditedPayloadChangesBase."""

    ref: Required[PullRequestEditedPayloadChangesBaseRefDict]
    sha: Required[PullRequestEditedPayloadChangesBaseShaDict]


class PullRequestEnqueuedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestEnqueuedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestEnqueuedPayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestEnqueuedPayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestEnqueuedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestEnqueuedPayloadPullRequestLinks."""

    comments: Required[PullRequestEnqueuedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestEnqueuedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestEnqueuedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestEnqueuedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestEnqueuedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestEnqueuedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestEnqueuedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestEnqueuedPayloadPullRequestLinksStatusesDict]


class PullRequestLabeledPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestLabeledPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestLabeledPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestLabeledPayloadPullRequestLinks."""

    comments: Required[PullRequestLabeledPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestLabeledPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestLabeledPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestLabeledPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestLabeledPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestLabeledPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestLabeledPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestLabeledPayloadPullRequestLinksStatusesDict]


class PullRequestLockedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestLockedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestLockedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestLockedPayloadPullRequestLinks."""

    comments: Required[PullRequestLockedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestLockedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestLockedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestLockedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestLockedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestLockedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestLockedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestLockedPayloadPullRequestLinksStatusesDict]


class PullRequestMinimalBaseDict(TypedDict, total=False):
    """PullRequestMinimalBase."""

    ref: Required[str]
    sha: Required[str]
    repo: Required[PullRequestMinimalBaseRepoDict]


class PullRequestMinimalHeadDict(TypedDict, total=False):
    """PullRequestMinimalHead."""

    ref: Required[str]
    sha: Required[str]
    repo: Required[PullRequestMinimalHeadRepoDict]


class PullRequestReviewCommentCreatedPayloadCommentLinksDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadCommentLinks."""

    html: Required[PullRequestReviewCommentCreatedPayloadCommentLinksHtmlDict]
    pull_request: Required[PullRequestReviewCommentCreatedPayloadCommentLinksPullRequestDict]
    self: Required[PullRequestReviewCommentCreatedPayloadCommentLinksSelfDict]


class PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewCommentCreatedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewCommentDeletedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewCommentDeletedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewCommentEditedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewCommentEditedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewCommentEditedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewCommentEditedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewDismissedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewDismissedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewDismissedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewDismissedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewDismissedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewDismissedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewDismissedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewDismissedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewDismissedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewDismissedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewDismissedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewDismissedPayloadReviewLinksDict(TypedDict, total=False):
    """PullRequestReviewDismissedPayloadReviewLinks."""

    html: Required[PullRequestReviewDismissedPayloadReviewLinksHtmlDict]
    pull_request: Required[PullRequestReviewDismissedPayloadReviewLinksPullRequestDict]


class PullRequestReviewEditedPayloadChangesDict(TypedDict, total=False):
    """PullRequestReviewEditedPayloadChanges."""

    body: NotRequired[PullRequestReviewEditedPayloadChangesBodyDict]


class PullRequestReviewEditedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewEditedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


class PullRequestReviewEditedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewEditedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewEditedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewEditedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewEditedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewEditedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewEditedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewEditedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewEditedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewEditedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewSubmittedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewSubmittedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewSubmittedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewSubmittedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewSubmittedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewSubmittedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewSubmittedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewSubmittedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewSubmittedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewSubmittedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewSubmittedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewThreadResolvedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewThreadResolvedPayloadThreadCommentLinksDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadThreadCommentLinks."""

    html: Required[PullRequestReviewThreadResolvedPayloadThreadCommentLinksHtmlDict]
    pull_request: Required[PullRequestReviewThreadResolvedPayloadThreadCommentLinksPullRequestDict]
    self: Required[PullRequestReviewThreadResolvedPayloadThreadCommentLinksSelfDict]


class PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestReviewThreadUnresolvedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestLinks."""

    comments: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksStatusesDict]


class PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadThreadCommentLinks."""

    html: Required[PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksHtmlDict]
    pull_request: Required[PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksPullRequestDict]
    self: Required[PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksSelfDict]


class PullRequestSynchronizePayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestSynchronizePayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestSynchronizePayloadPullRequestHeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestSynchronizePayloadPullRequestHeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestSynchronizePayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestSynchronizePayloadPullRequestLinks."""

    comments: Required[PullRequestSynchronizePayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestSynchronizePayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestSynchronizePayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestSynchronizePayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestSynchronizePayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestSynchronizePayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestSynchronizePayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestSynchronizePayloadPullRequestLinksStatusesDict]


class PullRequestUnassignedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestUnassignedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestUnassignedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestUnassignedPayloadPullRequestLinks."""

    comments: Required[PullRequestUnassignedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestUnassignedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestUnassignedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestUnassignedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestUnassignedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestUnassignedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestUnassignedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestUnassignedPayloadPullRequestLinksStatusesDict]


class PullRequestUnlabeledPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestUnlabeledPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestUnlabeledPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestUnlabeledPayloadPullRequestLinks."""

    comments: Required[PullRequestUnlabeledPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestUnlabeledPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestUnlabeledPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestUnlabeledPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestUnlabeledPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestUnlabeledPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestUnlabeledPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestUnlabeledPayloadPullRequestLinksStatusesDict]


class PullRequestUnlockedPayloadPullRequestBaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PullRequestUnlockedPayloadPullRequestBaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestUnlockedPayloadPullRequestLinksDict(TypedDict, total=False):
    """PullRequestUnlockedPayloadPullRequestLinks."""

    comments: Required[PullRequestUnlockedPayloadPullRequestLinksCommentsDict]
    commits: Required[PullRequestUnlockedPayloadPullRequestLinksCommitsDict]
    html: Required[PullRequestUnlockedPayloadPullRequestLinksHtmlDict]
    issue: Required[PullRequestUnlockedPayloadPullRequestLinksIssueDict]
    review_comment: Required[PullRequestUnlockedPayloadPullRequestLinksReviewCommentDict]
    review_comments: Required[PullRequestUnlockedPayloadPullRequestLinksReviewCommentsDict]
    self: Required[PullRequestUnlockedPayloadPullRequestLinksSelfDict]
    statuses: Required[PullRequestUnlockedPayloadPullRequestLinksStatusesDict]


class PushPayloadCommitDict(TypedDict, total=False):
    """Commit."""

    added: NotRequired[list[str]]
    author: Required[PushPayloadCommitAuthorDict]
    committer: Required[PushPayloadCommitCommitterDict]
    distinct: Required[bool]
    id: Required[str]
    message: Required[str]
    modified: NotRequired[list[str]]
    removed: NotRequired[list[str]]
    timestamp: Required[str]
    tree_id: Required[str]
    url: Required[str]


class PushPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: NotRequired[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[PushPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: NotRequired[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: NotRequired[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class RegistryPackagePublishedPayloadRegistryPackageDict(TypedDict, total=False):
    """RegistryPackagePublishedPayloadRegistryPackage."""

    created_at: Required[None | str]
    description: Required[None | str]
    ecosystem: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    namespace: Required[str]
    owner: Required[RegistryPackagePublishedPayloadRegistryPackageOwnerDict]
    package_type: Required[str]
    package_version: Required[Any | None]
    registry: Required[Any | None]
    updated_at: Required[None | str]


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersionRelease."""

    author: Required[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseAuthorDict]
    created_at: Required[str]
    draft: Required[bool]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    prerelease: Required[bool]
    published_at: Required[str]
    tag_name: Required[str]
    target_commitish: Required[str]
    url: Required[str]


class ReleaseEditedPayloadChangesDict(TypedDict, total=False):
    """ReleaseEditedPayloadChanges."""

    body: NotRequired[ReleaseEditedPayloadChangesBodyDict]
    name: NotRequired[ReleaseEditedPayloadChangesNameDict]
    tag_name: NotRequired[ReleaseEditedPayloadChangesTagNameDict]
    make_latest: NotRequired[ReleaseEditedPayloadChangesMakeLatestDict]


class ReleasePrereleasedPayloadReleaseDict(TypedDict, total=False):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    assets: Required[list[Any | None]]
    assets_url: Required[str]
    author: Required[Any | None]
    body: Required[None | str]
    created_at: Required[None | str]
    discussion_url: NotRequired[str]
    draft: Required[bool]
    html_url: Required[str]
    id: Required[int]
    immutable: Required[bool]
    name: Required[None | str]
    node_id: Required[str]
    prerelease: Required[Literal[True]]
    published_at: Required[None | str]
    reactions: NotRequired[ReleasePrereleasedPayloadReleaseReactionsDict]
    tag_name: Required[str]
    tarball_url: Required[None | str]
    target_commitish: Required[str]
    upload_url: Required[str]
    updated_at: Required[None | str]
    url: Required[str]
    zipball_url: Required[None | str]


class RepositoryAdvisoryDict(TypedDict, total=False):
    """A repository security advisory."""

    ghsa_id: Required[str]
    cve_id: Required[None | str]
    url: Required[str]
    html_url: Required[str]
    summary: Required[str]
    description: Required[None | str]
    severity: Required[Literal["critical", "high", "medium", "low"] | None]
    author: Required[None]
    publisher: Required[None]
    identifiers: Required[list[RepositoryAdvisoryIdentifierDict]]
    state: Required[Literal["published", "closed", "withdrawn", "draft", "triage"]]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    published_at: Required[None | str]
    closed_at: Required[None | str]
    withdrawn_at: Required[None | str]
    submission: Required[Any | None]
    vulnerabilities: Required[Any | None]
    cvss: Required[Any | None]
    cvss_severities: NotRequired[Any | None]
    cwes: Required[Any | None]
    cwe_ids: Required[Any | None]
    credits: Required[Any | None]
    credits_detailed: Required[Any | None]
    collaborating_users: Required[Any | None]
    collaborating_teams: Required[Any | None]
    private_fork: Required[None]


class RepositoryEditedPayloadChangesDict(TypedDict, total=False):
    """RepositoryEditedPayloadChanges."""

    default_branch: NotRequired[RepositoryEditedPayloadChangesDefaultBranchDict]
    description: NotRequired[RepositoryEditedPayloadChangesDescriptionDict]
    homepage: NotRequired[RepositoryEditedPayloadChangesHomepageDict]
    topics: NotRequired[RepositoryEditedPayloadChangesTopicsDict]


class RepositoryRenamedPayloadChangesRepositoryDict(TypedDict, total=False):
    """RepositoryRenamedPayloadChangesRepository."""

    name: Required[RepositoryRenamedPayloadChangesRepositoryNameDict]


class RepositoryRuleBranchNamePatternDict(TypedDict, total=False):
    """Parameters to be used for the branch_name_pattern rule."""

    type: Required[Literal["branch_name_pattern"]]
    parameters: NotRequired[RepositoryRuleBranchNamePatternParametersDict]


class RepositoryRuleCommitAuthorEmailPatternDict(TypedDict, total=False):
    """Parameters to be used for the commit_author_email_pattern rule."""

    type: Required[Literal["commit_author_email_pattern"]]
    parameters: NotRequired[RepositoryRuleCommitAuthorEmailPatternParametersDict]


class RepositoryRuleCommitMessagePatternDict(TypedDict, total=False):
    """Parameters to be used for the commit_message_pattern rule."""

    type: Required[Literal["commit_message_pattern"]]
    parameters: NotRequired[RepositoryRuleCommitMessagePatternParametersDict]


class RepositoryRuleCommitterEmailPatternDict(TypedDict, total=False):
    """Parameters to be used for the committer_email_pattern rule."""

    type: Required[Literal["committer_email_pattern"]]
    parameters: NotRequired[RepositoryRuleCommitterEmailPatternParametersDict]


class RepositoryRuleCopilotCodeReviewDict(TypedDict, total=False):
    """Request Copilot code review for new pull requests automatically if the author has access to Copilot code review and their premium requests quota has not reached the limit."""

    type: Required[Literal["copilot_code_review"]]
    parameters: NotRequired[RepositoryRuleCopilotCodeReviewParametersDict]


class RepositoryRuleFileExtensionRestrictionDict(TypedDict, total=False):
    """Prevent commits that include files with specified file extensions from being pushed to the commit graph."""

    type: Required[Literal["file_extension_restriction"]]
    parameters: NotRequired[RepositoryRuleFileExtensionRestrictionParametersDict]


class RepositoryRuleFilePathRestrictionDict(TypedDict, total=False):
    """Prevent commits that include changes in specified file and folder paths from being pushed to the commit graph. This includes absolute paths that contain file names."""

    type: Required[Literal["file_path_restriction"]]
    parameters: NotRequired[RepositoryRuleFilePathRestrictionParametersDict]


class RepositoryRuleMaxFilePathLengthDict(TypedDict, total=False):
    """Prevent commits that include file paths that exceed the specified character limit from being pushed to the commit graph."""

    type: Required[Literal["max_file_path_length"]]
    parameters: NotRequired[RepositoryRuleMaxFilePathLengthParametersDict]


class RepositoryRuleMaxFileSizeDict(TypedDict, total=False):
    """Prevent commits with individual files that exceed the specified limit from being pushed to the commit graph."""

    type: Required[Literal["max_file_size"]]
    parameters: NotRequired[RepositoryRuleMaxFileSizeParametersDict]


class RepositoryRuleMergeQueueDict(TypedDict, total=False):
    """Merges must be performed via a merge queue."""

    type: Required[Literal["merge_queue"]]
    parameters: NotRequired[RepositoryRuleMergeQueueParametersDict]


class RepositoryRuleRequiredDeploymentsDict(TypedDict, total=False):
    """Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule."""

    type: Required[Literal["required_deployments"]]
    parameters: NotRequired[RepositoryRuleRequiredDeploymentsParametersDict]


class RepositoryRuleTagNamePatternDict(TypedDict, total=False):
    """Parameters to be used for the tag_name_pattern rule."""

    type: Required[Literal["tag_name_pattern"]]
    parameters: NotRequired[RepositoryRuleTagNamePatternParametersDict]


class RepositoryRuleUpdateDict(TypedDict, total=False):
    """Only allow users with bypass permission to update matching refs."""

    type: Required[Literal["update"]]
    parameters: NotRequired[RepositoryRuleUpdateParametersDict]


class RepositoryRulesetConditionsDict(TypedDict, total=False):
    """Parameters for a repository ruleset ref name condition."""

    ref_name: NotRequired[RepositoryRulesetConditionsRefNameDict]


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdatedChanges."""

    condition_type: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesConditionTypeDict]
    target: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesTargetDict]
    include: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesIncludeDict]
    exclude: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesExcludeDict]


class RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesRulesUpdatedChanges."""

    configuration: NotRequired[RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesConfigurationDict]
    rule_type: NotRequired[RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesRuleTypeDict]
    pattern: NotRequired[RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesPatternDict]


class RepositoryRulesetLinksDict(TypedDict, total=False):
    """RepositoryRulesetLinks."""

    self: NotRequired[RepositoryRulesetLinksSelfDict]
    html: NotRequired[Any | None]


class RepositoryTransferredPayloadChangesOwnerFromDict(TypedDict, total=False):
    """RepositoryTransferredPayloadChangesOwnerFrom."""

    organization: NotRequired[RepositoryTransferredPayloadChangesOwnerFromOrganizationDict]
    user: NotRequired[Any | None]


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityDict(TypedDict, total=False):
    """SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerability."""

    first_patched_version: Required[Any | None]
    package: Required[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityPackageDict]
    severity: Required[str]
    vulnerable_version_range: Required[str]


SecurityAndAnalysisPayloadChangesDict = TypedDict(
    "SecurityAndAnalysisPayloadChangesDict",
    {
        "from": NotRequired[SecurityAndAnalysisPayloadChangesFromDict],
    },
    total=False,
)
SecurityAndAnalysisPayloadChangesDict.__doc__ = """SecurityAndAnalysisPayloadChanges."""


class SponsorshipEditedPayloadChangesDict(TypedDict, total=False):
    """SponsorshipEditedPayloadChanges."""

    privacy_level: NotRequired[SponsorshipEditedPayloadChangesPrivacyLevelDict]


class StatusPayloadBrancheDict(TypedDict, total=False):
    """StatusPayloadBranche."""

    commit: Required[StatusPayloadBrancheCommitDict]
    name: Required[str]
    protected: Required[bool]


class StatusPayloadCommitCommitDict(TypedDict, total=False):
    """StatusPayloadCommitCommit."""

    author: Required[Any]
    comment_count: Required[int]
    committer: Required[Any]
    message: Required[str]
    tree: Required[StatusPayloadCommitCommitTreeDict]
    url: Required[str]
    verification: Required[StatusPayloadCommitCommitVerificationDict]


class TeamAddedToRepositoryPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[TeamAddedToRepositoryPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


class TeamCreatedPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[TeamCreatedPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


class TeamDeletedPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[TeamDeletedPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


TeamEditedPayloadChangesRepositoryPermissionsDict = TypedDict(
    "TeamEditedPayloadChangesRepositoryPermissionsDict",
    {
        "from": Required[TeamEditedPayloadChangesRepositoryPermissionsFromDict],
    },
    total=False,
)
TeamEditedPayloadChangesRepositoryPermissionsDict.__doc__ = """TeamEditedPayloadChangesRepositoryPermissions."""


class TeamEditedPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[TeamEditedPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


class TeamRemovedFromRepositoryPayloadRepositoryDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    custom_properties: NotRequired[dict[str, Any]]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[TeamRemovedFromRepositoryPayloadRepositoryPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]


class WebhookRubygemsMetadataDict(TypedDict, total=False):
    """Ruby Gems metadata."""

    name: NotRequired[str]
    description: NotRequired[str]
    readme: NotRequired[str]
    homepage: NotRequired[str]
    version_info: NotRequired[WebhookRubygemsMetadataVersionInfoDict]
    platform: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    repo: NotRequired[str]
    dependencies: NotRequired[list[dict[str, Any]]]
    commit_oid: NotRequired[str]


class WebhooksAnswerDict(TypedDict, total=False):
    """WebhooksAnswer."""

    author_association: Required[
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
    ]
    body: Required[str]
    child_comment_count: Required[int]
    created_at: Required[str]
    discussion_id: Required[int]
    html_url: Required[str]
    id: Required[int]
    node_id: Required[str]
    parent_id: Required[None]
    reactions: NotRequired[WebhooksAnswerReactionsDict]
    repository_url: Required[str]
    updated_at: Required[str]
    user: Required[Any | None]


WebhooksChanges8TierDict = TypedDict(
    "WebhooksChanges8TierDict",
    {
        "from": Required[WebhooksChanges8TierFromDict],
    },
    total=False,
)
WebhooksChanges8TierDict.__doc__ = """WebhooksChanges8Tier."""


class WebhooksChangesDict(TypedDict, total=False):
    """The changes to the comment."""

    body: NotRequired[WebhooksChangesBodyDict]


class WebhooksCommentDict(TypedDict, total=False):
    """WebhooksComment."""

    author_association: Required[
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
    ]
    body: Required[str]
    child_comment_count: Required[int]
    created_at: Required[str]
    discussion_id: Required[int]
    html_url: Required[str]
    id: Required[int]
    node_id: Required[str]
    parent_id: Required[None | int]
    reactions: Required[WebhooksCommentReactionsDict]
    repository_url: Required[str]
    updated_at: Required[str]
    user: Required[Any | None]


class WebhooksIssueCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself."""

    author_association: Required[
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
    ]
    body: Required[str]
    created_at: Required[str]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    node_id: Required[str]
    performed_via_github_app: Required[Any | None]
    reactions: Required[WebhooksIssueCommentReactionsDict]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class WebhooksMarketplacePurchaseDict(TypedDict, total=False):
    """Marketplace Purchase."""

    account: Required[WebhooksMarketplacePurchaseAccountDict]
    billing_cycle: Required[str]
    free_trial_ends_on: Required[None | str]
    next_billing_date: Required[None | str]
    on_free_trial: Required[bool]
    plan: Required[WebhooksMarketplacePurchasePlanDict]
    unit_count: Required[int]


class WebhooksPreviousMarketplacePurchaseDict(TypedDict, total=False):
    """Marketplace Purchase."""

    account: Required[WebhooksPreviousMarketplacePurchaseAccountDict]
    billing_cycle: Required[str]
    free_trial_ends_on: Required[None]
    next_billing_date: NotRequired[None | str]
    on_free_trial: Required[bool]
    plan: Required[WebhooksPreviousMarketplacePurchasePlanDict]
    unit_count: Required[int]


class WebhooksProjectChangesDict(TypedDict, total=False):
    """WebhooksProjectChanges."""

    archived_at: NotRequired[WebhooksProjectChangesArchivedAtDict]


class WebhooksPullRequest5BaseRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[WebhooksPullRequest5BaseRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class WebhooksPullRequest5HeadRepoDict(TypedDict, total=False):
    """A git repository."""

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: Required[str]
    archived: Required[bool]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    clone_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    created_at: Required[int | str]
    default_branch: Required[str]
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: Required[str]
    description: Required[None | str]
    disabled: NotRequired[bool]
    downloads_url: Required[str]
    events_url: Required[str]
    fork: Required[bool]
    forks: Required[int]
    forks_count: Required[int]
    forks_url: Required[str]
    full_name: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    has_downloads: Required[bool]
    has_issues: Required[bool]
    has_pages: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_discussions: Required[bool]
    homepage: Required[None | str]
    hooks_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    is_template: NotRequired[bool]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    language: Required[None | str]
    languages_url: Required[str]
    license: Required[Any | None]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: Required[str]
    milestones_url: Required[str]
    mirror_url: Required[None | str]
    name: Required[str]
    node_id: Required[str]
    notifications_url: Required[str]
    open_issues: Required[int]
    open_issues_count: Required[int]
    organization: NotRequired[str]
    owner: Required[Any | None]
    permissions: NotRequired[WebhooksPullRequest5HeadRepoPermissionsDict]
    private: Required[bool]
    public: NotRequired[bool]
    pulls_url: Required[str]
    pushed_at: Required[int | str]
    releases_url: Required[str]
    role_name: NotRequired[None | str]
    size: Required[int]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: Required[str]
    stargazers: NotRequired[int]
    stargazers_count: Required[int]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    svn_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    topics: Required[list[str]]
    trees_url: Required[str]
    updated_at: Required[str]
    url: Required[str]
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Required[Literal["public", "private", "internal"]]
    watchers: Required[int]
    watchers_count: Required[int]
    web_commit_signoff_required: NotRequired[bool]


class WebhooksPullRequest5LinksDict(TypedDict, total=False):
    """WebhooksPullRequest5Links."""

    comments: Required[WebhooksPullRequest5LinksCommentsDict]
    commits: Required[WebhooksPullRequest5LinksCommitsDict]
    html: Required[WebhooksPullRequest5LinksHtmlDict]
    issue: Required[WebhooksPullRequest5LinksIssueDict]
    review_comment: Required[WebhooksPullRequest5LinksReviewCommentDict]
    review_comments: Required[WebhooksPullRequest5LinksReviewCommentsDict]
    self: Required[WebhooksPullRequest5LinksSelfDict]
    statuses: Required[WebhooksPullRequest5LinksStatusesDict]


class WebhooksRelease1Dict(TypedDict, total=False):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    assets: Required[list[Any | None]]
    assets_url: Required[str]
    author: Required[Any | None]
    body: Required[None | str]
    created_at: Required[None | str]
    discussion_url: NotRequired[str]
    draft: Required[bool]
    html_url: Required[str]
    id: Required[int]
    immutable: Required[bool]
    name: Required[None | str]
    node_id: Required[str]
    prerelease: Required[bool]
    published_at: Required[None | str]
    reactions: NotRequired[WebhooksRelease1ReactionsDict]
    tag_name: Required[str]
    tarball_url: Required[None | str]
    target_commitish: Required[str]
    updated_at: Required[None | str]
    upload_url: Required[str]
    url: Required[str]
    zipball_url: Required[None | str]


class WebhooksReleaseDict(TypedDict, total=False):
    """The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object."""

    assets: Required[list[WebhooksReleaseAssetDict]]
    assets_url: Required[str]
    author: Required[Any | None]
    body: Required[None | str]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    discussion_url: NotRequired[str]
    draft: Required[bool]
    html_url: Required[str]
    id: Required[int]
    immutable: Required[bool]
    name: Required[None | str]
    node_id: Required[str]
    prerelease: Required[bool]
    published_at: Required[None | str]
    reactions: NotRequired[WebhooksReleaseReactionsDict]
    tag_name: Required[str]
    tarball_url: Required[None | str]
    target_commitish: Required[str]
    upload_url: Required[str]
    url: Required[str]
    zipball_url: Required[None | str]


class WebhooksReviewCommentLinksDict(TypedDict, total=False):
    """WebhooksReviewCommentLinks."""

    html: Required[WebhooksReviewCommentLinksHtmlDict]
    pull_request: Required[WebhooksReviewCommentLinksPullRequestDict]
    self: Required[WebhooksReviewCommentLinksSelfDict]


class WebhooksReviewLinksDict(TypedDict, total=False):
    """WebhooksReviewLinks."""

    html: Required[WebhooksReviewLinksHtmlDict]
    pull_request: Required[WebhooksReviewLinksPullRequestDict]


class WebhooksSecurityAdvisoryVulnerabilityDict(TypedDict, total=False):
    """WebhooksSecurityAdvisoryVulnerability."""

    first_patched_version: Required[Any | None]
    package: Required[WebhooksSecurityAdvisoryVulnerabilityPackageDict]
    severity: Required[str]
    vulnerable_version_range: Required[str]


class WebhooksSponsorshipDict(TypedDict, total=False):
    """WebhooksSponsorship."""

    created_at: Required[str]
    maintainer: NotRequired[WebhooksSponsorshipMaintainerDict]
    node_id: Required[str]
    privacy_level: Required[str]
    sponsor: Required[Any | None]
    sponsorable: Required[Any | None]
    tier: Required[WebhooksSponsorshipTierDict]


class WorkflowJobQueuedPayloadWorkflowJobDict(TypedDict, total=False):
    """WorkflowJobQueuedPayloadWorkflowJob."""

    check_run_url: Required[str]
    completed_at: Required[None | str]
    conclusion: Required[None | str]
    created_at: Required[str]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: Required[list[str]]
    name: Required[str]
    node_id: Required[str]
    run_attempt: Required[int]
    run_id: Required[float]
    run_url: Required[str]
    runner_group_id: Required[None | int]
    runner_group_name: Required[None | str]
    runner_id: Required[None | int]
    runner_name: Required[None | str]
    started_at: Required[str]
    status: Required[Literal["queued", "in_progress", "completed", "waiting"]]
    head_branch: Required[None | str]
    workflow_name: Required[None | str]
    steps: Required[list[WorkflowJobQueuedPayloadWorkflowJobStepDict]]
    url: Required[str]


class WorkflowJobWaitingPayloadWorkflowJobDict(TypedDict, total=False):
    """WorkflowJobWaitingPayloadWorkflowJob."""

    check_run_url: Required[str]
    completed_at: Required[None | str]
    conclusion: Required[None | str]
    created_at: Required[str]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: Required[list[str]]
    name: Required[str]
    node_id: Required[str]
    run_attempt: Required[int]
    run_id: Required[float]
    run_url: Required[str]
    runner_group_id: Required[None | int]
    runner_group_name: Required[None | str]
    runner_id: Required[None | int]
    runner_name: Required[None | str]
    started_at: Required[str]
    head_branch: Required[None | str]
    workflow_name: Required[None | str]
    status: Required[Literal["queued", "in_progress", "completed", "waiting"]]
    steps: Required[list[WorkflowJobWaitingPayloadWorkflowJobStepDict]]
    url: Required[str]


class WorkflowRunCompletedPayloadWorkflowRunHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[WorkflowRunCompletedPayloadWorkflowRunHeadCommitAuthorDict]
    committer: Required[WorkflowRunCompletedPayloadWorkflowRunHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class WorkflowRunInProgressPayloadWorkflowRunHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[WorkflowRunInProgressPayloadWorkflowRunHeadCommitAuthorDict]
    committer: Required[WorkflowRunInProgressPayloadWorkflowRunHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunHeadCommitDict(TypedDict, total=False):
    """SimpleCommit."""

    author: Required[WorkflowRunRequestedPayloadWorkflowRunHeadCommitAuthorDict]
    committer: Required[WorkflowRunRequestedPayloadWorkflowRunHeadCommitCommitterDict]
    id: Required[str]
    message: Required[str]
    timestamp: Required[str]
    tree_id: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseDict(TypedDict, total=False):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequestBase."""

    ref: Required[str]
    repo: Required[WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseRepoDict]
    sha: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadDict(TypedDict, total=False):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequestHead."""

    ref: Required[str]
    repo: Required[WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadRepoDict]
    sha: Required[str]


class DependabotAlertDependencyDict(TypedDict, total=False):
    """Details for the vulnerable dependency."""

    package: NotRequired[DependabotAlertPackageDict]
    manifest_path: NotRequired[str]
    scope: NotRequired[Literal["development", "runtime"] | None]
    relationship: NotRequired[Literal["unknown", "direct", "transitive"] | None]


class DependabotAlertSecurityVulnerabilityDict(TypedDict, total=False):
    """Details pertaining to one vulnerable version range for the advisory."""

    package: Required[DependabotAlertPackageDict]
    severity: Required[Literal["low", "medium", "high", "critical"]]
    vulnerable_version_range: Required[str]
    first_patched_version: Required[Any | None]


class PingPayloadHookDict(TypedDict, total=False):
    """The webhook that is being pinged."""

    active: Required[bool]
    app_id: NotRequired[int]
    config: Required[PingPayloadHookConfigDict]
    created_at: Required[str]
    deliveries_url: NotRequired[str]
    events: Required[list[str]]
    id: Required[int]
    last_response: NotRequired[HookResponseDict]
    name: Required[Literal["web"]]
    ping_url: NotRequired[str]
    test_url: NotRequired[str]
    type: Required[str]
    updated_at: Required[str]
    url: NotRequired[str]


class DiscussionDict(TypedDict, total=False):
    """A Discussion in a repository."""

    active_lock_reason: Required[None | str]
    answer_chosen_at: Required[None | str]
    answer_chosen_by: Required[Any | None]
    answer_html_url: Required[None | str]
    author_association: Required[
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
    ]
    body: Required[str]
    category: Required[DiscussionCategoryDict]
    comments: Required[int]
    created_at: Required[str]
    html_url: Required[str]
    id: Required[int]
    locked: Required[bool]
    node_id: Required[str]
    number: Required[int]
    reactions: NotRequired[DiscussionReactionsDict]
    repository_url: Required[str]
    state: Required[Literal["open", "closed", "locked", "converting", "transferring"]]
    state_reason: Required[Literal["resolved", "outdated", "duplicate", "reopened"] | None]
    timeline_url: NotRequired[str]
    title: Required[str]
    updated_at: Required[str]
    user: Required[Any | None]
    labels: NotRequired[list[LabelDict]]


class PullRequestLinksDict(TypedDict, total=False):
    """PullRequestLinks."""

    comments: Required[LinkDict]
    commits: Required[LinkDict]
    statuses: Required[LinkDict]
    html: Required[LinkDict]
    issue: Required[LinkDict]
    review_comments: Required[LinkDict]
    review_comment: Required[LinkDict]
    self: Required[LinkDict]


ProjectsV2ItemEditedPayloadChangesOption1FieldValueDict = TypedDict(
    "ProjectsV2ItemEditedPayloadChangesOption1FieldValueDict",
    {
        "field_node_id": NotRequired[str],
        "field_type": NotRequired[str],
        "field_name": NotRequired[str],
        "project_number": NotRequired[int],
        "from": NotRequired[ProjectsV2IterationSettingDict | ProjectsV2SingleSelectOptionDict | int | str],
        "to": NotRequired[ProjectsV2IterationSettingDict | ProjectsV2SingleSelectOptionDict | int | str],
    },
    total=False,
)
ProjectsV2ItemEditedPayloadChangesOption1FieldValueDict.__doc__ = (
    """ProjectsV2ItemEditedPayloadChangesOption1FieldValue."""
)


class RepositoryRuleCodeScanningParametersDict(TypedDict, total=False):
    """RepositoryRuleCodeScanningParameters."""

    code_scanning_tools: Required[list[RepositoryRuleParamsCodeScanningToolDict]]


class RepositoryRuleParamsRequiredReviewerConfigurationDict(TypedDict, total=False):
    """A reviewing team, and file patterns describing which files they must approve changes to."""

    file_patterns: Required[list[str]]
    minimum_approvals: Required[int]
    reviewer: Required[RepositoryRuleParamsReviewerDict]


class RepositoryRuleRequiredStatusChecksParametersDict(TypedDict, total=False):
    """RepositoryRuleRequiredStatusChecksParameters."""

    do_not_enforce_on_create: NotRequired[bool]
    required_status_checks: Required[list[RepositoryRuleParamsStatusCheckConfigurationDict]]
    strict_required_status_checks_policy: Required[bool]


class RepositoryRuleWorkflowsParametersDict(TypedDict, total=False):
    """RepositoryRuleWorkflowsParameters."""

    do_not_enforce_on_create: NotRequired[bool]
    workflows: Required[list[RepositoryRuleParamsWorkflowFileReferenceDict]]


class SecretScanningLocationDict(TypedDict, total=False):
    """SecretScanningLocation."""

    type: NotRequired[
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
    ]
    details: NotRequired[
        SecretScanningLocationCommitDict
        | SecretScanningLocationDiscussionBodyDict
        | SecretScanningLocationDiscussionCommentDict
        | SecretScanningLocationDiscussionTitleDict
        | SecretScanningLocationIssueBodyDict
        | SecretScanningLocationIssueCommentDict
        | SecretScanningLocationIssueTitleDict
        | SecretScanningLocationPullRequestBodyDict
        | SecretScanningLocationPullRequestCommentDict
        | SecretScanningLocationPullRequestReviewCommentDict
        | SecretScanningLocationPullRequestReviewDict
        | SecretScanningLocationPullRequestTitleDict
        | SecretScanningLocationWikiCommitDict
    ]


class MergeGroupDict(TypedDict, total=False):
    """A group of pull requests that the merge queue has grouped together to be merged."""

    head_sha: Required[str]
    head_ref: Required[str]
    base_sha: Required[str]
    base_ref: Required[str]
    head_commit: Required[SimpleCommitDict]


class CodeScanningAlertAppearedInBranchPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    assignees: NotRequired[list[UserDict]]
    created_at: Required[str]
    dismissed_at: Required[None | str]
    dismissed_by: Required[Any | None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[Literal["false positive", "won't fix", "used in tests"] | None]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertAppearedInBranchPayloadAlertRuleDict]
    state: Required[Literal["open", "dismissed", "fixed"] | None]
    tool: Required[CodeScanningAlertAppearedInBranchPayloadAlertToolDict]
    url: Required[str]


class CodeScanningAlertClosedByUserPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    assignees: NotRequired[list[UserDict]]
    created_at: Required[str]
    dismissed_at: Required[str]
    dismissed_by: Required[Any | None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[Literal["false positive", "won't fix", "used in tests"] | None]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertClosedByUserPayloadAlertRuleDict]
    state: Required[Literal["dismissed", "fixed"]]
    tool: Required[CodeScanningAlertClosedByUserPayloadAlertToolDict]
    url: Required[str]
    dismissal_approved_by: NotRequired[Any | None]


class CodeScanningAlertCreatedPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    created_at: Required[None | str]
    dismissed_at: Required[None]
    dismissed_by: Required[None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[None]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    instances_url: NotRequired[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertCreatedPayloadAlertRuleDict]
    state: Required[Literal["open", "dismissed"] | None]
    tool: Required[Any | None]
    updated_at: NotRequired[None | str]
    url: Required[str]
    dismissal_approved_by: NotRequired[None]
    assignees: NotRequired[list[UserDict]]


class CodeScanningAlertFixedPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    assignees: NotRequired[list[UserDict]]
    created_at: Required[str]
    dismissed_at: Required[None | str]
    dismissed_by: Required[Any | None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[Literal["false positive", "won't fix", "used in tests"] | None]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    instances_url: NotRequired[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertFixedPayloadAlertRuleDict]
    state: Required[Literal["fixed"] | None]
    tool: Required[CodeScanningAlertFixedPayloadAlertToolDict]
    url: Required[str]


class CodeScanningAlertReopenedByUserPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    assignees: NotRequired[list[UserDict]]
    created_at: Required[str]
    dismissed_at: Required[None]
    dismissed_by: Required[None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[None]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertReopenedByUserPayloadAlertRuleDict]
    state: Required[Literal["open", "fixed"] | None]
    tool: Required[CodeScanningAlertReopenedByUserPayloadAlertToolDict]
    url: Required[str]


class CodeScanningAlertReopenedPayloadAlertDict(TypedDict, total=False):
    """The code scanning alert involved in the event."""

    assignees: NotRequired[list[UserDict]]
    created_at: Required[str]
    dismissed_at: Required[None | str]
    dismissed_by: Required[Any | None]
    dismissed_comment: NotRequired[None | str]
    dismissed_reason: Required[None | str]
    fixed_at: NotRequired[None]
    html_url: Required[str]
    instances_url: NotRequired[str]
    most_recent_instance: NotRequired[Any | None]
    number: Required[int]
    rule: Required[CodeScanningAlertReopenedPayloadAlertRuleDict]
    state: Required[Literal["open", "dismissed", "fixed"] | None]
    tool: Required[CodeScanningAlertReopenedPayloadAlertToolDict]
    updated_at: NotRequired[None | str]
    url: Required[str]
    dismissal_approved_by: NotRequired[None]


class DeploymentDict(TypedDict, total=False):
    """A request for a specific ref(branch,sha,tag) to be deployed."""

    url: Required[str]
    id: Required[int]
    node_id: Required[str]
    sha: Required[str]
    ref: Required[str]
    task: Required[str]
    payload: Required[dict[str, Any] | str]
    original_environment: NotRequired[str]
    environment: Required[str]
    description: Required[None | str]
    creator: Required[None | UserDict]
    created_at: Required[str]
    updated_at: Required[str]
    statuses_url: Required[str]
    repository_url: Required[str]
    transient_environment: NotRequired[bool]
    production_environment: NotRequired[bool]
    performed_via_github_app: NotRequired[Any | None]


class InstallationDict2(TypedDict, total=False):
    """Installation."""

    id: Required[int]
    account: Required[EnterpriseDict2 | UserDict]
    repository_selection: Required[Literal["all", "selected"]]
    access_tokens_url: Required[str]
    repositories_url: Required[str]
    html_url: Required[str]
    app_id: Required[int]
    client_id: NotRequired[str]
    target_id: Required[int]
    target_type: Required[str]
    permissions: Required[AppPermissionsDict]
    events: Required[list[str]]
    created_at: Required[str]
    updated_at: Required[str]
    single_file_name: Required[None | str]
    has_multiple_single_files: NotRequired[bool]
    single_file_paths: NotRequired[list[str]]
    app_slug: Required[str]
    suspended_by: Required[None | UserDict]
    suspended_at: Required[None | str]
    contact_email: NotRequired[None | str]


class MilestoneDict(TypedDict, total=False):
    """A collection of related issues and pull requests."""

    url: Required[str]
    html_url: Required[str]
    labels_url: Required[str]
    id: Required[int]
    node_id: Required[str]
    number: Required[int]
    state: Required[Literal["open", "closed"]]
    title: Required[str]
    description: Required[None | str]
    creator: Required[None | UserDict]
    open_issues: Required[int]
    closed_issues: Required[int]
    created_at: Required[str]
    updated_at: Required[str]
    closed_at: Required[None | str]
    due_on: Required[None | str]


class MinimalRepositoryDict(TypedDict, total=False):
    """Minimal Repository."""

    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    full_name: Required[str]
    owner: Required[UserDict]
    private: Required[bool]
    html_url: Required[str]
    description: Required[None | str]
    fork: Required[bool]
    url: Required[str]
    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    downloads_url: Required[str]
    events_url: Required[str]
    forks_url: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: NotRequired[str]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    notifications_url: Required[str]
    pulls_url: Required[str]
    releases_url: Required[str]
    ssh_url: NotRequired[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    clone_url: NotRequired[str]
    mirror_url: NotRequired[None | str]
    hooks_url: Required[str]
    svn_url: NotRequired[str]
    homepage: NotRequired[None | str]
    language: NotRequired[None | str]
    forks_count: NotRequired[int]
    stargazers_count: NotRequired[int]
    watchers_count: NotRequired[int]
    size: NotRequired[int]
    default_branch: NotRequired[str]
    open_issues_count: NotRequired[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    has_pages: NotRequired[bool]
    has_downloads: NotRequired[bool]
    has_discussions: NotRequired[bool]
    archived: NotRequired[bool]
    disabled: NotRequired[bool]
    visibility: NotRequired[str]
    pushed_at: NotRequired[None | str]
    created_at: NotRequired[None | str]
    updated_at: NotRequired[None | str]
    permissions: NotRequired[MinimalRepositoryPermissionsDict]
    role_name: NotRequired[str]
    temp_clone_token: NotRequired[str]
    delete_branch_on_merge: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    code_of_conduct: NotRequired[CodeOfConductDict]
    license: NotRequired[Any | None]
    forks: NotRequired[int]
    open_issues: NotRequired[int]
    watchers: NotRequired[int]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    security_and_analysis: NotRequired[Any | None]
    custom_properties: NotRequired[dict[str, Any]]


class PersonalAccessTokenRequestDict(TypedDict, total=False):
    """Details of a Personal Access Token Request."""

    id: Required[int]
    owner: Required[UserDict]
    permissions_added: Required[PersonalAccessTokenRequestPermissionsAddedDict]
    permissions_upgraded: Required[PersonalAccessTokenRequestPermissionsUpgradedDict]
    permissions_result: Required[PersonalAccessTokenRequestPermissionsResultDict]
    repository_selection: Required[Literal["none", "all", "subset"]]
    repository_count: Required[None | int]
    repositories: Required[Any | None]
    created_at: Required[str]
    token_id: Required[int]
    token_name: Required[str]
    token_expired: Required[bool]
    token_expires_at: Required[None | str]
    token_last_used_at: Required[None | str]


class ProjectsV2ItemDict(TypedDict, total=False):
    """An item belonging to a project."""

    id: Required[float]
    node_id: NotRequired[str]
    project_node_id: NotRequired[str]
    content_node_id: Required[str]
    content_type: Required[Literal["Issue", "PullRequest", "DraftIssue"]]
    creator: NotRequired[UserDict]
    created_at: Required[str]
    updated_at: Required[str]
    archived_at: Required[None | str]


class ProjectsV2StatusUpdateDict(TypedDict, total=False):
    """An status update belonging to a project."""

    id: Required[float]
    node_id: Required[str]
    project_node_id: NotRequired[str]
    creator: NotRequired[UserDict]
    created_at: Required[str]
    updated_at: Required[str]
    status: NotRequired[Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"] | None]
    start_date: NotRequired[str]
    target_date: NotRequired[str]
    body: NotRequired[None | str]


class RepositoryDict2(TypedDict, total=False):
    """A repository on GitHub."""

    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    full_name: Required[str]
    license: Required[LicenseSimpleDict | None]
    forks: Required[int]
    permissions: NotRequired[Repository2PermissionsDict]
    owner: Required[UserDict]
    private: Required[bool]
    html_url: Required[str]
    description: Required[None | str]
    fork: Required[bool]
    url: Required[str]
    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    downloads_url: Required[str]
    events_url: Required[str]
    forks_url: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    notifications_url: Required[str]
    pulls_url: Required[str]
    releases_url: Required[str]
    ssh_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    clone_url: Required[str]
    mirror_url: Required[None | str]
    hooks_url: Required[str]
    svn_url: Required[str]
    homepage: Required[None | str]
    language: Required[None | str]
    forks_count: Required[int]
    stargazers_count: Required[int]
    watchers_count: Required[int]
    size: Required[int]
    default_branch: Required[str]
    open_issues_count: Required[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_pages: Required[bool]
    has_downloads: Required[bool]
    has_discussions: NotRequired[bool]
    archived: Required[bool]
    disabled: Required[bool]
    visibility: NotRequired[str]
    pushed_at: Required[None | str]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    allow_rebase_merge: NotRequired[bool]
    temp_clone_token: NotRequired[str]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_merge_commit: NotRequired[bool]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    open_issues: Required[int]
    watchers: Required[int]
    master_branch: NotRequired[str]
    starred_at: NotRequired[str]
    anonymous_access_enabled: NotRequired[bool]
    code_search_index_status: NotRequired[Repository2CodeSearchIndexStatusDict]


class RepositoryDict(TypedDict, total=False):
    """The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property when the event occurs from activity in a repository."""

    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    full_name: Required[str]
    license: Required[LicenseSimpleDict | None]
    organization: NotRequired[None | UserDict]
    forks: Required[int]
    permissions: NotRequired[RepositoryPermissionsDict]
    owner: Required[UserDict]
    private: Required[bool]
    html_url: Required[str]
    description: Required[None | str]
    fork: Required[bool]
    url: Required[str]
    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    downloads_url: Required[str]
    events_url: Required[str]
    forks_url: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    notifications_url: Required[str]
    pulls_url: Required[str]
    releases_url: Required[str]
    ssh_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    clone_url: Required[str]
    mirror_url: Required[None | str]
    hooks_url: Required[str]
    svn_url: Required[str]
    homepage: Required[None | str]
    language: Required[None | str]
    forks_count: Required[int]
    stargazers_count: Required[int]
    watchers_count: Required[int]
    size: Required[int]
    default_branch: Required[str]
    open_issues_count: Required[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    custom_properties: NotRequired[dict[str, Any]]
    has_issues: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_pages: Required[bool]
    has_downloads: Required[bool]
    has_discussions: NotRequired[bool]
    archived: Required[bool]
    disabled: Required[bool]
    visibility: NotRequired[str]
    pushed_at: Required[None | str]
    created_at: Required[None | str]
    updated_at: Required[None | str]
    allow_rebase_merge: NotRequired[bool]
    template_repository: NotRequired[Any | None]
    temp_clone_token: NotRequired[str]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_merge_commit: NotRequired[bool]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    open_issues: Required[int]
    watchers: Required[int]
    master_branch: NotRequired[str]
    starred_at: NotRequired[str]
    anonymous_access_enabled: NotRequired[bool]


class SecretScanningAlertWebhookDict(TypedDict, total=False):
    """SecretScanningAlertWebhook."""

    number: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[None | str]
    url: NotRequired[str]
    html_url: NotRequired[str]
    locations_url: NotRequired[str]
    resolution: NotRequired[
        Literal["false_positive", "wont_fix", "revoked", "used_in_tests", "pattern_deleted", "pattern_edited"] | None
    ]
    resolved_at: NotRequired[None | str]
    resolved_by: NotRequired[None | UserDict]
    resolution_comment: NotRequired[None | str]
    secret_type: NotRequired[str]
    secret_type_display_name: NotRequired[str]
    validity: NotRequired[Literal["active", "inactive", "unknown"]]
    push_protection_bypassed: NotRequired[None | bool]
    push_protection_bypassed_by: NotRequired[None | UserDict]
    push_protection_bypassed_at: NotRequired[None | str]
    push_protection_bypass_request_reviewer: NotRequired[None | UserDict]
    push_protection_bypass_request_reviewer_comment: NotRequired[None | str]
    push_protection_bypass_request_comment: NotRequired[None | str]
    push_protection_bypass_request_html_url: NotRequired[None | str]
    publicly_leaked: NotRequired[None | bool]
    multi_repo: NotRequired[None | bool]
    assigned_to: NotRequired[None | UserDict]


class CustomPropertyCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `created`."""

    action: Required[Literal["created"]]
    definition: Required[CustomPropertyDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    sender: NotRequired[UserDict]


class CustomPropertyDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    definition: Required[CustomPropertyDeletedPayloadDefinitionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    sender: NotRequired[UserDict]


class CustomPropertyPromoteToEnterprisePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `promote_to_enterprise`."""

    action: Required[Literal["promote_to_enterprise"]]
    definition: Required[CustomPropertyDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    sender: NotRequired[UserDict]


class CustomPropertyUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom_property` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    definition: Required[CustomPropertyDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    sender: NotRequired[UserDict]


class GithubAppAuthorizationRevokedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `github_app_authorization` webhook with action `revoked`."""

    action: Required[Literal["revoked"]]
    sender: Required[UserDict]


class IssuesDeletedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[IssuesDeletedPayloadIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesDeletedPayloadIssuePullRequestDict]
    reactions: Required[IssuesDeletedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesDemilestonedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[Any | None]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesDemilestonedPayloadIssuePullRequestDict]
    reactions: Required[IssuesDemilestonedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesEditedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[IssuesEditedPayloadIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesEditedPayloadIssuePullRequestDict]
    reactions: Required[IssuesEditedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    type: NotRequired[Any | None]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesLabeledPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[IssuesLabeledPayloadIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesLabeledPayloadIssuePullRequestDict]
    reactions: Required[IssuesLabeledPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    type: NotRequired[Any | None]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesLockedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[Any | None]]
    labels_url: Required[str]
    locked: Required[Literal[True]]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesLockedPayloadIssuePullRequestDict]
    reactions: Required[IssuesLockedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    type: NotRequired[Any | None]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesMilestonedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[Any | None]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesMilestonedPayloadIssuePullRequestDict]
    reactions: Required[IssuesMilestonedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesOpenedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[IssuesOpenedPayloadIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesOpenedPayloadIssuePullRequestDict]
    reactions: Required[IssuesOpenedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesReopenedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[Any | None]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesReopenedPayloadIssuePullRequestDict]
    reactions: Required[IssuesReopenedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: Required[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]
    type: NotRequired[Any | None]


class IssuesTransferredPayloadChangesNewIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[IssuesTransferredPayloadChangesNewIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesTransferredPayloadChangesNewIssuePullRequestDict]
    reactions: Required[IssuesTransferredPayloadChangesNewIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class IssuesUnlockedPayloadIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[Any | None]]
    labels_url: Required[str]
    locked: Required[Literal[False]]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[IssuesUnlockedPayloadIssuePullRequestDict]
    reactions: Required[IssuesUnlockedPayloadIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class WebhooksIssueDict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[WebhooksIssueLabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[WebhooksIssuePullRequestDict]
    reactions: Required[WebhooksIssueReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class WebhooksIssue2Dict(TypedDict, total=False):
    """The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself."""

    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: NotRequired[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments: Required[int]
    comments_url: Required[str]
    created_at: Required[str]
    draft: NotRequired[bool]
    events_url: Required[str]
    html_url: Required[str]
    id: Required[int]
    labels: NotRequired[list[WebhooksIssue2LabelDict]]
    labels_url: Required[str]
    locked: NotRequired[bool]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    performed_via_github_app: NotRequired[Any | None]
    pull_request: NotRequired[WebhooksIssue2PullRequestDict]
    reactions: Required[WebhooksIssue2ReactionsDict]
    repository_url: Required[str]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[None | str]
    timeline_url: NotRequired[str]
    title: Required[str]
    type: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class CheckSuiteCompletedPayloadCheckSuitePullRequestDict(TypedDict, total=False):
    """Check Run Pull Request."""

    base: Required[CheckSuiteCompletedPayloadCheckSuitePullRequestBaseDict]
    head: Required[CheckSuiteCompletedPayloadCheckSuitePullRequestHeadDict]
    id: Required[int]
    number: Required[int]
    url: Required[str]


class CheckSuiteRequestedPayloadCheckSuitePullRequestDict(TypedDict, total=False):
    """Check Run Pull Request."""

    base: Required[CheckSuiteRequestedPayloadCheckSuitePullRequestBaseDict]
    head: Required[CheckSuiteRequestedPayloadCheckSuitePullRequestHeadDict]
    id: Required[int]
    number: Required[int]
    url: Required[str]


class CheckSuiteRerequestedPayloadCheckSuitePullRequestDict(TypedDict, total=False):
    """Check Run Pull Request."""

    base: Required[CheckSuiteRerequestedPayloadCheckSuitePullRequestBaseDict]
    head: Required[CheckSuiteRerequestedPayloadCheckSuitePullRequestHeadDict]
    id: Required[int]
    number: Required[int]
    url: Required[str]


class DiscussionCategoryChangedPayloadChangesDict(TypedDict, total=False):
    """DiscussionCategoryChangedPayloadChanges."""

    category: Required[DiscussionCategoryChangedPayloadChangesCategoryDict]


class IssuesOpenedPayloadChangesDict(TypedDict, total=False):
    """IssuesOpenedPayloadChanges."""

    old_issue: Required[Any | None]
    old_repository: Required[IssuesOpenedPayloadChangesOldRepositoryDict]


class PullRequestAssignedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestAssignedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestAssignedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeDisabledPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestAutoMergeDisabledPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestAutoMergeDisabledPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeDisabledPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestAutoMergeDisabledPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestAutoMergeDisabledPayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeEnabledPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestAutoMergeEnabledPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestAutoMergeEnabledPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeEnabledPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestAutoMergeEnabledPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestAutoMergeEnabledPayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestDequeuedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestDequeuedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestDequeuedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestDequeuedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestDequeuedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestDequeuedPayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the comment if the action was `edited`."""

    base: NotRequired[PullRequestEditedPayloadChangesBaseDict]
    body: NotRequired[PullRequestEditedPayloadChangesBodyDict]
    title: NotRequired[PullRequestEditedPayloadChangesTitleDict]


class PullRequestEnqueuedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestEnqueuedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestEnqueuedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestEnqueuedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestEnqueuedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestEnqueuedPayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestLabeledPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestLabeledPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestLabeledPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestLockedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestLockedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestLockedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestMinimalDict(TypedDict, total=False):
    """Pull Request Minimal."""

    id: Required[int]
    number: Required[int]
    url: Required[str]
    head: Required[PullRequestMinimalHeadDict]
    base: Required[PullRequestMinimalBaseDict]


class PullRequestReviewCommentCreatedPayloadCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    _links: Required[PullRequestReviewCommentCreatedPayloadCommentLinksDict]
    author_association: Required[
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
    ]
    body: Required[str]
    commit_id: Required[str]
    created_at: Required[str]
    diff_hunk: Required[str]
    html_url: Required[str]
    id: Required[int]
    in_reply_to_id: NotRequired[int]
    line: Required[None | int]
    node_id: Required[str]
    original_commit_id: Required[str]
    original_line: Required[None | int]
    original_position: Required[int]
    original_start_line: Required[None | int]
    path: Required[str]
    position: Required[None | int]
    pull_request_review_id: Required[None | int]
    pull_request_url: Required[str]
    reactions: Required[PullRequestReviewCommentCreatedPayloadCommentReactionsDict]
    side: Required[Literal["LEFT", "RIGHT"]]
    start_line: Required[None | int]
    start_side: Required[Literal["LEFT", "RIGHT"] | None]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentCreatedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewCommentCreatedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentDeletedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewCommentDeletedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewCommentDeletedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentEditedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewCommentEditedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewCommentEditedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewDismissedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewDismissedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewDismissedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewDismissedPayloadReviewDict(TypedDict, total=False):
    """The review that was affected."""

    _links: Required[PullRequestReviewDismissedPayloadReviewLinksDict]
    author_association: Required[
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
    ]
    body: Required[None | str]
    commit_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    node_id: Required[str]
    pull_request_url: Required[str]
    state: Required[Literal["dismissed", "approved", "changes_requested"]]
    submitted_at: Required[str]
    updated_at: NotRequired[None | str]
    user: Required[Any | None]


class PullRequestReviewEditedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewEditedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewEditedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewSubmittedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewSubmittedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewSubmittedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadResolvedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewThreadResolvedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadResolvedPayloadThreadCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    _links: Required[PullRequestReviewThreadResolvedPayloadThreadCommentLinksDict]
    author_association: Required[
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
    ]
    body: Required[str]
    commit_id: Required[str]
    created_at: Required[str]
    diff_hunk: Required[str]
    html_url: Required[str]
    id: Required[int]
    in_reply_to_id: NotRequired[int]
    line: Required[None | int]
    node_id: Required[str]
    original_commit_id: Required[str]
    original_line: Required[None | int]
    original_position: Required[int]
    original_start_line: Required[None | int]
    path: Required[str]
    position: Required[None | int]
    pull_request_review_id: Required[None | int]
    pull_request_url: Required[str]
    reactions: Required[PullRequestReviewThreadResolvedPayloadThreadCommentReactionsDict]
    side: Required[Literal["LEFT", "RIGHT"]]
    start_line: Required[None | int]
    start_side: Required[Literal["LEFT", "RIGHT"] | None]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadUnresolvedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadUnresolvedPayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadUnresolvedPayloadThreadCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    _links: Required[PullRequestReviewThreadUnresolvedPayloadThreadCommentLinksDict]
    author_association: Required[
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
    ]
    body: Required[str]
    commit_id: Required[str]
    created_at: Required[str]
    diff_hunk: Required[str]
    html_url: Required[str]
    id: Required[int]
    in_reply_to_id: NotRequired[int]
    line: Required[None | int]
    node_id: Required[str]
    original_commit_id: Required[str]
    original_line: Required[int]
    original_position: Required[int]
    original_start_line: Required[None | int]
    path: Required[str]
    position: Required[None | int]
    pull_request_review_id: Required[None | int]
    pull_request_url: Required[str]
    reactions: Required[PullRequestReviewThreadUnresolvedPayloadThreadCommentReactionsDict]
    side: Required[Literal["LEFT", "RIGHT"]]
    start_line: Required[None | int]
    start_side: Required[Literal["LEFT", "RIGHT"] | None]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestSynchronizePayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestSynchronizePayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestSynchronizePayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestSynchronizePayloadPullRequestHeadDict(TypedDict, total=False):
    """PullRequestSynchronizePayloadPullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestSynchronizePayloadPullRequestHeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnassignedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestUnassignedPayloadPullRequestBase."""

    label: Required[None | str]
    ref: Required[str]
    repo: Required[PullRequestUnassignedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnlabeledPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestUnlabeledPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestUnlabeledPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PullRequestUnlockedPayloadPullRequestBaseDict(TypedDict, total=False):
    """PullRequestUnlockedPayloadPullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[PullRequestUnlockedPayloadPullRequestBaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class PushPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `push` webhook."""

    after: Required[str]
    base_ref: Required[None | str]
    before: Required[str]
    commits: Required[list[PushPayloadCommitDict]]
    compare: Required[str]
    created: Required[bool]
    deleted: Required[bool]
    enterprise: NotRequired[EnterpriseDict]
    forced: Required[bool]
    head_commit: Required[Any | None]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pusher: Required[PushPayloadPusherDict]
    ref: Required[str]
    repository: Required[PushPayloadRepositoryDict]
    sender: NotRequired[UserDict]


class RepositoryRenamedPayloadChangesDict(TypedDict, total=False):
    """RepositoryRenamedPayloadChanges."""

    repository: Required[RepositoryRenamedPayloadChangesRepositoryDict]


class RepositoryRulesetEditedPayloadChangesConditionsUpdatedDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesConditionsUpdated."""

    condition: NotRequired[RepositoryRulesetConditionsDict]
    changes: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsUpdatedChangesDict]


RepositoryTransferredPayloadChangesOwnerDict = TypedDict(
    "RepositoryTransferredPayloadChangesOwnerDict",
    {
        "from": Required[RepositoryTransferredPayloadChangesOwnerFromDict],
    },
    total=False,
)
RepositoryTransferredPayloadChangesOwnerDict.__doc__ = """RepositoryTransferredPayloadChangesOwner."""


class SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryDict(TypedDict, total=False):
    """The details of the security advisory, including summary, description, and severity."""

    cvss: Required[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCvssDict]
    cvss_severities: NotRequired[Any | None]
    cwes: Required[list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryCweDict]]
    description: Required[str]
    ghsa_id: Required[str]
    identifiers: Required[list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryIdentifierDict]]
    published_at: Required[str]
    references: Required[list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryReferenceDict]]
    severity: Required[str]
    summary: Required[str]
    updated_at: Required[str]
    vulnerabilities: Required[list[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryVulnerabilityDict]]
    withdrawn_at: Required[str]


class StatusPayloadCommitDict(TypedDict, total=False):
    """StatusPayloadCommit."""

    author: Required[Any | None]
    comments_url: Required[str]
    commit: Required[StatusPayloadCommitCommitDict]
    committer: Required[Any | None]
    html_url: Required[str]
    node_id: Required[str]
    parents: Required[list[StatusPayloadCommitParentDict]]
    sha: Required[str]
    url: Required[str]


class TeamAddedToRepositoryPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `added_to_repository`."""

    action: Required[Literal["added_to_repository"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[TeamAddedToRepositoryPayloadRepositoryDict]
    sender: NotRequired[UserDict]
    team: Required[WebhooksTeam1Dict]


class TeamCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[TeamCreatedPayloadRepositoryDict]
    sender: Required[UserDict]
    team: Required[WebhooksTeam1Dict]


class TeamDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[TeamDeletedPayloadRepositoryDict]
    sender: NotRequired[UserDict]
    team: Required[WebhooksTeam1Dict]


class TeamEditedPayloadChangesRepositoryDict(TypedDict, total=False):
    """TeamEditedPayloadChangesRepository."""

    permissions: Required[TeamEditedPayloadChangesRepositoryPermissionsDict]


class TeamRemovedFromRepositoryPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `removed_from_repository`."""

    action: Required[Literal["removed_from_repository"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[TeamRemovedFromRepositoryPayloadRepositoryDict]
    sender: Required[UserDict]
    team: Required[WebhooksTeam1Dict]


class PackageUpdatedPayloadPackagePackageVersionDict(TypedDict, total=False):
    """PackageUpdatedPayloadPackagePackageVersion."""

    author: Required[Any | None]
    body: Required[str]
    body_html: Required[str]
    created_at: Required[str]
    description: Required[str]
    docker_metadata: NotRequired[list[PackageUpdatedPayloadPackagePackageVersionDockerMetadataDict]]
    draft: NotRequired[bool]
    html_url: Required[str]
    id: Required[int]
    installation_command: Required[str]
    manifest: NotRequired[str]
    metadata: Required[list[dict[str, Any]]]
    name: Required[str]
    package_files: Required[list[PackageUpdatedPayloadPackagePackageVersionPackageFileDict]]
    package_url: NotRequired[str]
    prerelease: NotRequired[bool]
    release: NotRequired[PackageUpdatedPayloadPackagePackageVersionReleaseDict]
    rubygems_metadata: NotRequired[list[WebhookRubygemsMetadataDict]]
    source_url: NotRequired[str]
    summary: Required[str]
    tag_name: NotRequired[str]
    target_commitish: Required[str]
    target_oid: Required[str]
    updated_at: Required[str]
    version: Required[str]


class RegistryPackageUpdatedPayloadRegistryPackagePackageVersionDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackagePackageVersion."""

    author: Required[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionAuthorDict]
    body: Required[str]
    body_html: Required[str]
    created_at: Required[str]
    description: Required[str]
    docker_metadata: NotRequired[list[Any | None]]
    draft: NotRequired[bool]
    html_url: Required[str]
    id: Required[int]
    installation_command: Required[str]
    manifest: NotRequired[str]
    metadata: Required[list[dict[str, Any]]]
    name: Required[str]
    package_files: Required[list[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionPackageFileDict]]
    package_url: Required[str]
    prerelease: NotRequired[bool]
    release: NotRequired[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionReleaseDict]
    rubygems_metadata: NotRequired[list[WebhookRubygemsMetadataDict]]
    summary: Required[str]
    tag_name: NotRequired[str]
    target_commitish: Required[str]
    target_oid: Required[str]
    updated_at: Required[str]
    version: Required[str]


class WebhooksChanges8Dict(TypedDict, total=False):
    """WebhooksChanges8."""

    tier: Required[WebhooksChanges8TierDict]


class WebhooksPullRequest5BaseDict(TypedDict, total=False):
    """WebhooksPullRequest5Base."""

    label: Required[str]
    ref: Required[str]
    repo: Required[WebhooksPullRequest5BaseRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class WebhooksPullRequest5HeadDict(TypedDict, total=False):
    """WebhooksPullRequest5Head."""

    label: Required[str]
    ref: Required[str]
    repo: Required[WebhooksPullRequest5HeadRepoDict]
    sha: Required[str]
    user: Required[Any | None]


class WebhooksReviewCommentDict(TypedDict, total=False):
    """The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself."""

    _links: Required[WebhooksReviewCommentLinksDict]
    author_association: Required[
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
    ]
    body: Required[str]
    commit_id: Required[str]
    created_at: Required[str]
    diff_hunk: Required[str]
    html_url: Required[str]
    id: Required[int]
    in_reply_to_id: NotRequired[int]
    line: Required[None | int]
    node_id: Required[str]
    original_commit_id: Required[str]
    original_line: Required[int]
    original_position: Required[int]
    original_start_line: Required[None | int]
    path: Required[str]
    position: Required[None | int]
    pull_request_review_id: Required[None | int]
    pull_request_url: Required[str]
    reactions: Required[WebhooksReviewCommentReactionsDict]
    side: Required[Literal["LEFT", "RIGHT"]]
    start_line: Required[None | int]
    start_side: Required[Literal["LEFT", "RIGHT"] | None]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class WebhooksReviewDict(TypedDict, total=False):
    """The review that was affected."""

    _links: Required[WebhooksReviewLinksDict]
    author_association: Required[
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
    ]
    body: Required[None | str]
    commit_id: Required[str]
    html_url: Required[str]
    id: Required[int]
    node_id: Required[str]
    pull_request_url: Required[str]
    state: Required[str]
    submitted_at: Required[None | str]
    updated_at: NotRequired[None | str]
    user: Required[Any | None]


class WebhooksSecurityAdvisoryDict(TypedDict, total=False):
    """The details of the security advisory, including summary, description, and severity."""

    cvss: Required[WebhooksSecurityAdvisoryCvssDict]
    cvss_severities: NotRequired[Any | None]
    cwes: Required[list[WebhooksSecurityAdvisoryCweDict]]
    description: Required[str]
    ghsa_id: Required[str]
    identifiers: Required[list[WebhooksSecurityAdvisoryIdentifierDict]]
    published_at: Required[str]
    references: Required[list[WebhooksSecurityAdvisoryReferenceDict]]
    severity: Required[str]
    summary: Required[str]
    updated_at: Required[str]
    vulnerabilities: Required[list[WebhooksSecurityAdvisoryVulnerabilityDict]]
    withdrawn_at: Required[None | str]


class WorkflowRunCompletedPayloadWorkflowRunDict(TypedDict, total=False):
    """Workflow Run."""

    actor: NotRequired[Any | None]
    artifacts_url: Required[str]
    cancel_url: Required[str]
    check_suite_id: Required[int]
    check_suite_node_id: Required[str]
    check_suite_url: Required[str]
    conclusion: Required[
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
    ]
    created_at: Required[str]
    event: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[WorkflowRunCompletedPayloadWorkflowRunHeadCommitDict]
    head_repository: Required[WorkflowRunCompletedPayloadWorkflowRunHeadRepositoryDict]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    jobs_url: Required[str]
    logs_url: Required[str]
    name: Required[None | str]
    node_id: Required[str]
    path: NotRequired[str]
    previous_attempt_url: Required[None | str]
    pull_requests: Required[list[Any | None]]
    referenced_workflows: NotRequired[Any | None]
    repository: Required[WorkflowRunCompletedPayloadWorkflowRunRepositoryDict]
    rerun_url: Required[str]
    run_attempt: Required[int]
    run_number: Required[int]
    run_started_at: Required[str]
    status: Required[Literal["requested", "in_progress", "completed", "queued", "pending", "waiting"]]
    triggering_actor: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    workflow_id: Required[int]
    workflow_url: Required[str]
    display_title: NotRequired[str]


class WorkflowRunInProgressPayloadWorkflowRunDict(TypedDict, total=False):
    """Workflow Run."""

    actor: NotRequired[Any | None]
    artifacts_url: Required[str]
    cancel_url: Required[str]
    check_suite_id: Required[int]
    check_suite_node_id: Required[str]
    check_suite_url: Required[str]
    conclusion: Required[
        Literal["action_required", "cancelled", "failure", "neutral", "skipped", "stale", "success", "timed_out"] | None
    ]
    created_at: Required[str]
    event: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[WorkflowRunInProgressPayloadWorkflowRunHeadCommitDict]
    head_repository: Required[WorkflowRunInProgressPayloadWorkflowRunHeadRepositoryDict]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    jobs_url: Required[str]
    logs_url: Required[str]
    name: Required[None | str]
    node_id: Required[str]
    path: NotRequired[str]
    previous_attempt_url: Required[None | str]
    pull_requests: Required[list[Any | None]]
    referenced_workflows: NotRequired[Any | None]
    repository: Required[WorkflowRunInProgressPayloadWorkflowRunRepositoryDict]
    rerun_url: Required[str]
    run_attempt: Required[int]
    run_number: Required[int]
    run_started_at: Required[str]
    status: Required[Literal["requested", "in_progress", "completed", "queued", "pending"]]
    triggering_actor: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    workflow_id: Required[int]
    workflow_url: Required[str]


class WorkflowRunRequestedPayloadWorkflowRunPullRequestDict(TypedDict, total=False):
    """WorkflowRunRequestedPayloadWorkflowRunPullRequest."""

    base: Required[WorkflowRunRequestedPayloadWorkflowRunPullRequestBaseDict]
    head: Required[WorkflowRunRequestedPayloadWorkflowRunPullRequestHeadDict]
    id: Required[float]
    number: Required[float]
    url: Required[str]


class DependabotAlertSecurityAdvisoryDict(TypedDict, total=False):
    """Details for the GitHub Security Advisory."""

    ghsa_id: Required[str]
    cve_id: Required[None | str]
    summary: Required[str]
    description: Required[str]
    vulnerabilities: Required[list[DependabotAlertSecurityVulnerabilityDict]]
    severity: Required[Literal["low", "medium", "high", "critical"]]
    cvss: Required[DependabotAlertSecurityAdvisoryCvssDict]
    cvss_severities: NotRequired[Any | None]
    epss: NotRequired[Any | None]
    cwes: Required[list[DependabotAlertSecurityAdvisoryCweDict]]
    identifiers: Required[list[DependabotAlertSecurityAdvisoryIdentifierDict]]
    references: Required[list[DependabotAlertSecurityAdvisoryReferenceDict]]
    published_at: Required[str]
    updated_at: Required[str]
    withdrawn_at: Required[None | str]


class ProjectsV2ItemEditedPayloadChangesOption1Dict(TypedDict, total=False):
    """ProjectsV2ItemEditedPayloadChangesOption1."""

    field_value: Required[ProjectsV2ItemEditedPayloadChangesOption1FieldValueDict]


class RepositoryRuleCodeScanningDict(TypedDict, total=False):
    """Choose which tools must provide code scanning results before the reference is updated. When configured, code scanning must be enabled and have results for both the commit and the reference being updated."""

    type: Required[Literal["code_scanning"]]
    parameters: NotRequired[RepositoryRuleCodeScanningParametersDict]


class RepositoryRulePullRequestParametersDict(TypedDict, total=False):
    """RepositoryRulePullRequestParameters."""

    allowed_merge_methods: NotRequired[list[Literal["merge", "squash", "rebase"]]]
    automatic_copilot_code_review_enabled: NotRequired[bool]
    dismiss_stale_reviews_on_push: Required[bool]
    require_code_owner_review: Required[bool]
    require_last_push_approval: Required[bool]
    required_approving_review_count: Required[int]
    required_review_thread_resolution: Required[bool]
    required_reviewers: NotRequired[list[RepositoryRuleParamsRequiredReviewerConfigurationDict]]


class RepositoryRuleRequiredStatusChecksDict(TypedDict, total=False):
    """Choose which status checks must pass before the ref is updated. When enabled, commits must first be pushed to another ref where the checks pass."""

    type: Required[Literal["required_status_checks"]]
    parameters: NotRequired[RepositoryRuleRequiredStatusChecksParametersDict]


class RepositoryRuleWorkflowsDict(TypedDict, total=False):
    """Require all changes made to a targeted branch to pass the specified workflows before they can be merged."""

    type: Required[Literal["workflows"]]
    parameters: NotRequired[RepositoryRuleWorkflowsParametersDict]


class PersonalAccessTokenRequestApprovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `personal_access_token_request` webhook with action `approved`."""

    action: Required[Literal["approved"]]
    personal_access_token_request: Required[PersonalAccessTokenRequestDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: Required[OrganizationDict]
    sender: Required[UserDict]
    installation: Required[InstallationDict]


class PersonalAccessTokenRequestCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `personal_access_token_request` webhook with action `cancelled`."""

    action: Required[Literal["cancelled"]]
    personal_access_token_request: Required[PersonalAccessTokenRequestDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: Required[OrganizationDict]
    sender: Required[UserDict]
    installation: Required[InstallationDict]


class PersonalAccessTokenRequestCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `personal_access_token_request` webhook with action `created`."""

    action: Required[Literal["created"]]
    personal_access_token_request: Required[PersonalAccessTokenRequestDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: Required[OrganizationDict]
    sender: Required[UserDict]
    installation: NotRequired[InstallationDict]


class PersonalAccessTokenRequestDeniedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `personal_access_token_request` webhook with action `denied`."""

    action: Required[Literal["denied"]]
    personal_access_token_request: Required[PersonalAccessTokenRequestDict]
    organization: Required[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    sender: Required[UserDict]
    installation: Required[InstallationDict]


class ProjectsV2ItemArchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `archived`."""

    action: Required[Literal["archived"]]
    changes: Required[WebhooksProjectChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2ItemConvertedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `converted`."""

    action: Required[Literal["converted"]]
    changes: Required[ProjectsV2ItemConvertedPayloadChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2ItemCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `created`."""

    action: Required[Literal["created"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2ItemDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2ItemReorderedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `reordered`."""

    action: Required[Literal["reordered"]]
    changes: Required[ProjectsV2ItemReorderedPayloadChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2ItemRestoredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `restored`."""

    action: Required[Literal["restored"]]
    changes: Required[WebhooksProjectChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class ProjectsV2Dict(TypedDict, total=False):
    """A projects v2 project."""

    id: Required[float]
    node_id: Required[str]
    owner: Required[UserDict]
    creator: Required[UserDict]
    title: Required[str]
    description: Required[None | str]
    public: Required[bool]
    closed_at: Required[None | str]
    created_at: Required[str]
    updated_at: Required[str]
    number: Required[int]
    short_description: Required[None | str]
    deleted_at: Required[None | str]
    deleted_by: Required[None | UserDict]
    state: NotRequired[Literal["open", "closed"]]
    latest_status_update: NotRequired[None | ProjectsV2StatusUpdateDict]
    is_template: NotRequired[bool]


class ProjectsV2StatusUpdateCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `created`."""

    action: Required[Literal["created"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_status_update: Required[ProjectsV2StatusUpdateDict]
    sender: Required[UserDict]


class ProjectsV2StatusUpdateDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_status_update: Required[ProjectsV2StatusUpdateDict]
    sender: Required[UserDict]


class ProjectsV2StatusUpdateEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_status_update` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[ProjectsV2StatusUpdateEditedPayloadChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_status_update: Required[ProjectsV2StatusUpdateDict]
    sender: Required[UserDict]


class PullRequestBaseDict(TypedDict, total=False):
    """PullRequestBase."""

    label: Required[str]
    ref: Required[str]
    repo: Required[RepositoryDict2]
    sha: Required[str]
    user: Required[UserDict]


class PullRequestHeadDict(TypedDict, total=False):
    """PullRequestHead."""

    label: Required[str]
    ref: Required[str]
    repo: Required[RepositoryDict2]
    sha: Required[str]
    user: Required[UserDict]


class FullRepositoryDict(TypedDict, total=False):
    """Full Repository."""

    id: Required[int]
    node_id: Required[str]
    name: Required[str]
    full_name: Required[str]
    owner: Required[UserDict]
    private: Required[bool]
    html_url: Required[str]
    description: Required[None | str]
    fork: Required[bool]
    url: Required[str]
    archive_url: Required[str]
    assignees_url: Required[str]
    blobs_url: Required[str]
    branches_url: Required[str]
    collaborators_url: Required[str]
    comments_url: Required[str]
    commits_url: Required[str]
    compare_url: Required[str]
    contents_url: Required[str]
    contributors_url: Required[str]
    deployments_url: Required[str]
    downloads_url: Required[str]
    events_url: Required[str]
    forks_url: Required[str]
    git_commits_url: Required[str]
    git_refs_url: Required[str]
    git_tags_url: Required[str]
    git_url: Required[str]
    issue_comment_url: Required[str]
    issue_events_url: Required[str]
    issues_url: Required[str]
    keys_url: Required[str]
    labels_url: Required[str]
    languages_url: Required[str]
    merges_url: Required[str]
    milestones_url: Required[str]
    notifications_url: Required[str]
    pulls_url: Required[str]
    releases_url: Required[str]
    ssh_url: Required[str]
    stargazers_url: Required[str]
    statuses_url: Required[str]
    subscribers_url: Required[str]
    subscription_url: Required[str]
    tags_url: Required[str]
    teams_url: Required[str]
    trees_url: Required[str]
    clone_url: Required[str]
    mirror_url: Required[None | str]
    hooks_url: Required[str]
    svn_url: Required[str]
    homepage: Required[None | str]
    language: Required[None | str]
    forks_count: Required[int]
    stargazers_count: Required[int]
    watchers_count: Required[int]
    size: Required[int]
    default_branch: Required[str]
    open_issues_count: Required[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: Required[bool]
    has_projects: Required[bool]
    has_wiki: Required[bool]
    has_pages: Required[bool]
    has_downloads: NotRequired[bool]
    has_discussions: Required[bool]
    archived: Required[bool]
    disabled: Required[bool]
    visibility: NotRequired[str]
    pushed_at: Required[str]
    created_at: Required[str]
    updated_at: Required[str]
    permissions: NotRequired[FullRepositoryPermissionsDict]
    allow_rebase_merge: NotRequired[bool]
    template_repository: NotRequired[None | RepositoryDict2]
    temp_clone_token: NotRequired[None | str]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    subscribers_count: Required[int]
    network_count: Required[int]
    license: Required[LicenseSimpleDict | None]
    organization: NotRequired[None | UserDict]
    parent: NotRequired[RepositoryDict2]
    source: NotRequired[RepositoryDict2]
    forks: Required[int]
    master_branch: NotRequired[str]
    open_issues: Required[int]
    watchers: Required[int]
    anonymous_access_enabled: NotRequired[bool]
    code_of_conduct: NotRequired[CodeOfConductSimpleDict]
    security_and_analysis: NotRequired[Any | None]
    custom_properties: NotRequired[dict[str, Any]]


class IssueDict(TypedDict, total=False):
    """Issues are a great way to keep track of tasks, enhancements, and bugs for your projects."""

    id: Required[int]
    node_id: Required[str]
    url: Required[str]
    repository_url: Required[str]
    labels_url: Required[str]
    comments_url: Required[str]
    events_url: Required[str]
    html_url: Required[str]
    number: Required[int]
    state: Required[str]
    state_reason: NotRequired[Literal["completed", "reopened", "not_planned", "duplicate"] | None]
    title: Required[str]
    body: NotRequired[None | str]
    user: Required[None | UserDict]
    labels: Required[list[IssueLabelOption2Dict | str]]
    assignee: Required[None | UserDict]
    assignees: NotRequired[Any | None]
    milestone: Required[MilestoneDict | None]
    locked: Required[bool]
    active_lock_reason: NotRequired[None | str]
    comments: Required[int]
    pull_request: NotRequired[IssuePullRequestDict]
    closed_at: Required[None | str]
    created_at: Required[str]
    updated_at: Required[str]
    draft: NotRequired[bool]
    closed_by: NotRequired[None | UserDict]
    body_html: NotRequired[str]
    body_text: NotRequired[str]
    timeline_url: NotRequired[str]
    type: NotRequired[Any | None]
    repository: NotRequired[RepositoryDict2]
    performed_via_github_app: NotRequired[Any | None]
    author_association: NotRequired[
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
    ]
    reactions: NotRequired[ReactionRollupDict]
    sub_issues_summary: NotRequired[SubIssuesSummaryDict]
    parent_issue_url: NotRequired[None | str]
    issue_dependencies_summary: NotRequired[IssueDependenciesSummaryDict]
    issue_field_values: NotRequired[list[IssueFieldValueDict]]


class DiscussionTransferredPayloadChangesDict(TypedDict, total=False):
    """DiscussionTransferredPayloadChanges."""

    new_discussion: Required[DiscussionDict]
    new_repository: Required[RepositoryDict]


class BranchProtectionConfigurationDisabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `disabled`."""

    action: Required[Literal["disabled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class BranchProtectionConfigurationEnabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_configuration` webhook with action `enabled`."""

    action: Required[Literal["enabled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class BranchProtectionRuleCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    rule: Required[WebhooksRuleDict]
    sender: Required[UserDict]


class BranchProtectionRuleDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    rule: Required[WebhooksRuleDict]
    sender: Required[UserDict]


class BranchProtectionRuleEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `branch_protection_rule` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[BranchProtectionRuleEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    rule: Required[WebhooksRuleDict]
    sender: Required[UserDict]


class CodeScanningAlertAppearedInBranchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `appeared_in_branch`."""

    action: Required[Literal["appeared_in_branch"]]
    alert: Required[CodeScanningAlertAppearedInBranchPayloadAlertDict]
    commit_oid: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CodeScanningAlertClosedByUserPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `closed_by_user`."""

    action: Required[Literal["closed_by_user"]]
    alert: Required[CodeScanningAlertClosedByUserPayloadAlertDict]
    commit_oid: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CodeScanningAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[CodeScanningAlertCreatedPayloadAlertDict]
    commit_oid: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CodeScanningAlertFixedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `fixed`."""

    action: Required[Literal["fixed"]]
    alert: Required[CodeScanningAlertFixedPayloadAlertDict]
    commit_oid: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CodeScanningAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[CodeScanningAlertReopenedPayloadAlertDict]
    commit_oid: Required[None | str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[None | str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CodeScanningAlertReopenedByUserPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `code_scanning_alert` webhook with action `reopened_by_user`."""

    action: Required[Literal["reopened_by_user"]]
    alert: Required[CodeScanningAlertReopenedByUserPayloadAlertDict]
    commit_oid: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CommitCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `commit_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[CommitCommentCreatedPayloadCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CreatePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `create` webhook."""

    description: Required[None | str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    master_branch: Required[str]
    organization: NotRequired[OrganizationDict]
    pusher_type: Required[str]
    ref: Required[str]
    ref_type: Required[Literal["tag", "branch"]]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CustomPropertyValuesUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `custom-property-values` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    repository: Required[RepositoryDict]
    organization: Required[OrganizationDict]
    sender: NotRequired[UserDict]
    new_property_values: Required[list[CustomPropertyValueDict]]
    old_property_values: Required[list[CustomPropertyValueDict]]


class DeletePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `delete` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pusher_type: Required[str]
    ref: Required[str]
    ref_type: Required[Literal["tag", "branch"]]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DeployKeyCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deploy_key` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    key: Required[WebhooksDeployKeyDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DeployKeyDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deploy_key` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    key: Required[WebhooksDeployKeyDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DeploymentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment` webhook with action `created`."""

    action: Required[Literal["created"]]
    deployment: Required[DeploymentCreatedPayloadDeploymentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: Required[Any | None]
    workflow_run: Required[Any | None]


class DeploymentReviewApprovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `approved`."""

    action: Required[Literal["approved"]]
    approver: NotRequired[WebhooksApproverDict]
    comment: NotRequired[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    reviewers: NotRequired[list[DeploymentReviewApprovedPayloadReviewerDict]]
    sender: Required[UserDict]
    since: Required[str]
    workflow_job_run: NotRequired[WebhooksWorkflowJobRunDict]
    workflow_job_runs: NotRequired[list[DeploymentReviewApprovedPayloadWorkflowJobRunDict]]
    workflow_run: Required[Any | None]


class DeploymentReviewRejectedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `rejected`."""

    action: Required[Literal["rejected"]]
    approver: NotRequired[WebhooksApproverDict]
    comment: NotRequired[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    reviewers: NotRequired[list[DeploymentReviewRejectedPayloadReviewerDict]]
    sender: Required[UserDict]
    since: Required[str]
    workflow_job_run: NotRequired[WebhooksWorkflowJobRunDict]
    workflow_job_runs: NotRequired[list[DeploymentReviewRejectedPayloadWorkflowJobRunDict]]
    workflow_run: Required[Any | None]


class DeploymentReviewRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_review` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    enterprise: NotRequired[EnterpriseDict]
    environment: Required[str]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    requestor: Required[Any | None]
    reviewers: Required[list[DeploymentReviewRequestedPayloadReviewerDict]]
    sender: Required[UserDict]
    since: Required[str]
    workflow_job_run: Required[DeploymentReviewRequestedPayloadWorkflowJobRunDict]
    workflow_run: Required[Any | None]


class DeploymentStatusCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_status` webhook with action `created`."""

    action: Required[Literal["created"]]
    check_run: NotRequired[Any | None]
    deployment: Required[DeploymentStatusCreatedPayloadDeploymentDict]
    deployment_status: Required[DeploymentStatusCreatedPayloadDeploymentStatusDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: NotRequired[Any | None]
    workflow_run: NotRequired[Any | None]


class DiscussionAnsweredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `answered`."""

    action: Required[Literal["answered"]]
    answer: Required[WebhooksAnswerDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[WebhooksCommentDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    comment: Required[WebhooksCommentDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion_comment` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[DiscussionCommentEditedPayloadChangesDict]
    comment: Required[WebhooksCommentDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `created`."""

    action: Required[Literal["created"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[DiscussionEditedPayloadChangesDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: Required[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionPinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `pinned`."""

    action: Required[Literal["pinned"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionUnansweredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unanswered`."""

    action: Required[Literal["unanswered"]]
    discussion: Required[DiscussionDict]
    old_answer: Required[WebhooksAnswerDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class DiscussionUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: Required[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DiscussionUnpinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `unpinned`."""

    action: Required[Literal["unpinned"]]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class ForkPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `fork` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    forkee: Required[Any]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class GollumPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `gollum` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pages: Required[list[GollumPayloadPageDict]]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class InstallationCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories: NotRequired[list[InstallationCreatedPayloadRepositoryDict]]
    repository: NotRequired[RepositoryDict]
    requester: NotRequired[Any | None]
    sender: Required[UserDict]


class InstallationDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories: NotRequired[list[InstallationDeletedPayloadRepositoryDict]]
    repository: NotRequired[RepositoryDict]
    requester: NotRequired[None]
    sender: Required[UserDict]


class InstallationNewPermissionsAcceptedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `new_permissions_accepted`."""

    action: Required[Literal["new_permissions_accepted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories: NotRequired[list[InstallationNewPermissionsAcceptedPayloadRepositoryDict]]
    repository: NotRequired[RepositoryDict]
    requester: NotRequired[None]
    sender: Required[UserDict]


class InstallationRepositoriesAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_repositories` webhook with action `added`."""

    action: Required[Literal["added"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories_added: Required[list[InstallationRepositoriesAddedPayloadRepositoriesAddedDict]]
    repositories_removed: Required[list[InstallationRepositoriesAddedPayloadRepositoriesRemovedDict]]
    repository: NotRequired[RepositoryDict]
    repository_selection: Required[Literal["all", "selected"]]
    requester: Required[Any | None]
    sender: Required[UserDict]


class InstallationRepositoriesRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_repositories` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories_added: Required[list[InstallationRepositoriesRemovedPayloadRepositoriesAddedDict]]
    repositories_removed: Required[list[InstallationRepositoriesRemovedPayloadRepositoriesRemovedDict]]
    repository: NotRequired[RepositoryDict]
    repository_selection: Required[Literal["all", "selected"]]
    requester: Required[Any | None]
    sender: Required[UserDict]


class InstallationSuspendPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `suspend`."""

    action: Required[Literal["suspend"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories: NotRequired[list[InstallationSuspendPayloadRepositoryDict]]
    repository: NotRequired[RepositoryDict]
    requester: NotRequired[None]
    sender: Required[UserDict]


class InstallationTargetRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation_target` webhook with action `renamed`."""

    account: Required[InstallationTargetRenamedPayloadAccountDict]
    action: Required[Literal["renamed"]]
    changes: Required[InstallationTargetRenamedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]
    target_type: Required[str]


class InstallationUnsuspendPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `installation` webhook with action `unsuspend`."""

    action: Required[Literal["unsuspend"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict2]
    organization: NotRequired[OrganizationDict]
    repositories: NotRequired[list[InstallationUnsuspendPayloadRepositoryDict]]
    repository: NotRequired[RepositoryDict]
    requester: NotRequired[None]
    sender: Required[UserDict]


class IssueCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[IssueCommentCreatedPayloadCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[Any]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssueCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    comment: Required[WebhooksIssueCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[Any]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssueCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue_comment` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[WebhooksChangesDict]
    comment: Required[WebhooksIssueCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[Any]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[Any]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class LabelCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: Required[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class LabelDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: Required[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class LabelEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `label` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[LabelEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: Required[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MarketplacePurchaseCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `cancelled`."""

    action: Required[Literal["cancelled"]]
    effective_date: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    marketplace_purchase: Required[WebhooksMarketplacePurchaseDict]
    organization: NotRequired[OrganizationDict]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class MarketplacePurchaseChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `changed`."""

    action: Required[Literal["changed"]]
    effective_date: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    marketplace_purchase: Required[WebhooksMarketplacePurchaseDict]
    organization: NotRequired[OrganizationDict]
    previous_marketplace_purchase: NotRequired[MarketplacePurchaseChangedPayloadPreviousMarketplacePurchaseDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class MarketplacePurchasePendingChangePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change`."""

    action: Required[Literal["pending_change"]]
    effective_date: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    marketplace_purchase: Required[WebhooksMarketplacePurchaseDict]
    organization: NotRequired[OrganizationDict]
    previous_marketplace_purchase: NotRequired[MarketplacePurchasePendingChangePayloadPreviousMarketplacePurchaseDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class MarketplacePurchasePendingChangeCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `pending_change_cancelled`."""

    action: Required[Literal["pending_change_cancelled"]]
    effective_date: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    marketplace_purchase: Required[MarketplacePurchasePendingChangeCancelledPayloadMarketplacePurchaseDict]
    organization: NotRequired[OrganizationDict]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class MarketplacePurchasePurchasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `marketplace_purchase` webhook with action `purchased`."""

    action: Required[Literal["purchased"]]
    effective_date: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    marketplace_purchase: Required[WebhooksMarketplacePurchaseDict]
    organization: NotRequired[OrganizationDict]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class MemberAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `added`."""

    action: Required[Literal["added"]]
    changes: NotRequired[MemberAddedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    member: Required[Any | None]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MemberEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[MemberEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    member: Required[Any | None]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MemberRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `member` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    member: Required[Any | None]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MembershipAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `membership` webhook with action `added`."""

    action: Required[Literal["added"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    member: Required[Any | None]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    scope: Required[Literal["team"]]
    sender: Required[Any | None]
    team: Required[WebhooksTeamDict]


class MembershipRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `membership` webhook with action `removed`."""

    action: Required[Literal["removed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    member: Required[Any | None]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    scope: Required[Literal["team", "organization"]]
    sender: Required[Any | None]
    team: Required[WebhooksTeamDict]


class MergeGroupChecksRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `merge_group` webhook with action `checks_requested`."""

    action: Required[Literal["checks_requested"]]
    installation: NotRequired[InstallationDict]
    merge_group: Required[MergeGroupDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class MergeGroupDestroyedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `merge_group` webhook with action `destroyed`."""

    action: Required[Literal["destroyed"]]
    reason: NotRequired[Literal["merged", "invalidated", "dequeued"]]
    installation: NotRequired[InstallationDict]
    merge_group: Required[MergeGroupDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class MetaDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `meta` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    hook: Required[MetaDeletedPayloadHookDict]
    hook_id: Required[int]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[None | RepositoryDict]
    sender: NotRequired[UserDict]


class MilestoneClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    installation: NotRequired[InstallationDict]
    milestone: Required[MilestoneClosedPayloadMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MilestoneCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    milestone: Required[MilestoneCreatedPayloadMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MilestoneDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    milestone: Required[WebhooksMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MilestoneEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[MilestoneEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    milestone: Required[WebhooksMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class MilestoneOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `milestone` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    installation: NotRequired[InstallationDict]
    milestone: Required[MilestoneOpenedPayloadMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class OrgBlockBlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `org_block` webhook with action `blocked`."""

    action: Required[Literal["blocked"]]
    blocked_user: Required[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class OrgBlockUnblockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `org_block` webhook with action `unblocked`."""

    action: Required[Literal["unblocked"]]
    blocked_user: Required[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class OrganizationDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    membership: NotRequired[WebhooksMembershipDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class OrganizationMemberAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_added`."""

    action: Required[Literal["member_added"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    membership: Required[WebhooksMembershipDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class OrganizationMemberInvitedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_invited`."""

    action: Required[Literal["member_invited"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    invitation: Required[OrganizationMemberInvitedPayloadInvitationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    user: NotRequired[Any | None]


class OrganizationMemberRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `member_removed`."""

    action: Required[Literal["member_removed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    membership: Required[WebhooksMembershipDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class OrganizationRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `organization` webhook with action `renamed`."""

    action: Required[Literal["renamed"]]
    changes: NotRequired[OrganizationRenamedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    membership: NotRequired[WebhooksMembershipDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class PackagePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `package` webhook with action `published`."""

    action: Required[Literal["published"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    package: Required[PackagePublishedPayloadPackageDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class PageBuildPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `page_build` webhook."""

    build: Required[PageBuildPayloadBuildDict]
    enterprise: NotRequired[EnterpriseDict]
    id: Required[int]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PingPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `ping` webhook."""

    hook: NotRequired[PingPayloadHookDict]
    hook_id: NotRequired[int]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]
    zen: NotRequired[str]


class ProjectCardConvertedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `converted`."""

    action: Required[Literal["converted"]]
    changes: Required[ProjectCardConvertedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_card: Required[WebhooksProjectCardDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectCardCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_card: Required[WebhooksProjectCardDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectCardDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_card: Required[ProjectCardDeletedPayloadProjectCardDict]
    repository: NotRequired[None | RepositoryDict]
    sender: Required[UserDict]


class ProjectCardEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[ProjectCardEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_card: Required[WebhooksProjectCardDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectCardMovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_card` webhook with action `moved`."""

    action: Required[Literal["moved"]]
    changes: NotRequired[ProjectCardMovedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_card: Required[Any]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project: Required[WebhooksProjectDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectColumnCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_column: Required[WebhooksProjectColumnDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class ProjectColumnDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_column: Required[WebhooksProjectColumnDict]
    repository: NotRequired[None | RepositoryDict]
    sender: NotRequired[UserDict]


class ProjectColumnEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[ProjectColumnEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_column: Required[WebhooksProjectColumnDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class ProjectColumnMovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project_column` webhook with action `moved`."""

    action: Required[Literal["moved"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project_column: Required[WebhooksProjectColumnDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project: Required[WebhooksProjectDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ProjectDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project: Required[WebhooksProjectDict]
    repository: NotRequired[None | RepositoryDict]
    sender: NotRequired[UserDict]


class ProjectEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[ProjectEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project: Required[WebhooksProjectDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class ProjectReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `project` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    project: Required[WebhooksProjectDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class PublicPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `public` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestConvertedToDraftPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `converted_to_draft`."""

    action: Required[Literal["converted_to_draft"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestReadyForReviewPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `ready_for_review`."""

    action: Required[Literal["ready_for_review"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RegistryPackagePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `registry_package` webhook with action `published`."""

    action: Required[Literal["published"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    registry_package: Required[RegistryPackagePublishedPayloadRegistryPackageDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class ReleaseCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksReleaseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class ReleaseDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksReleaseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class ReleaseEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[ReleaseEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksReleaseDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class ReleasePrereleasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `prereleased`."""

    action: Required[Literal["prereleased"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[ReleasePrereleasedPayloadReleaseDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class ReleasePublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `published`."""

    action: Required[Literal["published"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksRelease1Dict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class ReleaseReleasedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `released`."""

    action: Required[Literal["released"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksReleaseDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class ReleaseUnpublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `release` webhook with action `unpublished`."""

    action: Required[Literal["unpublished"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    release: Required[WebhooksRelease1Dict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class RepositoryAdvisoryPublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_advisory` webhook with action `published`."""

    action: Required[Literal["published"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    repository_advisory: Required[RepositoryAdvisoryDict]
    sender: NotRequired[UserDict]


class RepositoryAdvisoryReportedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_advisory` webhook with action `reported`."""

    action: Required[Literal["reported"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    repository_advisory: Required[RepositoryAdvisoryDict]
    sender: NotRequired[UserDict]


class RepositoryArchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `archived`."""

    action: Required[Literal["archived"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryDispatchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_dispatch` webhook."""

    action: Required[str]
    branch: Required[str]
    client_payload: Required[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: Required[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[RepositoryEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryImportPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_import` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    status: Required[Literal["success", "cancelled", "failure"]]


class RepositoryPrivatizedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `privatized`."""

    action: Required[Literal["privatized"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryPublicizedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `publicized`."""

    action: Required[Literal["publicized"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryUnarchivedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `unarchived`."""

    action: Required[Literal["unarchived"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryVulnerabilityAlertCreatePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `create`."""

    action: Required[Literal["create"]]
    alert: Required[WebhooksAlertDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryVulnerabilityAlertDismissPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `dismiss`."""

    action: Required[Literal["dismiss"]]
    alert: Required[RepositoryVulnerabilityAlertDismissPayloadAlertDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryVulnerabilityAlertReopenPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `reopen`."""

    action: Required[Literal["reopen"]]
    alert: Required[WebhooksAlertDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryVulnerabilityAlertResolvePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_vulnerability_alert` webhook with action `resolve`."""

    action: Required[Literal["resolve"]]
    alert: Required[RepositoryVulnerabilityAlertResolvePayloadAlertDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class SecretScanningScanCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_scan` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    type: Required[Literal["backfill", "custom-pattern-backfill", "pattern-version-backfill"]]
    source: Required[Literal["git", "issues", "pull-requests", "discussions", "wiki"]]
    started_at: Required[str]
    completed_at: Required[str]
    secret_types: NotRequired[Any | None]
    custom_pattern_name: NotRequired[None | str]
    custom_pattern_scope: NotRequired[Literal["repository", "organization", "enterprise"] | None]
    repository: NotRequired[RepositoryDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    sender: NotRequired[UserDict]


class SponsorshipCancelledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `cancelled`."""

    action: Required[Literal["cancelled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class SponsorshipCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class SponsorshipEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[SponsorshipEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class SponsorshipPendingCancellationPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `pending_cancellation`."""

    action: Required[Literal["pending_cancellation"]]
    effective_date: NotRequired[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class StarCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `star` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    starred_at: Required[None | str]


class StarDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `star` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    starred_at: Required[None]


class TeamAddPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team_add` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    team: Required[WebhooksTeam1Dict]


class WatchStartedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `watch` webhook with action `started`."""

    action: Required[Literal["started"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class WorkflowDispatchPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_dispatch` webhook."""

    enterprise: NotRequired[EnterpriseDict]
    inputs: Required[Any | None]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    ref: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: Required[str]


class WorkflowJobCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow_job: Required[Any]
    deployment: NotRequired[DeploymentDict]


class WorkflowJobInProgressPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `in_progress`."""

    action: Required[Literal["in_progress"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow_job: Required[Any]
    deployment: NotRequired[DeploymentDict]


class WorkflowJobQueuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `queued`."""

    action: Required[Literal["queued"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow_job: Required[WorkflowJobQueuedPayloadWorkflowJobDict]
    deployment: NotRequired[DeploymentDict]


class WorkflowJobWaitingPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_job` webhook with action `waiting`."""

    action: Required[Literal["waiting"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow_job: Required[WorkflowJobWaitingPayloadWorkflowJobDict]
    deployment: NotRequired[DeploymentDict]


class SecretScanningAlertAssignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `assigned`."""

    action: Required[Literal["assigned"]]
    alert: Required[SecretScanningAlertWebhookDict]
    assignee: NotRequired[UserDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[SecretScanningAlertWebhookDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertLocationCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert_location` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[SecretScanningAlertWebhookDict]
    installation: NotRequired[InstallationDict]
    location: Required[SecretScanningLocationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class SecretScanningAlertPubliclyLeakedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `publicly_leaked`."""

    action: Required[Literal["publicly_leaked"]]
    alert: Required[SecretScanningAlertWebhookDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[SecretScanningAlertWebhookDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertResolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `resolved`."""

    action: Required[Literal["resolved"]]
    alert: Required[SecretScanningAlertWebhookDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertUnassignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `unassigned`."""

    action: Required[Literal["unassigned"]]
    alert: Required[SecretScanningAlertWebhookDict]
    assignee: NotRequired[UserDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class SecretScanningAlertValidatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `secret_scanning_alert` webhook with action `validated`."""

    action: Required[Literal["validated"]]
    alert: Required[SecretScanningAlertWebhookDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class IssuesDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesDeletedPayloadIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesDemilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `demilestoned`."""

    action: Required[Literal["demilestoned"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesDemilestonedPayloadIssueDict]
    milestone: NotRequired[WebhooksMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[IssuesEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesEditedPayloadIssueDict]
    label: NotRequired[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesLabeledPayloadIssueDict]
    label: NotRequired[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesLockedPayloadIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesMilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `milestoned`."""

    action: Required[Literal["milestoned"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesMilestonedPayloadIssueDict]
    milestone: Required[WebhooksMilestoneDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesReopenedPayloadIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesTransferredPayloadChangesDict(TypedDict, total=False):
    """IssuesTransferredPayloadChanges."""

    new_issue: Required[IssuesTransferredPayloadChangesNewIssueDict]
    new_repository: Required[IssuesTransferredPayloadChangesNewRepositoryDict]


class IssuesUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesUnlockedPayloadIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesAssignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `assigned`."""

    action: Required[Literal["assigned"]]
    assignee: NotRequired[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesTypedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `typed`."""

    action: Required[Literal["typed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssueDict]
    type: Required[Any | None]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesUnassignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unassigned`."""

    action: Required[Literal["unassigned"]]
    assignee: NotRequired[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssueDict]
    label: NotRequired[WebhooksLabelDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesUntypedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `untyped`."""

    action: Required[Literal["untyped"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssueDict]
    type: Required[Any | None]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesPinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `pinned`."""

    action: Required[Literal["pinned"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssue2Dict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesUnpinnedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `unpinned`."""

    action: Required[Literal["unpinned"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssue2Dict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckSuiteCompletedPayloadCheckSuiteDict(TypedDict, total=False):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    after: Required[None | str]
    app: Required[CheckSuiteCompletedPayloadCheckSuiteAppDict]
    before: Required[None | str]
    check_runs_url: Required[str]
    conclusion: Required[
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
    ]
    created_at: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[CheckSuiteCompletedPayloadCheckSuiteHeadCommitDict]
    head_sha: Required[str]
    id: Required[int]
    latest_check_runs_count: Required[int]
    node_id: Required[str]
    pull_requests: Required[list[CheckSuiteCompletedPayloadCheckSuitePullRequestDict]]
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]
    status: Required[Literal["requested", "in_progress", "completed", "queued", "pending"] | None]
    updated_at: Required[str]
    url: Required[str]


class CheckSuiteRequestedPayloadCheckSuiteDict(TypedDict, total=False):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    after: Required[None | str]
    app: Required[CheckSuiteRequestedPayloadCheckSuiteAppDict]
    before: Required[None | str]
    check_runs_url: Required[str]
    conclusion: Required[
        Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale", "skipped"] | None
    ]
    created_at: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[CheckSuiteRequestedPayloadCheckSuiteHeadCommitDict]
    head_sha: Required[str]
    id: Required[int]
    latest_check_runs_count: Required[int]
    node_id: Required[str]
    pull_requests: Required[list[CheckSuiteRequestedPayloadCheckSuitePullRequestDict]]
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]
    status: Required[Literal["requested", "in_progress", "completed", "queued"] | None]
    updated_at: Required[str]
    url: Required[str]


class CheckSuiteRerequestedPayloadCheckSuiteDict(TypedDict, total=False):
    """The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite)."""

    after: Required[None | str]
    app: Required[CheckSuiteRerequestedPayloadCheckSuiteAppDict]
    before: Required[None | str]
    check_runs_url: Required[str]
    conclusion: Required[
        Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale"] | None
    ]
    created_at: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[CheckSuiteRerequestedPayloadCheckSuiteHeadCommitDict]
    head_sha: Required[str]
    id: Required[int]
    latest_check_runs_count: Required[int]
    node_id: Required[str]
    pull_requests: Required[list[CheckSuiteRerequestedPayloadCheckSuitePullRequestDict]]
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]
    status: Required[Literal["requested", "in_progress", "completed", "queued"] | None]
    updated_at: Required[str]
    url: Required[str]


class DiscussionCategoryChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `category_changed`."""

    action: Required[Literal["category_changed"]]
    changes: Required[DiscussionCategoryChangedPayloadChangesDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesOpenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `opened`."""

    action: Required[Literal["opened"]]
    changes: NotRequired[IssuesOpenedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[IssuesOpenedPayloadIssueDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestAssignedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestAssignedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestAssignedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestAssignedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestAssignedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestAssignedPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestAssignedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeDisabledPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestAutoMergeDisabledPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestAutoMergeDisabledPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestAutoMergeDisabledPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestAutoMergeDisabledPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[
        list[Any | None | PullRequestAutoMergeDisabledPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestAutoMergeDisabledPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestAutoMergeEnabledPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestAutoMergeEnabledPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestAutoMergeEnabledPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestAutoMergeEnabledPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestAutoMergeEnabledPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[
        list[Any | None | PullRequestAutoMergeEnabledPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestAutoMergeEnabledPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestDequeuedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestDequeuedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestDequeuedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestDequeuedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestDequeuedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestDequeuedPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestDequeuedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[PullRequestEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[Any]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class PullRequestEnqueuedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestEnqueuedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestEnqueuedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestEnqueuedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestEnqueuedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestEnqueuedPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestEnqueuedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestLabeledPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestLabeledPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestLabeledPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestLabeledPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestLabeledPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestLabeledPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestLabeledPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestLockedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestLockedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestLockedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestLockedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestLockedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestLockedPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestLockedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class SimpleCheckSuiteDict(TypedDict, total=False):
    """A suite of checks performed on the code of a given code change."""

    after: NotRequired[None | str]
    app: NotRequired[Any | None]
    before: NotRequired[None | str]
    conclusion: NotRequired[
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
    ]
    created_at: NotRequired[str]
    head_branch: NotRequired[None | str]
    head_sha: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    pull_requests: NotRequired[list[PullRequestMinimalDict]]
    repository: NotRequired[MinimalRepositoryDict]
    status: NotRequired[Literal["queued", "in_progress", "completed", "pending", "waiting"]]
    updated_at: NotRequired[str]
    url: NotRequired[str]


class PullRequestReviewCommentCreatedPayloadPullRequestDict(TypedDict, total=False):
    """PullRequestReviewCommentCreatedPayloadPullRequest."""

    _links: Required[PullRequestReviewCommentCreatedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: NotRequired[Any | None]
    base: Required[PullRequestReviewCommentCreatedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: NotRequired[bool]
    head: Required[PullRequestReviewCommentCreatedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewCommentCreatedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewCommentCreatedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewCommentCreatedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentDeletedPayloadPullRequestDict(TypedDict, total=False):
    """PullRequestReviewCommentDeletedPayloadPullRequest."""

    _links: Required[PullRequestReviewCommentDeletedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: NotRequired[Any | None]
    base: Required[PullRequestReviewCommentDeletedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: NotRequired[bool]
    head: Required[PullRequestReviewCommentDeletedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewCommentDeletedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewCommentDeletedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewCommentDeletedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewCommentEditedPayloadPullRequestDict(TypedDict, total=False):
    """PullRequestReviewCommentEditedPayloadPullRequest."""

    _links: Required[PullRequestReviewCommentEditedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: NotRequired[Any | None]
    base: Required[PullRequestReviewCommentEditedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: NotRequired[bool]
    head: Required[PullRequestReviewCommentEditedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewCommentEditedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewCommentEditedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewCommentEditedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewDismissedPayloadPullRequestDict(TypedDict, total=False):
    """Simple Pull Request."""

    _links: Required[PullRequestReviewDismissedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestReviewDismissedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestReviewDismissedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewDismissedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewDismissedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewDismissedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewEditedPayloadPullRequestDict(TypedDict, total=False):
    """Simple Pull Request."""

    _links: Required[PullRequestReviewEditedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestReviewEditedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestReviewEditedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewEditedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewEditedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewEditedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewSubmittedPayloadPullRequestDict(TypedDict, total=False):
    """Simple Pull Request."""

    _links: Required[PullRequestReviewSubmittedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestReviewSubmittedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestReviewSubmittedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewSubmittedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewSubmittedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewSubmittedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadResolvedPayloadPullRequestDict(TypedDict, total=False):
    """Simple Pull Request."""

    _links: Required[PullRequestReviewThreadResolvedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestReviewThreadResolvedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestReviewThreadResolvedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewThreadResolvedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewThreadResolvedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewThreadResolvedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadResolvedPayloadThreadDict(TypedDict, total=False):
    """PullRequestReviewThreadResolvedPayloadThread."""

    comments: Required[list[PullRequestReviewThreadResolvedPayloadThreadCommentDict]]
    node_id: Required[str]


class PullRequestReviewThreadUnresolvedPayloadPullRequestDict(TypedDict, total=False):
    """Simple Pull Request."""

    _links: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestBaseDict]
    body: Required[None | str]
    closed_at: Required[None | str]
    comments_url: Required[str]
    commits_url: Required[str]
    created_at: Required[str]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestReviewThreadUnresolvedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    merge_commit_sha: Required[None | str]
    merged_at: Required[None | str]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    requested_reviewers: Required[
        list[Any | None | PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestReviewThreadUnresolvedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestReviewThreadUnresolvedPayloadThreadDict(TypedDict, total=False):
    """PullRequestReviewThreadUnresolvedPayloadThread."""

    comments: Required[list[PullRequestReviewThreadUnresolvedPayloadThreadCommentDict]]
    node_id: Required[str]


class PullRequestSynchronizePayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestSynchronizePayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestSynchronizePayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestSynchronizePayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestSynchronizePayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[
        list[Any | None | PullRequestSynchronizePayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestSynchronizePayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestUnassignedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestUnassignedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestUnassignedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestUnassignedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestUnassignedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[
        list[Any | None | PullRequestUnassignedPayloadPullRequestRequestedReviewerOption2Dict]
    ]
    requested_teams: Required[list[PullRequestUnassignedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestUnlabeledPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestUnlabeledPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestUnlabeledPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestUnlabeledPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestUnlabeledPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestUnlabeledPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestUnlabeledPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class PullRequestUnlockedPayloadPullRequestDict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[PullRequestUnlockedPayloadPullRequestLinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[PullRequestUnlockedPayloadPullRequestBaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[PullRequestUnlockedPayloadPullRequestHeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[PullRequestUnlockedPayloadPullRequestLabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | PullRequestUnlockedPayloadPullRequestRequestedReviewerOption2Dict]]
    requested_teams: Required[list[PullRequestUnlockedPayloadPullRequestRequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class RepositoryRenamedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `renamed`."""

    action: Required[Literal["renamed"]]
    changes: Required[RepositoryRenamedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryRulesetEditedPayloadChangesConditionsDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesConditions."""

    added: NotRequired[list[RepositoryRulesetConditionsDict]]
    deleted: NotRequired[list[RepositoryRulesetConditionsDict]]
    updated: NotRequired[list[RepositoryRulesetEditedPayloadChangesConditionsUpdatedDict]]


class RepositoryTransferredPayloadChangesDict(TypedDict, total=False):
    """RepositoryTransferredPayloadChanges."""

    owner: Required[RepositoryTransferredPayloadChangesOwnerDict]


class SecurityAdvisoryWithdrawnPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `withdrawn`."""

    action: Required[Literal["withdrawn"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    security_advisory: Required[SecurityAdvisoryWithdrawnPayloadSecurityAdvisoryDict]
    sender: NotRequired[UserDict]


class StatusPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `status` webhook."""

    avatar_url: NotRequired[None | str]
    branches: Required[list[StatusPayloadBrancheDict]]
    commit: Required[StatusPayloadCommitDict]
    context: Required[str]
    created_at: Required[str]
    description: Required[None | str]
    enterprise: NotRequired[EnterpriseDict]
    id: Required[int]
    installation: NotRequired[InstallationDict]
    name: Required[str]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    sha: Required[str]
    state: Required[Literal["pending", "success", "failure", "error"]]
    target_url: Required[None | str]
    updated_at: Required[str]


class TeamEditedPayloadChangesDict(TypedDict, total=False):
    """The changes to the team if the action was `edited`."""

    description: NotRequired[TeamEditedPayloadChangesDescriptionDict]
    name: NotRequired[TeamEditedPayloadChangesNameDict]
    privacy: NotRequired[TeamEditedPayloadChangesPrivacyDict]
    notification_setting: NotRequired[TeamEditedPayloadChangesNotificationSettingDict]
    repository: NotRequired[TeamEditedPayloadChangesRepositoryDict]


class PackageUpdatedPayloadPackageDict(TypedDict, total=False):
    """Information about the package."""

    created_at: Required[str]
    description: Required[None | str]
    ecosystem: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    namespace: Required[str]
    owner: Required[Any | None]
    package_type: Required[str]
    package_version: Required[PackageUpdatedPayloadPackagePackageVersionDict]
    registry: Required[Any | None]
    updated_at: Required[str]


class RegistryPackageUpdatedPayloadRegistryPackageDict(TypedDict, total=False):
    """RegistryPackageUpdatedPayloadRegistryPackage."""

    created_at: Required[str]
    description: Required[None]
    ecosystem: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    namespace: Required[str]
    owner: Required[RegistryPackageUpdatedPayloadRegistryPackageOwnerDict]
    package_type: Required[str]
    package_version: Required[RegistryPackageUpdatedPayloadRegistryPackagePackageVersionDict]
    registry: Required[Any | None]
    updated_at: Required[str]


class SponsorshipPendingTierChangePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `pending_tier_change`."""

    action: Required[Literal["pending_tier_change"]]
    changes: Required[WebhooksChanges8Dict]
    effective_date: NotRequired[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class SponsorshipTierChangedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sponsorship` webhook with action `tier_changed`."""

    action: Required[Literal["tier_changed"]]
    changes: Required[WebhooksChanges8Dict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]
    sponsorship: Required[WebhooksSponsorshipDict]


class WebhooksPullRequest5Dict(TypedDict, total=False):
    """Pull Request."""

    _links: Required[WebhooksPullRequest5LinksDict]
    active_lock_reason: Required[Literal["resolved", "off-topic", "too heated", "spam"] | None]
    additions: NotRequired[int]
    assignee: Required[Any | None]
    assignees: Required[list[Any | None]]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    base: Required[WebhooksPullRequest5BaseDict]
    body: Required[None | str]
    changed_files: NotRequired[int]
    closed_at: Required[None | str]
    comments: NotRequired[int]
    comments_url: Required[str]
    commits: NotRequired[int]
    commits_url: Required[str]
    created_at: Required[str]
    deletions: NotRequired[int]
    diff_url: Required[str]
    draft: Required[bool]
    head: Required[WebhooksPullRequest5HeadDict]
    html_url: Required[str]
    id: Required[int]
    issue_url: Required[str]
    labels: Required[list[WebhooksPullRequest5LabelDict]]
    locked: Required[bool]
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Required[None | str]
    mergeable: NotRequired[None | bool]
    mergeable_state: NotRequired[str]
    merged: NotRequired[None | bool]
    merged_at: Required[None | str]
    merged_by: NotRequired[Any | None]
    milestone: Required[Any | None]
    node_id: Required[str]
    number: Required[int]
    patch_url: Required[str]
    rebaseable: NotRequired[None | bool]
    requested_reviewers: Required[list[Any | None | WebhooksPullRequest5RequestedReviewerOption2Dict]]
    requested_teams: Required[list[WebhooksPullRequest5RequestedTeamDict]]
    review_comment_url: Required[str]
    review_comments: NotRequired[int]
    review_comments_url: Required[str]
    state: Required[Literal["open", "closed"]]
    statuses_url: Required[str]
    title: Required[str]
    updated_at: Required[str]
    url: Required[str]
    user: Required[Any | None]


class SecurityAdvisoryPublishedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `published`."""

    action: Required[Literal["published"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    security_advisory: Required[WebhooksSecurityAdvisoryDict]
    sender: NotRequired[UserDict]


class SecurityAdvisoryUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_advisory` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    security_advisory: Required[WebhooksSecurityAdvisoryDict]
    sender: NotRequired[UserDict]


class WorkflowRunCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: Required[Any | None]
    workflow_run: Required[WorkflowRunCompletedPayloadWorkflowRunDict]


class WorkflowRunInProgressPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `in_progress`."""

    action: Required[Literal["in_progress"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: Required[Any | None]
    workflow_run: Required[WorkflowRunInProgressPayloadWorkflowRunDict]


class WorkflowRunRequestedPayloadWorkflowRunDict(TypedDict, total=False):
    """Workflow Run."""

    actor: NotRequired[Any | None]
    artifacts_url: Required[str]
    cancel_url: Required[str]
    check_suite_id: Required[int]
    check_suite_node_id: Required[str]
    check_suite_url: Required[str]
    conclusion: Required[
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
    ]
    created_at: Required[str]
    event: Required[str]
    head_branch: Required[None | str]
    head_commit: Required[WorkflowRunRequestedPayloadWorkflowRunHeadCommitDict]
    head_repository: Required[WorkflowRunRequestedPayloadWorkflowRunHeadRepositoryDict]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    jobs_url: Required[str]
    logs_url: Required[str]
    name: Required[None | str]
    node_id: Required[str]
    path: NotRequired[str]
    previous_attempt_url: Required[None | str]
    pull_requests: Required[list[WorkflowRunRequestedPayloadWorkflowRunPullRequestDict]]
    referenced_workflows: NotRequired[Any | None]
    repository: Required[WorkflowRunRequestedPayloadWorkflowRunRepositoryDict]
    rerun_url: Required[str]
    run_attempt: Required[int]
    run_number: Required[int]
    run_started_at: Required[str]
    status: Required[Literal["requested", "in_progress", "completed", "queued", "pending", "waiting"]]
    triggering_actor: NotRequired[Any | None]
    updated_at: Required[str]
    url: Required[str]
    workflow_id: Required[int]
    workflow_url: Required[str]
    display_title: Required[str]


class DependabotAlertDict(TypedDict, total=False):
    """A Dependabot alert."""

    number: Required[int]
    state: Required[Literal["auto_dismissed", "dismissed", "fixed", "open"]]
    dependency: Required[DependabotAlertDependencyDict]
    security_advisory: Required[DependabotAlertSecurityAdvisoryDict]
    security_vulnerability: Required[DependabotAlertSecurityVulnerabilityDict]
    url: Required[str]
    html_url: Required[str]
    created_at: Required[str]
    updated_at: Required[str]
    dismissed_at: Required[None | str]
    dismissed_by: Required[None | UserDict]
    dismissed_reason: Required[
        Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"] | None
    ]
    dismissed_comment: Required[None | str]
    fixed_at: Required[None | str]
    auto_dismissed_at: NotRequired[None | str]


class ProjectsV2ItemEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2_item` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: NotRequired[ProjectsV2ItemEditedPayloadChangesOption1Dict | ProjectsV2ItemEditedPayloadChangesOption2Dict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2_item: Required[ProjectsV2ItemDict]
    sender: Required[UserDict]


class RepositoryRulePullRequestDict(TypedDict, total=False):
    """Require all commits be made to a non-target branch and submitted via a pull request before they can be merged."""

    type: Required[Literal["pull_request"]]
    parameters: NotRequired[RepositoryRulePullRequestParametersDict]


class ProjectsV2ClosedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2` webhook with action `closed`."""

    action: Required[Literal["closed"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2: Required[ProjectsV2Dict]
    sender: Required[UserDict]


class ProjectsV2CreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2` webhook with action `created`."""

    action: Required[Literal["created"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2: Required[ProjectsV2Dict]
    sender: Required[UserDict]


class ProjectsV2DeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2: Required[ProjectsV2Dict]
    sender: Required[UserDict]


class ProjectsV2EditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[ProjectsV2EditedPayloadChangesDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2: Required[ProjectsV2Dict]
    sender: Required[UserDict]


class ProjectsV2ReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `projects_v2` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    projects_v2: Required[ProjectsV2Dict]
    sender: Required[UserDict]


class PullRequestDict(TypedDict, total=False):
    """Pull requests let you tell others about changes you've pushed to a repository on GitHub. Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary."""

    url: Required[str]
    id: Required[int]
    node_id: Required[str]
    html_url: Required[str]
    diff_url: Required[str]
    patch_url: Required[str]
    issue_url: Required[str]
    commits_url: Required[str]
    review_comments_url: Required[str]
    review_comment_url: Required[str]
    comments_url: Required[str]
    statuses_url: Required[str]
    number: Required[int]
    state: Required[Literal["open", "closed"]]
    locked: Required[bool]
    title: Required[str]
    user: Required[UserDict]
    body: Required[None | str]
    labels: Required[list[PullRequestLabelDict]]
    milestone: Required[MilestoneDict | None]
    active_lock_reason: NotRequired[None | str]
    created_at: Required[str]
    updated_at: Required[str]
    closed_at: Required[None | str]
    merged_at: Required[None | str]
    merge_commit_sha: Required[None | str]
    assignee: Required[None | UserDict]
    assignees: NotRequired[Any | None]
    requested_reviewers: NotRequired[Any | None]
    requested_teams: NotRequired[Any | None]
    head: Required[PullRequestHeadDict]
    base: Required[PullRequestBaseDict]
    _links: Required[PullRequestLinksDict]
    author_association: Required[
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
    ]
    auto_merge: Required[Any | None]
    draft: NotRequired[bool]
    merged: Required[bool]
    mergeable: Required[None | bool]
    rebaseable: NotRequired[None | bool]
    mergeable_state: Required[str]
    merged_by: Required[None | UserDict]
    comments: Required[int]
    review_comments: Required[int]
    maintainer_can_modify: Required[bool]
    commits: Required[int]
    additions: Required[int]
    deletions: Required[int]
    changed_files: Required[int]


class SecurityAndAnalysisPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `security_and_analysis` webhook."""

    changes: Required[SecurityAndAnalysisPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[FullRepositoryDict]
    sender: NotRequired[UserDict]


class IssueDependenciesBlockedByAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocked_by_added`."""

    action: Required[Literal["blocked_by_added"]]
    blocked_issue_id: Required[float]
    blocked_issue: Required[IssueDict]
    blocking_issue_id: Required[float]
    blocking_issue: Required[IssueDict]
    blocking_issue_repo: Required[RepositoryDict2]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssueDependenciesBlockedByRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocked_by_removed`."""

    action: Required[Literal["blocked_by_removed"]]
    blocked_issue_id: Required[float]
    blocked_issue: Required[IssueDict]
    blocking_issue_id: Required[float]
    blocking_issue: Required[IssueDict]
    blocking_issue_repo: Required[RepositoryDict2]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssueDependenciesBlockingAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocking_added`."""

    action: Required[Literal["blocking_added"]]
    blocked_issue_id: Required[float]
    blocked_issue: Required[IssueDict]
    blocked_issue_repo: Required[RepositoryDict2]
    blocking_issue_id: Required[float]
    blocking_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssueDependenciesBlockingRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issue-dependencies` webhook with action `blocking_removed`."""

    action: Required[Literal["blocking_removed"]]
    blocked_issue_id: Required[float]
    blocked_issue: Required[IssueDict]
    blocked_issue_repo: Required[RepositoryDict2]
    blocking_issue_id: Required[float]
    blocking_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class SubIssuesParentIssueAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sub-issues` webhook with action `parent_issue_added`."""

    action: Required[Literal["parent_issue_added"]]
    parent_issue_id: Required[float]
    parent_issue: Required[IssueDict]
    parent_issue_repo: Required[RepositoryDict2]
    sub_issue_id: Required[float]
    sub_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class SubIssuesParentIssueRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sub-issues` webhook with action `parent_issue_removed`."""

    action: Required[Literal["parent_issue_removed"]]
    parent_issue_id: Required[float]
    parent_issue: Required[IssueDict]
    parent_issue_repo: Required[RepositoryDict2]
    sub_issue_id: Required[float]
    sub_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class SubIssuesSubIssueAddedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sub-issues` webhook with action `sub_issue_added`."""

    action: Required[Literal["sub_issue_added"]]
    sub_issue_id: Required[float]
    sub_issue: Required[IssueDict]
    sub_issue_repo: Required[RepositoryDict2]
    parent_issue_id: Required[float]
    parent_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class SubIssuesSubIssueRemovedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `sub-issues` webhook with action `sub_issue_removed`."""

    action: Required[Literal["sub_issue_removed"]]
    sub_issue_id: Required[float]
    sub_issue: Required[IssueDict]
    sub_issue_repo: Required[RepositoryDict2]
    parent_issue_id: Required[float]
    parent_issue: Required[IssueDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    sender: NotRequired[UserDict]


class DiscussionTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `discussion` webhook with action `transferred`."""

    action: Required[Literal["transferred"]]
    changes: Required[DiscussionTransferredPayloadChangesDict]
    discussion: Required[DiscussionDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class IssuesTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `issues` webhook with action `transferred`."""

    action: Required[Literal["transferred"]]
    changes: Required[IssuesTransferredPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    issue: Required[WebhooksIssue2Dict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckSuiteCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    check_suite: Required[CheckSuiteCompletedPayloadCheckSuiteDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckSuiteRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    check_suite: Required[CheckSuiteRequestedPayloadCheckSuiteDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckSuiteRerequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_suite` webhook with action `rerequested`."""

    action: Required[Literal["rerequested"]]
    check_suite: Required[CheckSuiteRerequestedPayloadCheckSuiteDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestAssignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `assigned`."""

    action: Required[Literal["assigned"]]
    assignee: Required[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestAssignedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestAutoMergeDisabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_disabled`."""

    action: Required[Literal["auto_merge_disabled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestAutoMergeDisabledPayloadPullRequestDict]
    reason: Required[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestAutoMergeEnabledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `auto_merge_enabled`."""

    action: Required[Literal["auto_merge_enabled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestAutoMergeEnabledPayloadPullRequestDict]
    reason: NotRequired[str]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestDequeuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `dequeued`."""

    action: Required[Literal["dequeued"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestDequeuedPayloadPullRequestDict]
    reason: Required[
        Literal[
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
    ]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestEnqueuedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `enqueued`."""

    action: Required[Literal["enqueued"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestEnqueuedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestLabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `labeled`."""

    action: Required[Literal["labeled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: NotRequired[WebhooksLabelDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestLabeledPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestLockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `locked`."""

    action: Required[Literal["locked"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestLockedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckRunWithSimpleCheckSuiteDict(TypedDict, total=False):
    """A check performed on the code of a given code change."""

    app: Required[Any | None]
    check_suite: Required[SimpleCheckSuiteDict]
    completed_at: Required[None | str]
    conclusion: Required[
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
    ]
    deployment: NotRequired[DeploymentSimpleDict]
    details_url: Required[str]
    external_id: Required[str]
    head_sha: Required[str]
    html_url: Required[str]
    id: Required[int]
    name: Required[str]
    node_id: Required[str]
    output: Required[CheckRunWithSimpleCheckSuiteOutputDict]
    pull_requests: Required[list[PullRequestMinimalDict]]
    started_at: Required[str]
    status: Required[Literal["queued", "in_progress", "completed", "pending"]]
    url: Required[str]


class PullRequestReviewCommentCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `created`."""

    action: Required[Literal["created"]]
    comment: Required[PullRequestReviewCommentCreatedPayloadCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewCommentCreatedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestReviewCommentDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    comment: Required[WebhooksReviewCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewCommentDeletedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestReviewCommentEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_comment` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[WebhooksChangesDict]
    comment: Required[WebhooksReviewCommentDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewCommentEditedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestReviewDismissedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `dismissed`."""

    action: Required[Literal["dismissed"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewDismissedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    review: Required[PullRequestReviewDismissedPayloadReviewDict]
    sender: Required[UserDict]


class PullRequestReviewEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[PullRequestReviewEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewEditedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    review: Required[WebhooksReviewDict]
    sender: Required[UserDict]


class PullRequestReviewSubmittedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review` webhook with action `submitted`."""

    action: Required[Literal["submitted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewSubmittedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    review: Required[WebhooksReviewDict]
    sender: Required[UserDict]


class PullRequestReviewThreadResolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `resolved`."""

    action: Required[Literal["resolved"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewThreadResolvedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]
    thread: Required[PullRequestReviewThreadResolvedPayloadThreadDict]
    updated_at: NotRequired[None | str]


class PullRequestReviewThreadUnresolvedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request_review_thread` webhook with action `unresolved`."""

    action: Required[Literal["unresolved"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestReviewThreadUnresolvedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]
    thread: Required[PullRequestReviewThreadUnresolvedPayloadThreadDict]
    updated_at: NotRequired[None | str]


class PullRequestSynchronizePayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `synchronize`."""

    action: Required[Literal["synchronize"]]
    after: Required[str]
    before: Required[str]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestSynchronizePayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestUnassignedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unassigned`."""

    action: Required[Literal["unassigned"]]
    assignee: NotRequired[Any | None]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestUnassignedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class PullRequestUnlabeledPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unlabeled`."""

    action: Required[Literal["unlabeled"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    label: NotRequired[WebhooksLabelDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestUnlabeledPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class PullRequestUnlockedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `unlocked`."""

    action: Required[Literal["unlocked"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[PullRequestUnlockedPayloadPullRequestDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryTransferredPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository` webhook with action `transferred`."""

    action: Required[Literal["transferred"]]
    changes: Required[RepositoryTransferredPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class TeamEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `team` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    changes: Required[TeamEditedPayloadChangesDict]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: Required[OrganizationDict]
    repository: NotRequired[TeamEditedPayloadRepositoryDict]
    sender: Required[UserDict]
    team: Required[WebhooksTeam1Dict]


class PackageUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `package` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    package: Required[PackageUpdatedPayloadPackageDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RegistryPackageUpdatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `registry_package` webhook with action `updated`."""

    action: Required[Literal["updated"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    registry_package: Required[RegistryPackageUpdatedPayloadRegistryPackageDict]
    repository: NotRequired[RepositoryDict]
    sender: Required[UserDict]


class PullRequestDemilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `demilestoned`."""

    action: Required[Literal["demilestoned"]]
    enterprise: NotRequired[EnterpriseDict]
    milestone: NotRequired[MilestoneDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[WebhooksPullRequest5Dict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class PullRequestMilestonedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `pull_request` webhook with action `milestoned`."""

    action: Required[Literal["milestoned"]]
    enterprise: NotRequired[EnterpriseDict]
    milestone: NotRequired[MilestoneDict]
    number: Required[int]
    organization: NotRequired[OrganizationDict]
    pull_request: Required[WebhooksPullRequest5Dict]
    repository: Required[RepositoryDict]
    sender: NotRequired[UserDict]


class WorkflowRunRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `workflow_run` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]
    workflow: Required[Any | None]
    workflow_run: Required[WorkflowRunRequestedPayloadWorkflowRunDict]


class DependabotAlertAutoDismissedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `auto_dismissed`."""

    action: Required[Literal["auto_dismissed"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertAutoReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `auto_reopened`."""

    action: Required[Literal["auto_reopened"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `created`."""

    action: Required[Literal["created"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertDismissedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `dismissed`."""

    action: Required[Literal["dismissed"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertFixedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `fixed`."""

    action: Required[Literal["fixed"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertReintroducedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `reintroduced`."""

    action: Required[Literal["reintroduced"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class DependabotAlertReopenedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `dependabot_alert` webhook with action `reopened`."""

    action: Required[Literal["reopened"]]
    alert: Required[DependabotAlertDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    enterprise: NotRequired[EnterpriseDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryRulesetEditedPayloadChangesRulesUpdatedDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesRulesUpdated."""

    rule: NotRequired[
        RepositoryRuleBranchNamePatternDict
        | RepositoryRuleCodeScanningDict
        | RepositoryRuleCommitAuthorEmailPatternDict
        | RepositoryRuleCommitMessagePatternDict
        | RepositoryRuleCommitterEmailPatternDict
        | RepositoryRuleCopilotCodeReviewDict
        | RepositoryRuleCreationDict
        | RepositoryRuleDeletionDict
        | RepositoryRuleFileExtensionRestrictionDict
        | RepositoryRuleFilePathRestrictionDict
        | RepositoryRuleMaxFilePathLengthDict
        | RepositoryRuleMaxFileSizeDict
        | RepositoryRuleMergeQueueDict
        | RepositoryRuleNonFastForwardDict
        | RepositoryRulePullRequestDict
        | RepositoryRuleRequiredDeploymentsDict
        | RepositoryRuleRequiredLinearHistoryDict
        | RepositoryRuleRequiredSignaturesDict
        | RepositoryRuleRequiredStatusChecksDict
        | RepositoryRuleTagNamePatternDict
        | RepositoryRuleUpdateDict
        | RepositoryRuleWorkflowsDict
    ]
    changes: NotRequired[RepositoryRulesetEditedPayloadChangesRulesUpdatedChangesDict]


class RepositoryRulesetDict(TypedDict, total=False):
    """A set of rules to apply when specified conditions are met."""

    id: Required[int]
    name: Required[str]
    target: NotRequired[Literal["branch", "tag", "push", "repository"]]
    source_type: NotRequired[Literal["Repository", "Organization", "Enterprise"]]
    source: Required[str]
    enforcement: Required[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[list[RepositoryRulesetBypassActorDict]]
    current_user_can_bypass: NotRequired[Literal["always", "pull_requests_only", "never", "exempt"]]
    node_id: NotRequired[str]
    _links: NotRequired[RepositoryRulesetLinksDict]
    conditions: NotRequired[RepositoryRulesetConditionsDict | dict[str, Any]]
    rules: NotRequired[
        list[
            RepositoryRuleBranchNamePatternDict
            | RepositoryRuleCodeScanningDict
            | RepositoryRuleCommitAuthorEmailPatternDict
            | RepositoryRuleCommitMessagePatternDict
            | RepositoryRuleCommitterEmailPatternDict
            | RepositoryRuleCopilotCodeReviewDict
            | RepositoryRuleCreationDict
            | RepositoryRuleDeletionDict
            | RepositoryRuleFileExtensionRestrictionDict
            | RepositoryRuleFilePathRestrictionDict
            | RepositoryRuleMaxFilePathLengthDict
            | RepositoryRuleMaxFileSizeDict
            | RepositoryRuleMergeQueueDict
            | RepositoryRuleNonFastForwardDict
            | RepositoryRulePullRequestDict
            | RepositoryRuleRequiredDeploymentsDict
            | RepositoryRuleRequiredLinearHistoryDict
            | RepositoryRuleRequiredSignaturesDict
            | RepositoryRuleRequiredStatusChecksDict
            | RepositoryRuleTagNamePatternDict
            | RepositoryRuleUpdateDict
            | RepositoryRuleWorkflowsDict
        ]
    ]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


class DeploymentProtectionRuleRequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `deployment_protection_rule` webhook with action `requested`."""

    action: Required[Literal["requested"]]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[DeploymentDict]
    pull_requests: NotRequired[list[PullRequestDict]]
    repository: Required[RepositoryDict]
    organization: NotRequired[OrganizationDict]
    installation: NotRequired[InstallationDict]
    sender: Required[UserDict]


class CheckRunCompletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `completed`."""

    action: Required[Literal["completed"]]
    check_run: Required[CheckRunWithSimpleCheckSuiteDict]
    installation: NotRequired[InstallationDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckRunCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `created`."""

    action: Required[Literal["created"]]
    check_run: Required[CheckRunWithSimpleCheckSuiteDict]
    installation: NotRequired[InstallationDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class CheckRunRequestedActionPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `requested_action`."""

    action: Required[Literal["requested_action"]]
    check_run: Required[CheckRunWithSimpleCheckSuiteDict]
    installation: NotRequired[InstallationDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    requested_action: NotRequired[CheckRunRequestedActionPayloadRequestedActionDict]
    sender: Required[UserDict]


class CheckRunRerequestedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `check_run` webhook with action `rerequested`."""

    action: Required[Literal["rerequested"]]
    check_run: Required[CheckRunWithSimpleCheckSuiteDict]
    installation: NotRequired[InstallationDict]
    enterprise: NotRequired[EnterpriseDict]
    organization: NotRequired[OrganizationDict]
    repository: Required[RepositoryDict]
    sender: Required[UserDict]


class RepositoryRulesetEditedPayloadChangesRulesDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChangesRules."""

    added: NotRequired[
        list[
            RepositoryRuleBranchNamePatternDict
            | RepositoryRuleCodeScanningDict
            | RepositoryRuleCommitAuthorEmailPatternDict
            | RepositoryRuleCommitMessagePatternDict
            | RepositoryRuleCommitterEmailPatternDict
            | RepositoryRuleCopilotCodeReviewDict
            | RepositoryRuleCreationDict
            | RepositoryRuleDeletionDict
            | RepositoryRuleFileExtensionRestrictionDict
            | RepositoryRuleFilePathRestrictionDict
            | RepositoryRuleMaxFilePathLengthDict
            | RepositoryRuleMaxFileSizeDict
            | RepositoryRuleMergeQueueDict
            | RepositoryRuleNonFastForwardDict
            | RepositoryRulePullRequestDict
            | RepositoryRuleRequiredDeploymentsDict
            | RepositoryRuleRequiredLinearHistoryDict
            | RepositoryRuleRequiredSignaturesDict
            | RepositoryRuleRequiredStatusChecksDict
            | RepositoryRuleTagNamePatternDict
            | RepositoryRuleUpdateDict
            | RepositoryRuleWorkflowsDict
        ]
    ]
    deleted: NotRequired[
        list[
            RepositoryRuleBranchNamePatternDict
            | RepositoryRuleCodeScanningDict
            | RepositoryRuleCommitAuthorEmailPatternDict
            | RepositoryRuleCommitMessagePatternDict
            | RepositoryRuleCommitterEmailPatternDict
            | RepositoryRuleCopilotCodeReviewDict
            | RepositoryRuleCreationDict
            | RepositoryRuleDeletionDict
            | RepositoryRuleFileExtensionRestrictionDict
            | RepositoryRuleFilePathRestrictionDict
            | RepositoryRuleMaxFilePathLengthDict
            | RepositoryRuleMaxFileSizeDict
            | RepositoryRuleMergeQueueDict
            | RepositoryRuleNonFastForwardDict
            | RepositoryRulePullRequestDict
            | RepositoryRuleRequiredDeploymentsDict
            | RepositoryRuleRequiredLinearHistoryDict
            | RepositoryRuleRequiredSignaturesDict
            | RepositoryRuleRequiredStatusChecksDict
            | RepositoryRuleTagNamePatternDict
            | RepositoryRuleUpdateDict
            | RepositoryRuleWorkflowsDict
        ]
    ]
    updated: NotRequired[list[RepositoryRulesetEditedPayloadChangesRulesUpdatedDict]]


class RepositoryRulesetCreatedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_ruleset` webhook with action `created`."""

    action: Required[Literal["created"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    repository_ruleset: Required[RepositoryRulesetDict]
    sender: Required[UserDict]


class RepositoryRulesetDeletedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_ruleset` webhook with action `deleted`."""

    action: Required[Literal["deleted"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    repository_ruleset: Required[RepositoryRulesetDict]
    sender: Required[UserDict]


class RepositoryRulesetEditedPayloadChangesDict(TypedDict, total=False):
    """RepositoryRulesetEditedPayloadChanges."""

    name: NotRequired[RepositoryRulesetEditedPayloadChangesNameDict]
    enforcement: NotRequired[RepositoryRulesetEditedPayloadChangesEnforcementDict]
    conditions: NotRequired[RepositoryRulesetEditedPayloadChangesConditionsDict]
    rules: NotRequired[RepositoryRulesetEditedPayloadChangesRulesDict]


class RepositoryRulesetEditedPayloadDict(TypedDict, total=False):
    """Payload for the GitHub `repository_ruleset` webhook with action `edited`."""

    action: Required[Literal["edited"]]
    enterprise: NotRequired[EnterpriseDict]
    installation: NotRequired[InstallationDict]
    organization: NotRequired[OrganizationDict]
    repository: NotRequired[RepositoryDict]
    repository_ruleset: Required[RepositoryRulesetDict]
    changes: NotRequired[RepositoryRulesetEditedPayloadChangesDict]
    sender: Required[UserDict]


type WebhookPayload = dict[str, Any]
