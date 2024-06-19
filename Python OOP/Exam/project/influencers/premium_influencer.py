from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85       # 85%

    CAMPAIGNS = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8
    }

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * PremiumInfluencer.INITIAL_PAYMENT_PERCENTAGE
        return payment

    def reached_followers(self, campaign_type: str):
        reached_followers = self.followers * self.engagement_rate * PremiumInfluencer.CAMPAIGNS[campaign_type]
        return reached_followers